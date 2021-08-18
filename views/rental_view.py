from flask import Blueprint, render_template, request, url_for, flash, session, g
from models import Book, Rental
from app import db
from werkzeug.utils import redirect

from datetime import datetime

bp = Blueprint('rental', __name__, url_prefix='/rental')


@bp.route('/record', methods=['GET'])
def record():
    if g.user is None:
        flash('로그인 후 대여기록을 볼 수 있습니다.')
        return redirect(url_for('main.home'))
    else:
        user_id = session['user_id']
        rental_list = Rental.query.filter_by(
            user_id=user_id).order_by(Rental.rented_at.desc()).all()
        return render_template('rental_record.html', rental_list=rental_list)


@bp.route('/<int:book_id>', methods=['POST'])
def rent(book_id):
    if g.user is None:
        flash('로그인 후 대여할 수 있습니다.')
        return redirect(url_for('main.home'))
    else:
        book = Book.query.filter_by(book_id=book_id).first()
        user_id = session['user_id']
        if book.stock > 0:
            has_already_rented = Rental.query.filter_by(
                user_id=user_id, book_id=book.book_id, rented_at=None).first()
            if has_already_rented:
                flash('이미 대여중인 책은 중복 대여가 불가능합니다.')
                return redirect(url_for('main.home'))
            else:
                book.stock -= 1
                rental = Rental(user_id=user_id,
                                book_id=book_id, returned_at=None)
                db.session.add(rental)
                db.session.commit()

                return redirect(url_for('rental.rented_data'))
        else:
            flash('현재 대여 가능한 책이 없습니다.')
            return redirect(url_for('main.home'))


@bp.route('/return', methods=['GET'])
def rented_data():
    if g.user is None:
        flash('로그인 후 반납할 수 있습니다.')
        return redirect(url_for('main.home'))
    else:
        user_id = session['user_id']
        rental_list = Rental.query.filter_by(
            user_id=user_id, rented_at=None).order_by(Rental.rented_at.desc()).all()

        return render_template('rented_list.html', rental_list=rental_list)


@bp.route('/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    user_id = session['user_id']

    rental_data = Rental.query.filter_by(
        book_id=book_id, user_id=user_id, returned_at=None).first()
    book_data = Book.query.filter_by(book_id=book_id).first()

    rental_data.returned_at = datetime.today()
    book_data.stock += 1

    db.session.commit()

    return redirect(url_for('rental.rented_data'))
