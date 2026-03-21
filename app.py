from flask import *

from routes.students_routes import *
from routes.authors_routes import *
from flask_migrate import Migrate
from models import *
from sqlalchemy import text

from db import *

from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/db-health")
def db_health():
  try:
    db.session.execute(text("SELECT 1"))
    return {"status": "Ok","database":"Connected"}
  except Exception as e:
    return { "status" : str(e)}


@app.route("/")
def home():
  return render_template("home.html")

# Register and Login for students
app.register_blueprint(student_bp, url_prefix="/student")

# Register and Login for author
app.register_blueprint(author_bp, url_prefix="/author")



# if __name__ == "__main__":

#   app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)