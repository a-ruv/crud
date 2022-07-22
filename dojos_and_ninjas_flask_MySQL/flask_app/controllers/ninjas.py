from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#create
@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    id = Ninja.save(request.form)
    return redirect(f"/dojos/{id}")

#read
@app.route("/ninjas")
def ninja():
    dojos = Dojo.get_all()
    return render_template("ninja.html", dojos = dojos)