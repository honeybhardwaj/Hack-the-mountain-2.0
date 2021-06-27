from flask import Flask, redirect, url_for, render_template, request

app=Flask(__name__)


@app.route("/")
def about():
    return render_template("about.html")

@app.route("/bmi",methods=["POST","GET"])
def bmi():
    if request.method == "POST":
        height = request.form["height"]
        weight = request.form["weight"]
        return redirect(url_for("calc", h=height, w=weight))
    
    else:
        return render_template("bmi.html")

@app.route("/edu")
def edu():
    return render_template("edu.html")


@app.route("/calcbmi/<h>/<w>")
def calc(h,w):
    BMI = int(w)/((int(h)/100)**2)
    if BMI <= 18.4:
        str="You are underweight."
    elif BMI <= 24.9:
        str="You are healthy."
    elif BMI <= 29.9:
        str="You are over weight."
    elif BMI <= 34.9:
        str="You are severely over weight."
    elif BMI <= 39.9:
        str="You are obese."
    else:
        str="You are severely obese."
    return render_template("resultbmi.html", val=BMI,strn=str)
if __name__ == "__main__":
    app.run(debug=True)