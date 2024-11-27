from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simple check for demonstration (replace with real check later)
        if username == "user" and password == "1234":
            message = "Login Successful!"

    html = f"""
    <!DOCTYPE html>

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Screen</title>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="text-align: center; width: 500px; font-family: fantasy">
            <h1>Limitless</h1>
            <form method="POST">
                <div style="font-family: sans-serif">
                    <label>Username/Email:</label>
                    <input type="text" name="username" required>
                </div>
                <div style="margin-top: 10px; font-family: sans-serif">
                    <label>Password:</label>
                    <input type="password" name="password" required>
                </div>
                <div style="margin-top: 20px; font-family: sans-serif">
                    <button type="submit">Login</button>
                </div>
            </form>
            <div style="margin-top: 15px; color: blue; text-decoration: underline;">
                <a href="#">Create an account</a>
            </div>
            <p>{message}</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
