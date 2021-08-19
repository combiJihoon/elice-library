from flask import Blueprint, request, render_template, url_for, flash, session, g
from werkzeug.utils import redirect
from models import Book, Comment
from app import db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    book_list = Book.query.order_by(Book.book_id.asc()).all()
    return render_template('index.html', book_list=book_list)


@bp.route('/detail/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    if request.method == 'POST':
        if g.user is None:
            flash('로그인 후 사용할 수 있습니다.')
        else:
            user_id = session['user_id']
            rating = request.form['rating']
            content = request.form['content']
            comment = Comment(user_id=user_id, book_id=book_id,
                              rating=rating, content=content)
            db.session.add(comment)
            db.session.commit()
        return redirect(url_for('main.book_detail', book_id=book_id))

    else:
        comment_list = Comment.query.filter_by(
            book_id=book_id).order_by(Comment.created_at.desc()).all()
        book = Book.query.filter_by(book_id=book_id).first()
        return render_template('book_detail.html', book=book, comment_list=comment_list)
