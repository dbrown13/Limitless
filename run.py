from flask import Blueprint, request, url_for, redirect
import sqlite3
import database
import getCalories
from jinja2 import Template

global insert_html
insert_html = ""
global actList
actList = []

workout_bp = Blueprint("workout", __name__)

run_bp = Blueprint("run",__name__)

def get_runs(userName):
    global insert_html
    insert_html=""
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    # First pull all existing 
    actType = "running"
    try:
        res = cur.execute("SELECT * FROM activities WHERE userName = ? AND activity = ?", (userName, actType))
        result = res.fetchall()
    except:
        print("Database error")
        result = None
        cur.close()
        conn.close()
        return False
    
    if len(result) == 0:
        print("No running activities found.")
        result = "No running activities found"
    
    print_activities(result, userName)
    
    cur.close()
    conn.close()
    return True

def print_activities(result, userName):
    global insert_html
    insert_html=""
    if result == "No running activities found":
        insert_html = result
    else:
        for activity in result:
            insert_html = insert_html + '<li>' + activity[2] + ':  ' + str(activity[3]) + ' minutes, ' + str(activity[4]) + ' calories, ' + str(activity[5]) + 'oz of water</li>\n'
    
    print(f"html = {insert_html}")
    return True

def add_activity(userName, act, miles, cal, water):
    # Get database connection
    conn = database.get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO activities (userName, activity, actNum, calories, water) VALUES (?, ?, ?, ?, ?)",
                    (userName, act, miles, cal, water)
                    )
        message = "Successful activity add"
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = e.args[0]
        
    conn.commit()
    cur.close()
    conn.close()   

    print(message)
    return message


@run_bp.route('/', methods=['GET', 'POST'])
def run():

    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login
    get_runs(userName)

    if request.method == 'POST':
        # Get data from the form
        minutes = request.form.get('minutes')
        intensity = request.form.get('intensity')
        water = request.form.get('water')
        calories = getCalories.get_calories("running", intensity, minutes)
        if calories == -1:
            print("No weight registered")
            calories = 0
        print(f"calories = {calories}")
        result = add_activity(userName, "running", minutes, calories, water)
        if (result == "Successful activity add"):
            print(result)
            message = result
            get_runs(userName)
        else:
            print(result)
            message = result

    
    # HTML for the form
    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Running Tracker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
                        
            .list {
                text-align: left;
                margin-left: 10px;
            }
                        
            form div {
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
        <h2>Running</h2>
        <form method="POST">
            <div class="act-container">
                <div>
                    <label for="minutes">Minutes:</label>
                    <input type="integer" id="minutes" name="minutes" required>
                </div>
                <div>
                    <label for="intensity">Intensity:</label>
                    <select type= "text" name="intensity" id="intensity" required>
                        <option selected value="low">Low</option>
                        <option value="moderate">Moderate</option>
                        <option value="high">High</option>
                    </select>
                </div>
                <div style="margin-top: 20px;">
            </div>
            <div class="addl-container">
                <div>
                    <label for="water">Water (oz):</label>
                    <input type="text" id="water" name="water" required>
                </div>
            </div>
            <div style="margin-top: 20px;">
                <button type="submit">Submit</button>
            </div>
        </form>
        <hr>
        <h2>Your Current runs:</h2>
        <form method="POST">
            <ol id="runs" class="list">
                {{ actList }}
            </ol>
        </form>
        <br>
        <hr>
        <br>      
    </body>
    </html>
    """)
    return template.render(actList=insert_html)

