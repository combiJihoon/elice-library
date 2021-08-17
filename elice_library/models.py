# from sqlalchemy import Column, String, Text, Integer, DateTime
from elice_library import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.String(150), nullable=False,
                        primary_key=True, unique=True)
    user_password = db.Column(db.String(150), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)

    def __init__(self, user_id, user_password, user_name):
        self.user_id = user_id
        self.user_password = user_password
        self.user_name = user_name


class Book(db.Model):
    __tablename__ = 'book'

    book_id = db.Column(db.Integer, nullable=False,
                        primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publicated_at = db.Column(db.DateTime, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=True)
    link = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=True)
    stock = db.Column(db.Integer, nullable=False)


class Rental(db.Model):
    __tablename__ = 'rental'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'book.book_id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(150), db.ForeignKey(
        'user.user_id', ondelete='CASCADE'), nullable=False)
    rented_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    returned_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)

    book = db.relationship('Book', backref=db.backref('rental_set'))
    user = db.relationship('User', backref=db.backref('rental_set'))


class Comment(db.Model):
    __tablename__ = 'comment'

    comment_id = db.Column(db.Integer, nullable=False,
                           primary_key=True, autoincrement=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        'book.book_id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.String(150), db.ForeignKey(
        'user.user_id', ondelete='CASCADE'), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    modified_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)

    book = db.relationship('Book', backref=db.backref(
        'comment_set'))
    user = db.relationship('User', backref=db.backref(
        'comment_set'))

    def __init__(self, content, rating):
        self.content = content
        self.rating = rating
