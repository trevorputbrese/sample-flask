from flask import Flask
from flask import render_template
from flask_pyctuator.flask_pyctuator import FlaskPyctuator


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

FlaskPyctuator(
    app,
)

app.run(debug=False, port=8081, host="0.0.0.0")
