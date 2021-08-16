# from sqlalchemy import Column, String, Text, Integer, DateTime
from elice_library import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.String(150), Nullable=False, primary_key=True)
    user_password = db.Column(db.String(150), Nullable=False)
    user_name = db.Column(db.String(100), Nullable=False)
    children = db.relationship()

    def __init__(self, user_id, user_password, user_name):
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, Nullable=False,
                        primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), Nullable=False)
    author = db.Column(db.String(100), Nullable=False)
    publication_date = db.Column(db.DateTime, Nullable=False)
    pages = db.Column(db.Integer, Nullable=False)
    isbn = db.Column(db.Integer, Nullable=False)
    description = db.Column(db.Text())
    link = db.Column(db.String(255))
    img_url = db.Column(db.String(255))
    stock = db.Column(db.Integer, Nullable=False)


class Rental(db.Model):
    __tablename__ = 'rental'

    book_id = db.Column(db.Integer, db.Foreign_key(
        'book.book_id', on_delete='CASCADE'), Nullable=False)
    user_id = db.Column(db.String(150), db.Foreign_key(
        'user.user_id', on_delete='CASCADE'), Nullable=False)
    rented_at = db.Column(db.DateTime, Nullable=False)
    returned_at = db.Column(db.DateTime, Nullable=False)

    book = db.relationship('Book', backref=db.backref('rental'))
    user = db.relationship('User', backref=db.backref('rental'))


class Comment(db.Model):
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, Nullable=False,
                           primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.Foreign_key(
        'book.book_id', on_delete='CASCADE'), Nullable=False)
    user_id = db.Column(db.String(150), db.Foreign_key(
        'user.user_id', on_delete='CASCADE'), Nullable=False)
    content = db.Column(db.Text(), Nullable=False)
    rating = db.Column(db.Integer, Nullable=False)
    created_at = db.Column(db.DateTime, Nullable=False)
    modified_at = db.Column(db.DateTime, Nullable=False)

    book = db.relationship('Book', backref=db.backref('comment'))
    user = db.relationship('User', backref=db.backref('comment'))

    def __init__(self, content, rating):
        self.content = content
        self.rating = rating
