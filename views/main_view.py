from flask import Blueprint, request, render_template, url_for, flash, session, g, jsonify
from werkzeug.utils import redirect
from models import Book, Comment
from forms import CommentForm
from app import db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    page = request.args.get('page', type=int, default=1)
    book_list = Book.query.order_by(Book.book_id.asc())
    book_list = book_list.paginate(page, per_page=8)
    return render_template('index.html', book_list=book_list)


@bp.route('/create-comment/<int:book_id>', methods=['POST'])
def create_comment(book_id):
    if g.user is None:
        flash('로그인 후 사용할 수 있습니다.')
        return redirect(url_for('main.detail', book_id=book_id))
    else:
        user_id = session['user_id']
        content = request.form['content']
        try:
            rating = request.form['rating']
        except:
            rating = 0

        if content is None:
            flash('내용을 입력해 주세요!')
            return redirect(url_for('main.detail', book_id=book_id))

        comment = Comment(user_id=user_id, book_id=book_id,
                          rating=rating, content=content)

        db.session.add(comment)
        db.session.commit()

        # rating update
        rows = Comment.query.filter_by(
            book_id=book_id).all()
        if len(rows) != 0:
            rating_sum = 0
            for row in rows:
                rating_sum += row.rating
            avg_rating = round(rating_sum / len(rows))
            book = Book.query.filter_by(book_id=book_id).first()
            book.rating = avg_rating
            db.session.commit()

        return redirect(url_for('main.detail', book_id=book_id))


@bp.route('/detail/<int:book_id>', methods=['GET'])
def detail(book_id):
    # data = request.get_json()
    # book_id = request.form['book_id']
    form = CommentForm()
    comment_list = Comment.query.filter_by(
        book_id=book_id).order_by(Comment.created_at.desc()).all()
    book = Book.query.filter_by(book_id=book_id).first()
    return render_template('book_detail.html', book=book, comment_list=comment_list, form=form)
