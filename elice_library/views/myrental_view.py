from flask import Blueprint, render_template

bp = Blueprint('myrental', __name__, url_prefix='/myrental')


@bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')
