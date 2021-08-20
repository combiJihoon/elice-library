from flask import Blueprint, request, render_template, url_for, flash, session, g
from werkzeug.utils import redirect
from models import Book, Comment, User
from forms import CommentForm
from app import db

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/delete', methods=['POST'])
def delete(comment_id):
    comment = Comment.query.filter_by(comment_id=comment_id).first()
    book_id = comment.book_id

    db.session.delete(comment)
    db.session.commit()

    flash('정상적으로 삭제 되었습니다.')
    return redirect(url_for('main.detail', book_id=book_id))
