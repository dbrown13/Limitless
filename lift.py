from flask import Blueprint, request
import sqlite3
from jinja2 import Template


global insert_html
insert_html = ""
global actList
actList = []

#workout_bp = Blueprint("workout", __name__)

lift_bp = Blueprint("lift",__name__)

def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def get_lifts(userName):
    global insert_html
    insert_html=""
    # Get database connection
    conn = get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    # First pull all existing 
    actType = "lifting"
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
        print("No lifting activities found.")
        result = "No lifting activities found"
    
    print_activities(result, userName)

    cur.close()
    conn.close()
    return True

def print_activities(result, userName):
    global insert_html
    if result == "No lifting activities found":
        insert_html = result
    else:
        for activity in result:
            insert_html = insert_html + '<li>' + activity[2] + ':  ' + str(activity[3]) + ' reps, ' + str(activity[4]) + ' calories, ' + str(activity[5]) + 'oz of water</li>\n'
    
    print(f"html = {insert_html}")
    return True

def add_activity(userName, act, miles, cal, water):
    # Get database connection
    conn = get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO activities (userName, activity, actNum, calories, water) VALUES (?, ?, ?, ?, ?)",
                    (userName, act, miles, cal, water)
                    )
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = e.args[0]
        cur.close()
        conn.close()
        return message
        
    conn.commit()
    cur.close()
    conn.close()    
    print("Successful add")

    return "Successful"

@lift_bp.route('/', methods=['GET', 'POST'])
def lift():

    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login
    get_lifts(userName)

    if request.method == 'POST':
        # Get data from the form
        reps = request.form.get('reps')
        calories = request.form.get('calories')
        water = request.form.get('water')
        
        result = add_activity(userName, "lifting", reps, calories, water)
        if (result == "Successful"):
            print(result)
            message = result
            get_lifts(userName)
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
        <title>Lifting Tracker</title>
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
        <h2>Lifting</h2>
        <form method="POST">
            <div>
                <label for="reps">Reps:</label>
                <input type="text" id="reps" name="reps" required>
            </div>
            <div>
                <label for="calories">Calories Burned:</label>
                <input type="text" id="calories" name="calories" required>
            </div>
            <div>
                <label for="water">Water (oz):</label>
                <input type="text" id="water" name="water" required>
            </div>
            <div style="margin-top: 20px;">
                <button type="submit">Submit</button>
            </div>
        </form>
        <hr>
        <h2>Your Current Lifts:</h2>
        <form method="POST">
            <ol id="reps" class="list">
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

