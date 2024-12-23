from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    data = pd.read_excel("monika_calendar.xlsx", header=None)
    tiles = [{"text": row[1], "link": row[2]} for row in data.values]
    return render_template("index.html", tiles=tiles)

@app.route("/tiles")
def get_tiles():
    data = pd.read_excel("monika_calendar.xlsx", header=None)
    tiles = [{"text": row[1], "link": row[2]} for row in data.values]
    return jsonify(tiles)

if __name__ == "__main__":
    app.run(debug=True)
