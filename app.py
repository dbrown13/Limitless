from flask import Flask

# Importing blueprints from other files
from login import login_bp
from register import register_bp
from home import home_bp
from workout import workout_bp
from account import account_bp
from goals import goals_bp
from del_goal import del_goal_bp
from walk import walk_bp
from lift import lift_bp
from hiit import hiit_bp
from run import run_bp
from yoga import yoga_bp
from swim import swim_bp
from cycle import cycle_bp
from rec import rec_bp
from weight import weight_bp

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(login_bp)
app.register_blueprint(register_bp, url_prefix="/register")
app.register_blueprint(home_bp, url_prefix="/home")
app.register_blueprint(workout_bp, url_prefix="/workout")
app.register_blueprint(account_bp, url_prefix="/account")
app.register_blueprint(goals_bp, url_prefix="/goals")
app.register_blueprint(del_goal_bp, url_prefix="/delete")
app.register_blueprint(walk_bp, url_prefix="/walk")
app.register_blueprint(lift_bp, url_prefix="/lift")
app.register_blueprint(hiit_bp, url_prefix="/hiit")
app.register_blueprint(run_bp, url_prefix="/run")
app.register_blueprint(yoga_bp, url_prefix="/yoga")
app.register_blueprint(swim_bp, url_prefix="/swim")
app.register_blueprint(cycle_bp, url_prefix="/cycle")
app.register_blueprint(rec_bp, url_prefix="/rec")
app.register_blueprint(weight_bp, url_prefix="/weight")

if __name__ == "__main__":
    app.run(debug=True)

