from flask import Blueprint, render_template
from models import Book

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    book_list = Book.query.order_by(Book.book_id.asc()).all()
    return render_template('index.html', book_list=book_list)


@bp.route('/detail/<int:book_id>', methods=['GET'])
def book_detail(book_id):
    book = Book.query.filter_by(book_id=book_id).first()
    return render_template('index.html', book=book)
