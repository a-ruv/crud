from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route("/")
def read():
    users = User.get_all()
    return render_template("read.html", users = users)

@app.route("/create")
def createpage():
    return render_template("create.html")

@app.route("/read_one/<int:id>")
def read_one(id):
    data = {'id': id}
    return render_template("read_one.html", user = User.get_one(data))

@app.route("/edit_page/<int:id>")
def edit_page(id):
    data = {'id': id}
    return render_template("edit.html", user = User.get_one(data))

@app.route("/delete/<int:id>")
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')

@app.route('/create_user', methods = ['POST'])
def create_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email'],
    }
    id = User.save(data)
    return redirect(f"/read_one/{id}")

@app.route('/edit/<int:id>', methods = ['POST'])
def edit_user(id):
    User.edit(request.form)
    return redirect(f"/read_one/{id}")
