from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    dict = {"Station": station, "date":date, "temperature": 24}
    return dict

app.run(debug=True)