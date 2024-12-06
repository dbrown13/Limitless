from flask import Blueprint, request, redirect, url_for

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Redirect to the workout page if the Workout button is clicked
        if request.form.get("action") == "Workout":
            return redirect(url_for("workout.workout"))  
        if request.form.get("action") == "Account":
            return redirect(url_for("account.account")) 
        if request.form.get("action") == "Goals":
            return redirect(url_for("goals.goals")) 

    # HTML for the home page
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
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

            #achievements-card {
                border: 2px solid lightblue;
                padding: 50px;
                margin-left: 25%;
                color: black;
                display: block;
                float: left;
            }

            #progress-card {
                border: 2px solid lightblue;
                padding: 50px;
                color: black;
                display: inline-block;
            }

            #goals-card {
                border: 2px solid lightblue;
                padding: 50px;
                margin-right: 25%;
                color: black;
                display: block;
                float: right;
            }
            
            .cards-container {
                width: 100%;
                margin: 0 auto;
                display: inline-block;
                text-align: center;
                padding: 10px;
            }

            .summary-container {
                border: 2px solid lightgray;
                width: 80%;
                margin: 10%;
                padding: 10px;
                color: black;
            }
    </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home/">Home</a></li>
                <li><a href="/workout/">Workout</a></li>
                <li><a href="/goals/">Goals</a></li>
                <li style="float:right"><a class="active" href="/account/">Account</a></li>            
            </ul>
        </nav>

        <div class="container">
            <div class="summary-container">
                <h3>Weekly Summary:</h3>
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis 
                    nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore 
                    eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt 
                    in culpa qui officia deserunt mollit anim id est laborum.
                </p>
            </div>

            <div class="cards-container">
                <div class="card" id="achievements-card">
                    <h2>Achievements</h2>
                    <p>Badges will go here</p>
                </div>
                <div class="card" id="progress-card">
                    <h2>Progress</h2>
                    <p>Progress will go here</p>
                </div>
                <div class="card" id="goals-card">
                    <h2>Goals</h2>
                    <p>Goals will go here</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html



