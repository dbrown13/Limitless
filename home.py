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
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }

            li {
                float: left;
            }

            li h2 {
                display: block;
                color: lightblue;
                text-align: center;
                padding-left: 10px;
                text-decoration: none;
            }

            li a {
                display: block;
                color: white;
                text-align: center;
                padding-top: 27px;
                padding-left: 30px;
                text-decoration: none;
            }

            /* Change the link color to #111 (black) on hover */
            li a:hover {
                color: lightblue;
            }

            .active {
                color: white;
                padding-right: 14px;
                border-radius: 12px;
            }

            #achievements-card {
                border: 2px solid lightblue;
                padding: 50px;
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
                color: black;
                display: block;
                float: right;
            }
            
            .cards-container {
                width: 100%;
                margin: 0 auto;
                display: inline-block;
                text-align: center;
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



