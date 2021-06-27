from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)


@app.route("/")
def about():
    return render_template("about.html")

@app.route("/bmi")
def bmi():
    return render_template("bmi.html")

@app.route("/edu")
def edu():
    return render_template("edu.html")

@app.route("/cal")
def cal():
    return render_template("cal.html")


if __name__ == "__main__":
    app.run(debug=True)