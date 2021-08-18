from flask import Blueprint, render_template, url_for, flash, session, g
from models import Book, Rental
from app import db
from werkzeug.utils import redirect

bp = Blueprint('rental', __name__, url_prefix='/rental')


@bp.route('/record', methods=['GET'])
def record():
    if session['user_id'] is None:
        flash('로그인 후 대여기록을 볼 수 있습니다.')
        return redirect(url_for('main.home'))
    else:
        return render_template('record.html')


@bp.route('/<int:book_id>', methods=['GET', 'POST'])
def rent(book_id):
    if g.user is None:
        flash('로그인 후 대여할 수 있습니다.')
        return redirect(url_for('main.home'))
    else:
        book = Book.query.filter_by(book_id=book_id).first()
        user_id = session['user_id']
        if book.stock > 0:
            book.stock -= 1
            rental = Rental(user_id=user_id, book_id=book_id, returned_at=None)
            db.session.add(rental)
            db.session.commit()
            return render_template('rental_record.html')
        else:
            flash('현재 대여 가능한 책이 없습니다.')
            return redirect(url_for('main.home'))
