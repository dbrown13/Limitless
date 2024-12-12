from flask import Blueprint, request
import sqlite3
import userStore
import database

weight_bp = Blueprint("weight",__name__)

@weight_bp.route('/', methods=['GET', 'POST'])
def weight():
    #userName = userStore.get_user()
    userName="diverdib" # Temporary
    # if this doesn't work, something is wrong with login

    if request.method == 'POST':
        # Get data from the form
        weight = float(request.form.get('weight'))
        print(f"weight = {weight}")
        database.update_Weight(userName,weight)
        userStore.set_weight(weight)
        print(userStore.get_weight())

    
    html = """
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
        <h2>Please enter your current weight</h2>
        <form method="POST">
            <div>
                <label for="weight">Current weight:</label>
                <input type="number" step="0.1" id="weight" name="weight" required>
            </div>
            <div style="margin-top: 20px; font-family: sans-serif">
                <button type="submit">Submit</button>
            </div>
        </form>

    </body>
    </html>
    """
    return html