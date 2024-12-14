from flask import Blueprint

logout_bp = Blueprint("logout", __name__)

@logout_bp.route("/")
def logout():
    message = ""

    import userStore
    userStore.set_user("")
    userStore.set_weight(0)
    message = "userStore cleared."

    html = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Screen</title>
    </head>
    <body style="display: flex; align-items: center; justify-content: center; height: 100vh;">
        <div style="text-align: center; width: 500px; font-family: fantasy">
            <h1>Thank you for using Limitless!</h1>
            <br>
            <h2>See you next time...</h2>
        </div>
    </body>
    </html>
    """
    return html
