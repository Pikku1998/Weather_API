import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<year>/<month>")
def data(year, month):
    month = month.upper()
    df = pd.read_csv('temperatures/temperatures.csv')
    temperature = df.loc[df['YEAR'] == int(year)][month].squeeze()

    return {
        "Month and Year": month + "-" + str(year),
        "Temperature": temperature
    }


if __name__ == "__main__":
    app.run(debug=True)
