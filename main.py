from flask import Flask, render_template

app = Flask(__name__)


@app.route("/api/v1")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station_code>/<date>")
def data(station_code, date):
    return {
        "Place": station_code,
        "Date": date,
        "Temperature": 32
    }


app.run(debug=True)
