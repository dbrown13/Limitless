from flask import Blueprint, request, redirect, url_for


workout_bp = Blueprint("workout", __name__)

walk_bp = Blueprint("walk",__name__)

@walk_bp.route('/', methods=['GET', 'POST'])
def walk():
    if request.method == 'POST':
        # Get data from the form
        miles = request.form.get('miles')
        calories = request.form.get('calories')
        water = request.form.get('water')
        
        # Response with submitted data
        return f"""
        <h2>Data Submitted:</h2>
        <p><strong>Miles:</strong> {miles}</p>
        <p><strong>Calories Burned:</strong> {calories}</p>
        <p><strong>Water:</strong> {water} oz</p>
        <a href="/">Go back</a>
        """
    
    # HTML for the form
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Walking Tracker</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }}
            form div {{
                margin: 10px 0;
            }}
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
    </body>
    </html>
    """
    return html
