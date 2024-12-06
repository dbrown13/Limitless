from flask import Blueprint, request
import sqlite3
from jinja2 import Template


global insert_html
insert_html = ""
global actList
actList = []

workout_bp = Blueprint("workout", __name__)

walk_bp = Blueprint("walk",__name__)

def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def get_walks(userName):
    global insert_html
    insert_html=""
    # Get database connection
    conn = get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()
    # First pull all existing 
    actType = "walking"
    try:
        res = cur.execute("SELECT * FROM activities")
        #res = cur.execute("SELECT * FROM activities WHERE userName = ? AND activity = ?", (userName, actType))
        result = res.fetchall()
        print_activities(result, userName)
    except:
        print("No walking activities found.")
        result = None
        cur.close()
        conn.close()
        return False
    
    cur.close()
    conn.close()
    return True

def print_activities(result, userName):
    for activity in result:
        global insert_html
        insert_html = insert_html + '<li>' + activity[2] + ':  ' + str(activity[3]) + ' miles, ' + str(activity[4]) + ' calories, ' + str(activity[5]) + 'oz of water</li>\n'
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

@walk_bp.route('/', methods=['GET', 'POST'])
def walk():

    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login
    get_walks(userName)

    if request.method == 'POST':
        # Get data from the form
        miles = request.form.get('miles')
        calories = request.form.get('calories')
        water = request.form.get('water')
        
        result = add_activity(userName, "walking", miles, calories, water)
        if (result == "Successful"):
            print(result)
            message = result
            get_walks(userName)
        else:
            print(result)
            message = result

        # Response with submitted data
        #return f"""
        #<h2>Data Submitted:</h2>
        #<p><strong>Miles:</strong> {miles}</p>
        #<p><strong>Calories Burned:</strong> {calories}</p>
        #<p><strong>Water:</strong> {water} oz</p>
        #<a href="/">Go back</a>
        #"""
    
    # HTML for the form
    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Walking Tracker</title>
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
        <h2>Walking</h2>
        <form method="POST">
            <div>
                <label for="miles">Miles:</label>
                <input type="text" id="miles" name="miles" required>
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
        <h2>Your Current Walks:</h2>
        <form method="POST">
            <ol id="walks" class="list">
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

