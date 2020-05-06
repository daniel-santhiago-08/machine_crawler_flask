from app.auth import auth as auth_blueprint
from app.user import user as user_blueprint
from app.machines_crawler import machines_crawler as machines_crawler_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(machines_crawler_blueprint)







