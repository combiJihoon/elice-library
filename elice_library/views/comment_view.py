from flask import Blueprint, request, render_template, url_for, flash, session, g, jsonify
from werkzeug.utils import redirect
from elice_library.models import Book, Comment, User
from elice_library import db

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/delete', methods=['POST'])
def delete():
    comment_id = request.form['comment_id']
    comment = Comment.query.filter_by(comment_id=comment_id).first()

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": "정상적으로 삭제 되었습니다."})


# @bp.route('/update', methods=['POST'])
# def update():
#     comment_id = request.form['comment_id']
#     content = request.form['content']

#     comment = Comment.query.filter_by(comment_id=comment_id).first()

#     comment.content = content

#     db.session.commit()

#     return jsonify({"message": "정상적으로 수정 되었습니다."})


# @bp.route('/update', methods=['GET'])
# def update_try():
#     comment_id = request.form['comment_id']
#     content = request.form['content']

#     comment = Comment.query.filter_by(comment_id=comment_id).first()

#     comment.content = content

#     db.session.commit()

#     return jsonify({"message": "정상적으로 수정 되었습니다."})
