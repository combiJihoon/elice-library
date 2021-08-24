from flask import Blueprint, request, render_template, url_for, flash, session, g, jsonify
from werkzeug.utils import redirect
from models import Book, Comment, User
from app import db

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/delete', methods=['POST'])
def delete():
    comment_id = request.form['comment_id']
    comment = Comment.query.filter_by(comment_id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "정상적으로 삭제 되었습니다."})
# @bp.route('/update/<int:comment_id>', methods=['GET'])
# def update_try(comment_id):

#     return render_template('book_detail.html')


# @bp.route('/update/<int:comment_id>', methods=['POST'])
# def update(comment_id):
#     content = request.form['content']
#     if not content:
#         flash('내용을 작성해 주세요.')
#         return redirect('comment.update_try', comment_id=comment_id)
#     comment = Comment.query.filter_by(comment_id=comment_id).first()
#     book_id = comment.book_id

#     comment.content = content

#     flash('정상적으로 삭제 되었습니다.')
#     return redirect(url_for('main.detail', book_id=book_id))
