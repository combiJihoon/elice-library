from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


# 오류 페이지 정의
def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABSE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # blueprint
    from .views import main_view, auth_view, comment_view, rental_view
    app.register_blueprint(main_view, bp)
    app.register_blueprint(auth_view, bp)
    app.register_blueprint(comment_view, bp)
    app.register_blueprint(rental_view, bp)

    # 오류 페이지 등록
    app.register_error_handler(404, page_not_found)

    return app