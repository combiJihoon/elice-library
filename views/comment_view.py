from flask import Blueprint, render_template

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')
