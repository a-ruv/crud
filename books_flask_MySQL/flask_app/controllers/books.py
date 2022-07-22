from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author

#create
@app.route("/books/create", methods = ['POST'])
def create_book():
    Book.save(request.form)
    return redirect("/books")

@app.route("/books/<int:id>/fav", methods = ['POST'])
def create_book_fav(id):
    data = {
        "book_id": id ,
        "author_id": request.form["author_id"]
    }
    Book.add_fav(data)
    return redirect (f"/books/{id}")

#read
@app.route("/books")
def books():
    books = Book.get_all()
    return render_template("books.html", books = books)

@app.route("/books/<int:id>")
def show_book(id):
    data = {"id": id}
    authors= Author.get_all()
    book = Book.get_book_with_authors(data)
    return render_template("show_book.html", book = book, authors = authors)


# create the function to add favorites 
