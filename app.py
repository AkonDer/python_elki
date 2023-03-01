from flask import Flask, render_template
import calculation

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/elki/")
def elki():
    bar = calculation.run()
    return render_template("elki.html", bar=bar)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
