#!/usr/bin/python3
"""Is it a number?"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    formated_string = text.replace("_", " ")
    return f"C {formatted_string}"


@app.route("/python", strict_slashes=False)
def python():
    formated_string = text.replace("_", " ")
    return f"Python {formated_string}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    formated_string = text.replace("_", " ")
    return f"Python {formated_string}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_int(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
