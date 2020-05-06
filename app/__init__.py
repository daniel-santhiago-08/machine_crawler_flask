from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from filtros import format_date

from flask import Flask
from flask_mail import Mail, Message
import urllib

# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
# params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=SPLADB30;DATABASE=DB_NLAB;Trusted_Connection=yes;')


# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

# from sqlalchemy import create_engine
# engine = create_engine("mssql+pyodbc://SPLADB30/DB_NLAB?driver=SQL+Server?trusted_connection=yes")
# engine.connect()

SERVER='motty.db.elephantsql.com'
DATABASE='vdqwlrpc'
PORT='5432'
USERNAME='vdqwlrpc'
PASS='Pz3hNp6zHyu6L8bHrGbT9yqpzGh-TKK1'

def create_app():
    app = Flask(__name__,
                template_folder='templates',
                static_folder='static'
                )
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+USERNAME+':'+PASS+'@'+SERVER+':'+PORT+'/'+DATABASE

    # app.config['SQLALCHEMY_BINDS']  = {
    #     'machines_old': 'sqlite:///pythonsqlite.db',
    #     # 'db_nlab': 'mssql+pyodbc:///?odbc_connect=%s' % params
    #     'db_nlab':  "mssql+pyodbc://SPLADB30/DB_NLAB?driver=SQL+Server?trusted_connection=yes"
    # }
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "Chave_Secreta"
    # app.jinja_env.filters['formatdate'] = format_date


    config = {
        "MAIL_SERVER": "smtp.ethereal.email",
        "MAIL_PORT": 587,
        "MAIL_USE_TLS": True,
        "MAIL_DEBUG": True,
        "MAIL_USERNAME": "randall.hudson@ethereal.email",
        "MAIL_PASSWORD": "Z2YAXZZwuxY2mp8BSx",
        "MAIL_DEFAULT_SENDER": "Daniel <danielsanth@hotmail.com>"
    }

    app.config.update(config)

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    from app import routes
    routes.init_app(app)



    return app


