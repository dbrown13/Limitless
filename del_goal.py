from flask import Blueprint, request, redirect, url_for
import sqlite3
import database
from jinja2 import Template

global insert_html
insert_html = ""
global goalList
goalList = []

del_goal_bp = Blueprint("goals/delete", __name__)

def get_goals(userName):
    print("get goals")
    global insert_html
    insert_html=""
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    # First pull all existing goals
    try:
        result = cur.execute("SELECT goal FROM goals WHERE userName = ?", (userName,))
        result = result.fetchall()
        print_goals(result, userName)
    except:
        print("No existing goals found.")
        result = None
        cur.close()
        conn.close()
        return False
    
    cur.close()
    conn.close()
    return True

def print_goals(result, userName):
    print("print goals")
    global goalList
    goalList = []
    #goalNum = 0
    for goal in result:
        #goalNum=goalNum+1
        goalList.append(goal[0])
        global insert_html
        #insert_html= insert_html + '<li>' + goal[0] + '<button class="del_button" type="submit" name="del_goal" id="button"' + str(goalNum) + '>Delete</button></li>\n'
        insert_html= insert_html + '<li>' + goal[0] + '</li>\n'
        print(insert_html)
    return True

def del_num(userName, num):
    print("del goal")
    global goalList
    print(f"Length = {len(goalList)}")
    print(f"num = {num}")
    if num >= len(goalList):
        message = "The goal list is not that long"
        return message
    print(goalList[num])    
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM goals WHERE userName=? and goal=?",
                    (userName, goalList[num])
                    )
        message = "Successful delete"
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

@del_goal_bp.route('/', methods=('GET', 'POST'))
def del_goal():
    print("delete goal")
    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login
    get_goals(userName)
    print("after get_goals")
    print(request)
    if request.method == "POST":
        print("delete")            
        goalNum = request.form["del_goal"]
        result = del_num(userName, int(goalNum)-1)
        if (result == "Successful"):
            print(result)
            message = result
            get_goals(userName)
        else:
            print(result)
            message = result

    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless</title>
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
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }

            .goal-form {
                margin-bottom: 20px;
            }

            .goal-form input {
                padding: 10px;
                width: 70%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            .goal-form button {
                padding: 10px 20px;
                background-color: lightblue;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
            }

            .goal-form button:hover {
                background-color: #0056b3;
            }

            .goals-list {
                margin-top: 20px;
                list-style-type: none;
                padding: 0;
            }

            .goals-list li {
                background-color: #fff;
                margin: 10px auto;
                padding: 15px;
                width: 50%;
                text-align: left;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .goals-form-container {
                border: 2px solid lightblue;
                padding: 5px;
                width: 80%;
            }

            .goals-container {
                border: 2px solid lightblue;
                padding: 5px;
                width: 80%;
            }

            .delete-button {
                background-color: #FF0000;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
                cursor: pointer;
            }

            .form-submit {
                background-color: darkgray;
                color: white;
                border-radius: 2px;
            }

            .form-submit:hover {
                background-color: lightblue;
                color: black;
            }

            .delete-button:hover {
                background-color: #CC0000;
            }
        </style>                          
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home/">Home</a></li>
                <li><a href="/workout/" class="active">Workout</a></li>
                <li><a href="/goals/">Goals</a></li>
            </ul>
        </nav>
        
        <h1>Delete a Goal</h1>
        <hr>
        <h2>Your Current Goals:</h2>
        <form method="POST">
            <ol id="goals">
                {{ goalsList }}
            </ol>
        </form>
        <br><hr><br>
        <form method="POST">
            <input type="text" name="del_goal" placeholder="Enter number of goal you would like to delete" required>
            <button type="submit">Submit</button>
        </form>
        <br>
        <hr>
        <br>
        <a href=
        </body>
    </html>
    """)
    return template.render(goalsList=insert_html)

