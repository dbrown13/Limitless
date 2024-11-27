from flask import Flask

app = Flask(__name__)

@app.route('/')
def profile():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - Profile Page</title>
        <style>
            /* General Styles */
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

            .container {
                text-align: center;
                padding: 50px 20px;
            }

            .profile-icon {
                font-size: 80px;
                border: 2px solid #000;
                border-radius: 50%;
                display: inline-block;
                width: 100px;
                height: 100px;
                line-height: 100px;
                text-align: center;
                margin-bottom: 20px;
                color: #000;
            }

            .profile-details {
                border: 1px solid #333;
                padding: 20px;
                display: inline-block;
                text-align: left;
                background-color: #fff;
                margin-bottom: 20px;
            }

            .buttons {
                margin-top: 20px;
            }

            .buttons button {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                margin: 0 10px;
            }

            .buttons button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/">Home</a></li>
                <li><a href="#workout">Workout</a></li>
                <li><a href="#goals">Goals</a></li>
                <li style="float:right"><a class="active" href="/">Account</a></li>
            </ul>
        </nav>

        <div class="container">
            <div class="profile-icon">
                <span>&#128100;</span> <!-- Unicode for user icon -->
            </div>
            <div class="profile-details">
                <p><strong>Name:</strong> [Your Name]</p>
                <p><strong>Address:</strong> [Your Address]</p>
                <p><strong>Phone Number:</strong> [Your Phone Number]</p>
                <p><strong>Biography:</strong> [Short Bio]</p>
            </div>
            <div class="buttons">
                <button>Edit Profile</button>
                <button>Logout</button>
            </div>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)

