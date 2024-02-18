#!/usr/bin/python3
"""Odd or even? a flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    formated_text = text.replace("_", " ")
    return f"C {formated_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    formated_text = text.replace("_", " ")
    return f"Python {formated_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_int(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    if n % 2 == 0:
        res = 'even'
    else:
        res = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
