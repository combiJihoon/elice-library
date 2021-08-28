from flask import Blueprint, request, render_template, url_for, flash, session, g, jsonify
from werkzeug.utils import redirect
from models import Book, Comment, User
from app import db
import pytz

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/delete', methods=['POST'])
def delete():
    comment_id = request.form['comment_id']
    comment = Comment.query.filter_by(comment_id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "success"})


# @bp.route('/update/<int:comment_id>', methods=['GET'])
# def update_try(comment_id):
#     # data = request.get_json()
#     # book_id = request.form['book_id']
#     to_be_updated = Comment.query.filter_by(comment_id=comment_id).first()
#     book_id = to_be_updated.book.book_id

#     comment_list = Comment.query.filter_by(
#         book_id=book_id).order_by(Comment.created_at.desc())
#     book = Book.query.filter_by(book_id=book_id).first()

#     created_times = []
#     for comment in comment_list:
#         created_time = comment.created_at
#         created_times.append(created_time.astimezone(
#             pytz.timezone("Asia/Seoul")))

#     comment_list = comment_list.all()

#     return render_template('books/book_detail.html', book=book, comment_list=comment_list, created_times=created_times, to_be_updated=to_be_updated)


# @bp.route('/update/<int:comment_id>', methods=['POST'])
# def update(comment_id):
#     content = request.form['content']

#     comment = Comment.query.filter_by(comment_id=comment_id).first()
#     book_id = comment.book.book_id

#     comment = Comment.query.filter_by(comment_id=comment_id).first()

#     comment.content = content
#     db.session.commit()

#     return redirect(url_for('main.detail', book_id=book_id))
