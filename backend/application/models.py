from .database import db
from flask_security import UserMixin, RoleMixin
from flask_login import login_manager


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))    

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('Users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    Description = db.Column(db.String(255))


class List(db.Model):
    __tablename__ = "List"
    User_Id = db.Column(db.Integer,db.ForeignKey("user.id",ondelete="CASCADE"), nullable=False)
    List_Id  = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Name = db.Column(db.String)
    Description = db.Column(db.String)

class Card(db.Model):
    __tablename__ = 'Card'
    List_Id = db.Column(db.Integer,db.ForeignKey("List.List_Id",ondelete="CASCADE"), nullable=False)
    Card_Id = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Content = db.Column(db.String,nullable=False)
    Deadline = db.Column(db.String,nullable=False)
    Status = db.Column(db.String)
    Title = db.Column(db.String)


