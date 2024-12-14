from flask import Flask, Blueprint, request, redirect, url_for, render_template
import sqlite3
import database

resetPW_bp = Blueprint("resetPW", __name__)

#Global variables
valUser = ""
valEmail = ""

def check_user(name,email):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    cur.execute('SELECT userPW FROM users WHERE userName = ? and email = ?', (name, email))    
    # First row returned (should be only)
    row = cur.fetchone()
    # Close connection
    conn.close()
    # Nothing returned - user not found
    if row is None: 
        # user not found
        print("User name not found")
        return False
    else:
        print("User found")
        return True

def updatePW(name, pw):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET userPW = ? WHERE userName = ?",(pw, name))
        message = "Password successfully updated"
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = e.args[0]
        cur.close()
        conn.close()
        return message
        
    conn.commit()
    cur.close()
    conn.close()    

    return message

@resetPW_bp.route("/", methods=["GET", "POST"])
def resetPW():
    message = ""
    if request.method == "POST":
        userEmail = request.form["userEmail"]
        userName = request.form["userName"]
        userPW = request.form["userPW"]
        userPW2 = request.form["userPW2"]

        # Retain field values

        global valUser
        valUser=userName
        global valEmail
        valEmail=userEmail

        if (userPW != userPW2):
            message = "Passwords must match."
        else: 
            if check_user(userName,userEmail):
                message = updatePW(userName, userPW)

        if (message == "Password successfully updated"):
            print(message)
            return redirect(url_for("login.login"))  # Redirect to the login page
        else:
            print("Contact admin - something is wrong!")


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
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Email:</label>
                    <input type="text" name="userEmail" placeholder="Verify email" value=\"{valEmail}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Username/Email:</label>
                    <input type="text" name="userName" placeholder="Verify username" value=\"{valUser}\" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Password:</label>
                    <input type="password" name="userPW" placeholder="Enter new password"  required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Confirm Password:</label>
                    <input type="password" name="userPW2" placeholder="Confirm new password"  required>
                </div>
                <div style="margin-top: 20px; font-family: sans-serif">
                    <button type="submit">Update</button>
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
