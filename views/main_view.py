from flask import Blueprint, render_template
from models import Book

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    book_list = Book.query.order_by(Book.book_id.asc()).all()
    return render_template('index.html', book_list=book_list)
