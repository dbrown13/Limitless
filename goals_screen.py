from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)

GOALS_FILE = os.path.join(os.path.dirname(__file__), 'goals.txt')

@app.route('/')
def home():
    goals = []
    if os.path.exists(GOALS_FILE):
        with open(GOALS_FILE, 'r') as file:
            goals = file.readlines()

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Flask App</title>
    </head>
    <body>
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
    return render_template_string(html, goals=goals)

@app.route('/submit-goal', methods=['POST'])
def submit_goal():
    goal = request.form.get('goal')
    if goal:
        with open(GOALS_FILE, 'a') as file:
            file.write(goal + '\n')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
