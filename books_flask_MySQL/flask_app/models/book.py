from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author 
# book.authors.append(author.Author(author_data))

class Book:

    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.authors = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VAlUES(%(title)s, %(num_of_pages)s) ;"
        return connectToMySQL("books_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def get_book_with_authors(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        book = cls(results[0])
        for row in results:
            author_data = {
                "id": row["authors.id"],
                "name": row['name'],
            }
            book.authors.append(author.Author(author_data))
        return book

    @classmethod
    def add_fav(cls,data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES(%(book_id)s, %(author_id)s);"
        return connectToMySQL("books_schema").query_db(query,data)