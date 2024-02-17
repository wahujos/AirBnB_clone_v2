#!/usr/bin/python3
"""Python is cool!"""

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
    formatted_string = text.replace("_", " ")
    return f"C {formatted_string}"

@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    formatted_string = text.replace("_", " ")
    return f"Python {formatted_string}"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    formatted_string = text.replace("_", " ")
    return f"Python {formatted_string}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
