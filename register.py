from flask import Flask, Blueprint, request, redirect, url_for, render_template
import sqlite3
import database

register_bp = Blueprint("register", __name__)

# Global variables
valFirst = ""
valLast = ""
valEmail = ""
valUser = ""
valWt = ""
valPW = ""
valPW2 = ""

def add_user(firstName, lastName, email, userName, userPW, userWeight):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (firstName, lastName, email, userName, userPW, userWeight) VALUES (?, ?, ?, ?, ?, ?)",
                    (firstName, lastName, email, userName, userPW, userWeight)
                    )
        message = "Successful registration"
    except sqlite3.IntegrityError:
        message = "User Name already exists."
        print(message)
        cur.close()
        conn.close()
        return message
        
    conn.commit()
    cur.close()
    conn.close()    

    return message

@register_bp.route("/", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        userEmail = request.form["userEmail"]
        userName = request.form["userName"]
        userWeight = request.form["userWeight"]
        userPW = request.form["userPW"]
        userPW2 = request.form["userPW2"]

        # Retain field values
        global valFirst
        valFirst=firstName
        global valLast
        valLast=lastName
        global valEmail
        valEmail=userEmail
        global valUser
        valUser=userName
        global valWt
        valWt = userWeight

        if (userPW != userPW2):
            message = "Passwords must match."
        else: 
            message = add_user(firstName, lastName, userEmail, userName, userPW, userWeight)

        if (message == "Successful"):
            message = "Successful registration!"
            valFirst=""
            valLast=""
            valEmail=""
            valUser=""
            valWt=""
            return redirect(url_for("login.login"))  # Redirect to the login page

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registration Screen</title>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="text-align: center; width: 500px; font-family: fantasy">
            <h1>Limitless</h1>
            <form method="POST">
                <div style="font-family: sans-serif">
                    <label>First Name:</label>
                    <input type="text" name="firstName" placeholder="Enter first name" value=\"{valFirst}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Last Name:</label>
                    <input type="text" name="lastName" placeholder="Enter last name" value=\"{valLast}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Email:</label>
                    <input type="text" name="userEmail" placeholder="Enter email" value=\"{valEmail}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Username/Email:</label>
                    <input type="text" name="userName" placeholder="Enter user name or email" value=\"{valUser}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Current Weight:</label>
                    <input type="text" name="userWeight" placeholder="Enter current weight" value=\"{valWt}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Password:</label>
                    <input type="password" name="userPW" placeholder="Enter password" value=\"{valPW}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Confirm Password:</label>
                    <input type="password" name="userPW2" placeholder="Confirm password" value=\"{valPW2}\" required>
                </div>
                <div style="margin-top: 20px; font-family: sans-serif">
                    <button type="submit">Register</button>
                </div>
            </form>
            <div style="margin-top: 15px; color: blue; text-decoration: underline;">
                <a href="/">Return to Login</a>
            </div>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """
    return html
