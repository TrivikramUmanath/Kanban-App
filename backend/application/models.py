from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

engine = None
Base = declarative_base()
db = SQLAlchemy()





class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Name = db.Column(db.String, unique=False)
    email = db.Column(db.String, unique=False)
    password = db.Column(db.String)
    Category=db.Column(db.String)


class Thread(db.Model):
    __tablename__ = "Thread"
    user_id = db.Column(db.Integer,db.ForeignKey("user.user_id",ondelete="CASCADE"), nullable=False)
    thread_id  = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Title = db.Column(db.String)
    Thread_Map = db.Column(db.String)
    Thread_count = db.Column(db.Integer)

class Post(db.Model):
    __tablename__ = 'Post'
    thread_id = db.Column(db.Integer,db.ForeignKey("Thread.thread_id",ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Post_Message = db.Column(db.String(255))
    Annoynmous = db.Column(db.String())
    Post_Date_Time = db.Column(db.String())
    Poster_email=db.Column(db.String())
    Poster_Name=db.Column(db.String())

class Assesment(db.Model):
    __tablename__ = "Assesment"
    creator_id = db.Column(db.Integer,db.ForeignKey("user.user_id",ondelete="CASCADE"), nullable=False)
    assesment_id  = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Name = db.Column(db.String)
    Quiz = db.Column(db.String)
    Student_Count = db.Column(db.Integer)
    Toppers=db.Column(db.String)

class Aspirant(db.Model):
    __tablename__ = "Aspirant"
    aspirant_id = db.Column(db.Integer, db.ForeignKey("user.user_id",ondelete="CASCADE"),primary_key=True, nullable=False)
    assesment_id  = db.Column(db.Integer, db.ForeignKey("Assesment.assesment_id",ondelete="CASCADE"),primary_key=True, nullable=False)
    aspirant_score=db.Column(db.Integer)
    aspirant_name = db.Column(db.String)
     

class Connection(db.Model):
    __tablename__ = "Connection"
    sender_id = db.Column(db.Integer,db.ForeignKey("user.user_id",ondelete="CASCADE"), nullable=False)
    receiver_id=db.Column(db.Integer,db.ForeignKey("user.user_id",ondelete="CASCADE"), nullable=False)
    connection_id  = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Approval_Status = db.Column(db.String)
    Connection_Map = db.Column(db.String)
    Sender_Name = db.Column(db.String)
    Receiver_Name = db.Column(db.String)
    Request=db.Column(db.String)

class Message(db.Model):
    __tablename__ = 'Message'
    connection_id = db.Column(db.Integer,db.ForeignKey("Connection.connection_id",ondelete="CASCADE"), nullable=False)
    message_id = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    Content = db.Column(db.String)
    Message_Sender = db.Column(db.String)
    Message_Date_Time = db.Column(db.String)

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


