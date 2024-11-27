from flask import Blueprint

goals_bp = Blueprint("goals", __name__)

@goals_bp.route("/")
def goals():
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
        <form action="/submit-goal" method="POST">
            <input type="text" name="goal" placeholder="Enter your goal" required>
            <button type="submit">Submit</button>
        </form>
        <h2>Your Goals:</h2>
        <ul>
            {% for goal in goals %}
                <li>{{ goal.strip() }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return html
