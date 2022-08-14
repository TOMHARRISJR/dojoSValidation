from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.survey import Survey


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create/survey", methods=["POST"]) # action route
def form():
    if Survey.is_valid(request.form):
        Survey.save(request.form)
        session["name"] = request.form["name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        return redirect("/result")
    return redirect('/')


@app.route("/result")
def result():
    survey = Survey.get_last_survey()
    return render_template("index1.html", survey = survey)

