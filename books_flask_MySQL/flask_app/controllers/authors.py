from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book


#create
@app.route("/authors/create", methods =['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/')

@app.route("/authors/<int:id>/fav", methods = ['POST'])
def create_author_fav(id):
    data = {
        "book_id": request.form['book_id'],
        "author_id": id
    }
    Author.add_fav(data)
    return redirect (f"/authors/{id}")

#read
@app.route("/")
def index():
    return redirect("/authors")

@app.route('/authors')
def auhtors():
    authors= Author.get_all()
    return render_template("authors.html", authors = authors)

@app.route('/authors/<int:id>')
def show_author(id):
    data = {'id': id}
    books = Book.get_all()
    author = Author.get_author_with_books(data)
    return render_template("show_author.html", author = author, books = books)

# still need to create an add favorite 