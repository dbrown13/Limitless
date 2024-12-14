from flask import Flask, Blueprint, render_template_string, request, redirect, url_for
from jinja2 import Template
import sqlite3
import database
import userStore

profile_bp = Blueprint("profile_screen", __name__)

# profile structure
profile_data = {
    "firstName": "Enter first name here",
    "lastName": "Enter last name here",
    "email": "Enter email here",
    "userName": "Enter user name here",
    "weight": "Enter weight here",
    "userBio": "Enter biography here"
}

def get_data():
    #userName = userStore.get_user()
    userName = "diverdib" #Temporary

    # Get database connection
    conn = database.get_db_connection()
    # Create cursor
    cur = conn.cursor()

    try:
        cur.execute('SELECT firstName, lastName, email, userWeight, userBio, userPhoto FROM users WHERE userName = ?', (userName,))
        message = "Successful retrieval"
        data = cur.fetchone()
        if data == None:
            message = "No data retrieved"
            print(message)
        else:
            global profile_data
            profile_data.update({"firstName": data[0]})
            profile_data.update({"lastName": data[1]})
            profile_data.update({"userName": userName})
            profile_data.update({"email": data[2]})
            profile_data.update({"weight": data[3]})
            profile_data.update({"userBio": data[4]})
    except sqlite3.IntegrityError:
        message = "User Name does not exist."
        print(message)
        cur.close()
        conn.close()
        return message    

@profile_bp.route('/')
def profile():
    get_data()

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Profile Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }

            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            nav li a:hover {
                background-color: lightblue;
                color: black;
            }

            .active {
                background-color: lightskyblue;
                color: black;
            }

            .container {
                text-align: center;
                padding: 50px 20px;
            }

            .profile-icon {
                font-size: 80px;
                border: 2px solid #000;
                border-radius: 50%;
                display: inline-block;
                width: 100px;
                height: 100px;
                line-height: 100px;
                text-align: center;
                margin-bottom: 20px;
                background-color: #ddd;
            }

            .profile-details {
                border: 1px solid #333;
                padding: 20px;
                display: inline-block;
                text-align: left;
                background-color: #fff;
                margin-bottom: 20px;
            }

            .buttons {
                margin-top: 20px;
            }

            .buttons button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin: 0 10px;
            }

            .buttons button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home">Home</a></li>
                <li><a href="/workout">Workout</a></li>
                <li><a href="/goals">Goals</a></li>
                <li><a href="/about">About Us</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
            </ul>
        </nav>

        <div class="container">
            <div class="profile-icon">
                <span>&#128100;</span> <!-- Unicode for user icon -->
            </div>
            <div class="profile-details">
                <p><strong>First Name:</strong> {{ profile.firstName }}</p>
                <p><strong>Last Name:</strong> {{ profile.lastName }}</p>
                <p><strong>Username:</strong> {{ profile.userName }}</p>
                <p><strong>Email:</strong> {{ profile.email}}
                <p><strong>Weight:</strong> {{ profile.weight }}</p>
                <p><strong>Biography:</strong> {{ profile.userBio }}</p>
            </div>
            <div class="buttons">
                <form action="/edit_profile" style="display: inline;">
                    <button type="submit">Edit Profile</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, profile=profile_data)


edit_profile_bp = Blueprint("edit_profile", __name__)

# profile structure
profile_data = {
    "firstName": "Enter first name here",
    "lastName": "Enter last name here",
    "email": "Enter email here",
    "userName": "Enter user name here",
    "weight": "Enter weight here",
    "userBio": "Enter biography here"
}

def update_user(firstName, lastName, email, userWeight, userBio, userName):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET firstName=?, lastName=?, email=?, userWeight=?, userBio=? WHERE userName=?", (firstName, lastName, email, userWeight, userBio, userName))
        message = "Successful profile update!"
        print(message)
        conn.commit()
        cur.close()
        conn.close()
        get_data() # update profile
        return message
    
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = e.args[0]
        cur.close()
        conn.close()
        return message
        

@edit_profile_bp.route("/", methods=["GET", "POST"])
def edit_profile():
    get_data()

    message = ""
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        userEmail = request.form["userEmail"]
        userWeight = request.form["userWeight"]
        userBio = request.form["userBio"]

        userName = "diverdib"
        #userName = userStore.get_user()
        if userName:
            message = update_user(firstName, lastName, userEmail, userWeight, userBio, userName)
        # userName not in userStore - redirect to login
        else: 
            message="Are you logged in?"
            return redirect(url_for("login.login"))
        
        if (message == "Successful profile update"):
            print(message)

            return redirect(url_for('home.home'))  # Redirect to the profile page

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Profile Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            nav ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            nav li {
                float: left;
            }

            nav li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding: 14px 16px;
                margin: 0;
            }

            nav li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }

            nav li a:hover {
                background-color: lightblue;
                color: black;
            }

            .active {
                background-color: lightskyblue;
                color: black;
            }

            .container {
                text-align: center;
                padding: 50px 20px;
            }

            .profile-icon {
                font-size: 80px;
                border: 2px solid #000;
                border-radius: 50%;
                display: inline-block;
                width: 100px;
                height: 100px;
                line-height: 100px;
                text-align: center;
                margin-bottom: 20px;
                background-color: #ddd;
            }

            .profile-details {
                border: 1px solid #333;
                padding: 20px;
                display: inline-block;
                text-align: left;
                background-color: #fff;
                margin-bottom: 20px;
            }

            .buttons {
                margin-top: 20px;
            }

            .buttons button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin: 0 10px;
            }

            .buttons button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="text-align: center; width: 500px; font-family: fantasy">
            <h1>Limitless</h1>
            <h3>Edit Profile</h3>
            <br>
            <form method="POST">
                <div style="font-family: sans-serif">
                    <label>First Name:</label>
                    <input type="text" name="firstName" placeholder="Enter first name" value={{ profile.firstName }} required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Last Name:</label>
                    <input type="text" name="lastName" placeholder="Enter last name" value={{ profile.lastName }} required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Email:</label>
                    <input type="text" name="userEmail" placeholder="Enter email" value={{ profile.email }} required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Current Weight:</label>
                    <input type="text" name="userWeight" placeholder="Enter current weight" value={{ profile.weight }} required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Short Biography:</label>
                    <textarea id="userBio" name="userBio" rows="4" cols="40">{{ profile.userBio }}</textarea>
                </div>

                <div class="buttons" style="margin-top: 20px; font-family: sans-serif">
                    <button type="submit">Update</button>
                </div>
            </form>
            <div style="margin-top: 15px; color: blue; text-decoration: underline;">
                <a href="/profile">Return to Profile</a>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, profile=profile_data)
