from flask import Blueprint, request
import sqlite3
import userStore

#global goalList
#goalList = None

goals_bp = Blueprint("goals", __name__)

def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn
def get_goals(userName):
    goalList = []
    if request.method == "GET":
        # Get database connection
        conn = get_db_connection()
        # Create cursor and run select to look for username
        cur = conn.cursor()
        # First pull all existing goals
        print(f"pull existing goals for {userName}")
        try:
            result = cur.execute("SELECT goal FROM goals WHERE userName = ?", (userName,))
            result = result.fetchall()
            print(goals)
        except:
            print("No existing goals found.")
            result = None
            return goalList
        cur.close()
        conn.close()
        for goal in result:
            goalList.append(goal[0])
            print(goal[0])
            print(goalList)
        print("return goals")
        return goalList

def add_goal(userName, goal):
    print(f"In add userName = {userName}")
    print(f"In add goal = {goal}")
    # Get database connection
    conn = get_db_connection()
    # Create cursor and run select to look for username
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO goals (userName, goal) VALUES (?, ?)",
                    (userName, goal)
                    )
    except sqlite3.Error as e:
        print("Error:", e.args[0])
        message = "An error occurred."
        print("An error occurred")
        cur.close()
        conn.close()
        return message
        
    conn.commit()
    cur.close()
    conn.close()    

    return "Successful"

@goals_bp.route("/", methods=('GET', 'POST'))
def goals():
    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login
    goals = get_goals(userName)
    print("goals")
    print(goals)
    if goals:
        for item in goals:
            print(f"Goal = {item}")

    if request.method == "POST":
        goal = request.form["goal"]

        print(f"userName = {userName}")
        print(f"goal = {goal}")
        result = add_goal(userName, goal)
        if (result == "Successful"):
            message = "Goal added!"
        else:
            message = "Error occurred; goal not added."


    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Flask App</title>
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
        
        <h1>Enter your personal goals:</h1>
        <form method="POST">
            <input type="text" name="goal" placeholder="Enter your goal" required>
            <button type="submit">Submit</button>
        </form>
        <h2>Your Goals:</h2>
        <ul>
            {% for goal in goalList %}
                <li>{{ goal.strip() }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return html
