from flask import Blueprint, render_template, url_for, flash
from modelse import Book
from werkzeug.utils import redirect

bp = Blueprint('rental', __name__, url_prefix='/rental')


@bp.route('/<int:book_id>', methods=['GET', 'POST'])
def rent(book_id):
    book = Book.query.filter_by(book_id=book_id).first()
    if book.stock > 0:
        book.stock -= 1
        db.session.commit()
        return render_template('rental_record.html')
    else:
        flash('현재 대여 가능한 책이 없습니다.')
        return redirect(url_for('main.home'))
