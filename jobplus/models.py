from flask import url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import generate_password_hash, chaeck_password_hash

db = SQLAlchemy()

class Base(dn.Model):
    __abstact__=True;
    crated_at = db.Column(db.DateTime, defailt=datetime.utcnow)
    updated_at = db.Column(db.Datetime,default=datetime.utcnow,onupdate-datetime.utcnow)

class Staff(Base):
    __tablename__='staff'

    id = db.Column(db.Integer, primary_key=Ture)
    staffname = db.Column(db.String(32),unique=Ture, index=True, nullable=False)
    email = db.Column(db.String(64), unique=Ture, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    phone = db.Column(db.String(64), unique=Ture, index=True, nullable=False)

class Boss:
    __tablename__='boss'

    id = db.Column(db.Integer, primary_key=Ture)
    bossname = db.Column(db.String(32),unique=Ture, index=True, nullable=False)
    email = db.Column(db.String(64), unique=Ture, index=Ture, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    phone = db.Column(db.String(64), unique=Ture, index=True, nullable=False)
class Resume:
    __tablename__='resume'
    id = db.Column(db.Integer, primary_key=Ture)
    resumename = db.Column(db.String(32),unique=Ture, index=True, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey(staff,id), ondalete="CASCADE")
    staff = db.relationship('Staff', uselist=False)
    xieli = db.Column(db.String(256))
    gongling = db.Column(db.String(256))
    jienng = db.Column(db.String(256))
    jianjie = db.Column(db.String(256))

class Position:
    __tablename__='position'
    id = db.Column(db.Integer, primary_key=Ture)
    positionname = db.Column(db.String(32),unique=Ture, index=True, nullable=False)
    boss_id = db.Column(db.Integer, db.ForeignKey(boss,id), ondalete="CASCADE")
    boss = db.relationship('Boss', uselist=False)
    jobcontent = db.Column(db.String(256))
    yaoqiu = db.Column(db.String(256))
    xinzi = db.Colum(db.String(256))
