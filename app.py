from flask import Flask

# Importing blueprints from other files
from login import login_bp
from register import register_bp
from home import home_bp
from workout import workout_bp
from account import account_bp
from goals import goals_bp
from walk import walk_bp
from rec import rec_bp

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(login_bp)
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(workout_bp, url_prefix="/workout")
app.register_blueprint(account_bp, url_prefix="/account")
app.register_blueprint(goals_bp, url_prefix="/goals")
app.register_blueprint(walk_bp, url_prefix="/walk")
app.register_blueprint(rec_bp, url_prefix="/rec")



if __name__ == "__main__":
    app.run(debug=True)

