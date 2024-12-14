from flask import Flask, Blueprint, render_template_string, request, redirect, url_for


about_bp = Blueprint("about", __name__)
 
@about_bp.route('/')
def about():

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Limitless - About Us</title>
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
                background-color: #ddd;
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

            /* Apply border to table and cells */
            table {
                border: 1px hidden black; /* Hidden black border */
            }
            
            th, td {
                border: 1px hidden black; /* Hidden black border */
                padding: 0.5rem; /* Optional: Add padding for content */
            }

            .center {
                margin-left: auto;
                margin-right: auto;
            }
        </style>
    </head>
    <body>
        <nav>
            <ul>
                <li><h2>Limitless</h2></li>
                <li><a href="/home">Home</a></li>
                <li><a href="/workout">Workout</a></li>
                <li><a href="/goals">Goals</a></li>
                <li><a href="/about">About Us</a></li>
                <li style="float:right"><a class="active" href="/logout">Logout</a></li>
                <li style="float:right"><a class="active" href="/profile">Profile</a></li>
            </ul>
        </nav>

        <div class="container">
            <p>Information about us goes here...</p>
            <hr>

            <table class="center">
                <caption><strong>
                    Contact Information
                    
                </strong></caption>
                <thead>
                    <tr>
                        <th scope="col"></th>
                        <th scope="col">Phone</th>
                        <th scope="col">Email</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th scope="row">Technical Support</td>
                        <td>888-111.2222</td>
                        <td>TechSupport@limitless.com</td>
                    </tr>
                    <tr>
                        <th scope="row">Account Support</td>
                        <td>888-333-4444</td>
                        <td>AcctSupport@limitless.com</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """
    return html


