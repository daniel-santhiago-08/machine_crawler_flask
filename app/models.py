from app import db, login_manager
from flask_login import UserMixin
from sqlalchemy import BigInteger, Column, Date, Float, \
    Text, DateTime, Integer, \
    MetaData, Numeric, String, Table, Unicode

metadata = MetaData()



@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)

    def __str__(self):
        return self.name

class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    def __str__(self):
        return self.name


t_machine_print = Table(
    'machine_print', metadata,
    Column('id', BigInteger),
    Column('produto', Text),
    Column('data', Date),
    Column('loja', Text),
    Column('url', Text)
)



t_price_crawler_evolution = Table(
    'price_crawler_evolution', metadata,
    Column('id', BigInteger),
    Column('data_extracao', Date),
    Column('mini_me', Float(53)),
    Column('essenza', Float(53)),
    Column('inissia', Float(53)),
    Column('mimo_cafeteira', Float(53)),
    Column('pop_plus', Float(53)),

)


t_price_crawler_hist = Table(
    'price_crawler_hist', metadata,
    Column('id', BigInteger),
    Column('produto', Text),
    Column('data_extracao', Date),
    Column('loja', Text),
    Column('preco', Float(53))
)


t_price_crawler_hist_temp = Table(
    'price_crawler_hist_temp', metadata,
    Column('product_name', Text),
    Column('data_extracao', Text),
    Column('loja', Text),
    Column('price_num', Text),
    Column('url', Text)
)


t_price_crawler_min = Table(
    'price_crawler_min', metadata,
    Column('id', BigInteger),
    Column('produto', Text),
    Column('data_extracao', Date),
    Column('loja', Text),
    Column('preco', Float(53))
)



t_hist_rfv_total_segments = Table(
    'hist_rfv_total_segments', metadata,
    Column('Semana', String(25, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Segment', String(11, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False),
    Column('Clientes_Semana_Atual', Integer),
    Column('Clientes_Semana_Anterior', Integer),
    # info={'bind_key': 'db_nlab'}
)
# class RfvSegments(db.Model):
#     __table_name__ = 'hist_rfv_total_segments'
#     __bind_key__ = 'db_nlab'
#     id = db.Column(db.Integer, primary_key=True)
#     Semana = db.Column(db.String(84))
#     Segment = db.Column(db.String(84))
#     Clientes_Semana_Atual = db.Column(db.Integer)
#     Clientes_Semana_Anterior = db.Column(db.Integer)
#     # id = db.Column(db.Integer, primary_key=True)
#     # username = db.Column(db.String(80), unique=True)