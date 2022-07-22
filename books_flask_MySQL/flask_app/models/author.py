from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book 
# author.books.append(book.Book(book_data))

class Author:

    def __init__(self,data):
        self.id = data["id"]
        self.name = data['name']
        self.books = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VAlUES(%(name)s) ;"
        return connectToMySQL("books_schema").query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_author_with_books(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)
        author = cls(results[0])
        for row in results:
            book_data = {
                "id": row["books.id"],
                "title": row['title'],
                'num_of_pages': row['num_of_pages']
            }
            author.books.append(book.Book(book_data))
        return author

    @classmethod
    def add_fav(cls,data):
        query = "INSERT INTO favorites (book_id, author_id) VALUES(%(book_id)s, %(author_id)s);"
        return connectToMySQL("books_schema").query_db(query,data)