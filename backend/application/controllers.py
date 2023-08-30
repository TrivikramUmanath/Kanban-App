from asyncio.log import logger
from email.mime import message
from flask import Flask, redirect, request
from flask import render_template
from flask import current_app as app
from application.models import User,Card,List
from .database import db
import datetime
import matplotlib.pyplot as plt
from pytz import timezone
import flask
import numpy as np
import json
import pandas as pd

@app.route("/Dashboard/<string:id>/ExportUser",methods=["GET"])
def export_user(id):
    print("START")
    Complete_Data=[]
    intId = int(id)
    user_data=db.session.query(User).filter(User.id==intId).first()
    list_data=db.session.query(List).filter(List.User_Id==intId).all()
    for j in list_data:
        we=j.List_Id
        Cards_data = db.session.query(Card).filter(Card.List_Id==int(we)).all()
        for i in Cards_data:
                dar={}
                dar["User_id"]=user_data.id
                dar["email"]=user_data.email
                dar["password"]=user_data.password
                # dar["Customer Name"]=user_data["email".split("@")[0]
                dar["Card_Id"]=i.Card_Id
                dar["Title"]=i.Title
                dar["Deadline"]=i.Deadline
                dar["Status"]=i.Status
                dar["Content"]=i.Content
                dar["List_id"]=j.List_Id
                dar["List_Name"]=j.Name
                dar["Description"]=j.Description
                print(dar)
                Complete_Data.append(dar)
    print("Complete Data")
    w=json.dumps(Complete_Data)
    return "Job Started",200


@app.route("/Dashboard/<string:id>/ExportList",methods=["GET"])
def export_list(id):
    print("START")
    Complete_Data=[]
    intId = int(id)
    list_data=db.session.query(List).filter(List.List_Id==intId).first()
    print(Complete_Data)
    Cards_data = db.session.query(Card).filter(Card.List_Id==int(intId)).all()
    for i in Cards_data:
            dar={}
            dar["Card_Id"]=i.Card_Id
            dar["Title"]=i.Title
            dar["Deadline"]=i.Deadline
            dar["Status"]=i.Status
            dar["Content"]=i.Content
            dar["List_id"]=list_data.List_Id
            dar["List_Name"]=list_data.Name
            dar["Description"]=list_data.Description
            print(dar)
            Complete_Data.append(dar)
    print("Complete Data")
    w=json.dumps(Complete_Data)

    return "Job Started",200


@app.route("/Dashboard/<string:id>/ExportCard",methods=["GET"])
def export_card(id):
    print("START")
    Complete_Data=[]
    intId = int(id)
    i = db.session.query(Card).filter(Card.Card_Id==int(intId)).first()
    
    dar={}
    dar["Card_Id"]=i.Card_Id
    dar["Title"]=i.Title
    dar["Deadline"]=i.Deadline
    dar["Status"]=i.Status
    dar["Content"]=i.Content
    print(dar)
    print("Complete Data")
    Complete_Data.append(dar)
    w=json.dumps(Complete_Data)
    print(w)
    return "Job Started",200