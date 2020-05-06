# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, Float, Integer, String, Table, Text, text
from sqlalchemy.dialects.postgresql import OID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_machine_print = Table(
    'machine_print', metadata,
    Column('id', BigInteger),
    Column('produto', Text),
    Column('data', Date),
    Column('loja', Text),
    Column('url', Text)
)


t_pg_stat_statements = Table(
    'pg_stat_statements', metadata,
    Column('userid', OID),
    Column('dbid', OID),
    Column('queryid', BigInteger),
    Column('query', Text),
    Column('calls', BigInteger),
    Column('total_time', Float(53)),
    Column('min_time', Float(53)),
    Column('max_time', Float(53)),
    Column('mean_time', Float(53)),
    Column('stddev_time', Float(53)),
    Column('rows', BigInteger),
    Column('shared_blks_hit', BigInteger),
    Column('shared_blks_read', BigInteger),
    Column('shared_blks_dirtied', BigInteger),
    Column('shared_blks_written', BigInteger),
    Column('local_blks_hit', BigInteger),
    Column('local_blks_read', BigInteger),
    Column('local_blks_dirtied', BigInteger),
    Column('local_blks_written', BigInteger),
    Column('temp_blks_read', BigInteger),
    Column('temp_blks_written', BigInteger),
    Column('blk_read_time', Float(53)),
    Column('blk_write_time', Float(53))
)


t_price_crawler_evolution = Table(
    'price_crawler_evolution', metadata,
    Column('id', BigInteger),
    Column('data_extracao', Date),
    Column('mini_me', Float(53)),
    Column('essenza', Float(53)),
    Column('inissia', Float(53)),
    Column('mimo_cafeteira', Float(53)),
    Column('pop_plus', Float(53))
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
    Column('price_num', Float(53)),
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


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, server_default=text("nextval('profiles_id_seq'::regclass)"))
    photo = Column(String(124), nullable=False)
    user_id = Column(Integer)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    name = Column(String(84), nullable=False)
    email = Column(String(84), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
