from flask import Blueprint, request, redirect, url_for

rec_bp = Blueprint("rec",__name__)

@rec_bp.route('/', methods=['GET', 'POST'])
def rec():
    workouts = [
        {'name': 'Walking', 'icon': '🚶'},
        {'name': 'Swimming', 'icon': '🏊'},
        {'name': 'Cycling', 'icon': '🚴'},
    ]
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Workout Recommendation</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }
            header {
                background-color: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }
            nav {
                display: flex;
                justify-content: center;
                background-color: #eee;
                padding: 10px 0;
            }
            nav a {
                margin: 0 15px;
                text-decoration: none;
                color: #333;
                font-weight: bold;
            }
            nav a.active {
                color: blue;
                border-bottom: 2px solid blue;
            }
            .content {
                padding: 20px;
                text-align: center;
            }
            .workout-options {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin-top: 20px;
            }
            .workout-option {
                text-align: center;
            }
            .workout-option div {
                font-size: 40px;
            }
            .footer-link {
                color: blue;
                text-decoration: underline;
                margin-top: 20px;
                display: inline-block;
            }
        </style>
    </head>
    <body>

        <div class="content">
            <h2>Recommendation</h2>
            <p>Based on your past activity, these are the workouts we have chosen for you:</p>
            <div class="workout-options">
                {% for workout in workouts %}
                <div class="workout-option">
                    <div>{{ workout.icon }}</div>
                    <p><strong>{{ workout.name }}</strong></p>
                </div>
                {% endfor %}
            </div>
            <a href="#" class="footer-link">Select one to track!</a>
        </div>
    </body>
    </html>
    """ 
    return html
