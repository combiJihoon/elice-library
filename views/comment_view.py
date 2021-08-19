from flask import Blueprint, request, render_template, url_for, flash, session, g
from werkzeug.utils import redirect
from models import Book, Comment, User

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/<int:book_id>', methods=['GET', 'POST'])
def create_comment(book_id):
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
        comment_list = Comment.query.order_by(Comment.created_at.desc()).all()
        return render_template('book_detail.html', comment_list=comment_list)
