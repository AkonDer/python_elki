from flask import Flask, render_template
import calculation

app = Flask(__name__)


@app.route("/404")
def index():
    return render_template("404.html")


@app.route("/")
def page_elki():
    bar, img = calculation.run()
    return render_template("index.html", bar=bar, img=img)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')


# TODO сделать список всех выходных дней в году
# TODO сделать работу в зависимости от выходных дней
