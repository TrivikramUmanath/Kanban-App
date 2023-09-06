from celery.schedules import crontab
from datetime import datetime
import pandas as pd
from application.workers import celery
import json
from application.models import User,Card,List
import requests
import datetime
from .database import db
from application.mailer import create_pdf_report,send__montly_message,send_daily_reminder

h=datetime.datetime.now(datetime.timezone.utc).hour
m=datetime.datetime.now(datetime.timezone.utc).minute

print(h)
print(m)

# if (((m+1)/60)==1):
#     h=h+1
# m=(m+1)%60
id=21

h="15"
m="37"

print("HOUR IS "+str(h))
print("Minute is "+str(m))
print("crontab ", crontab)


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(10.0, print_current_time_job.s(), name='add every 10')
    sender.add_periodic_task(
        crontab(hour=str(h),minute=str(m)),daily_reminder_by_webhooks.s(), name="Daily Reminder by webhooks"
    )
    sender.add_periodic_task(
        crontab(day_of_month="15",hour=str(h),minute=str(m)),daily_reminder_by_email.s(), name="Daily Reminder by email"
    )
    sender.add_periodic_task(
        crontab(day_of_month="15",hour=str(h),minute=str(m)),mail_montly_report_pdf.s(), name="Mail Montly Report"
    )


@celery.task()
def mail_montly_report_pdf():
    print("INSIDE")
    report_data=[]
    intId = int(id)
    user_data=db.session.query(User).filter(User.id==intId).first()
    em=str(user_data.email)
    first_name=em.split("@")[0]
    report_data.append({"name":first_name,"email":em,"stuff":[]})
    list_data=list(db.session.query(List).filter(List.User_Id==intId).all())
    new_users = [{"name":"Trivikram","email":"Trivikram.Umanath@gmail.com","stuff":[{"list_name":"First list","description":"Help me Krishna"
    ,"card":[{"Title":"First Card","Content":"First content","Status":"Completed","Deadline":"today"}]}]}]
    t=0
    for j in list_data:
        we=j.List_Id
        report_data[0]["stuff"].append({"list_name":j.Name,"description":j.Description,"card":[]})
        Cards_data = db.session.query(Card).filter(Card.List_Id==int(we)).all()
        for i in Cards_data:
            report_data[0]["stuff"][t]["card"].append({"Title":i.Title,"Content":i.Content,"Deadline":i.Deadline,"Status":i.Status})
        t=t+1
    print(report_data)
    fi=create_pdf_report(report_data)
    send__montly_message(report_data,fi)


@celery.task()
def daily_reminder_by_webhooks():
    print("START")
    Pending_Cards=[]
    intId = int(id)
    user_data=db.session.query(User).filter(User.id==intId).first()
    list_data=db.session.query(List).filter(List.User_Id==intId).all()
    for j in list_data:
        we=j.List_Id
        Cards_data = db.session.query(Card).filter(Card.List_Id==int(we)).all()
        for i in Cards_data:
            if i.Status == "Incomplete":
                Pending_Cards.append(i.Title)
       
    print("Pending Tasks")
    print(Pending_Cards)
    pending_tasks = "Please  Update your Pending taks:"+ ",".join(Pending_Cards)
    print(pending_tasks)
    w=json.dumps({"text":pending_tasks})
    output=requests.post('''https://chat.googleapis.com/v1/spaces/AAAAahckBrw/messages?key=AIzaSyDdI0hCZtE6vySjMm-
    WEfRq3CPzqKqqsHI&token=sbePrXG2MGgDsmyf0VfjiaXtuepdmhtIxhSxRxfgMCM%3D''',data=w)
    return output.json()

@celery.task()
def daily_reminder_by_email():
    print("START")
    Pending_Cards=[]
    intId = int(id)
    user_data=db.session.query(User).filter(User.id==intId).first()
    email=user_data.email
    list_data=db.session.query(List).filter(List.User_Id==intId).all()
    for j in list_data:
        we=j.List_Id
        Cards_data = db.session.query(Card).filter(Card.List_Id==int(we)).all()
        for i in Cards_data:
            if i.Status == "Incomplete":
                Pending_Cards.append(i.Title)
    print("Pending Tasks")
    print(Pending_Cards)
    pending_tasks = "Please  Update your Pending tasks listed below:\n"+ "\n".join(Pending_Cards)
    print(pending_tasks)
    send_daily_reminder(pending_tasks,email)



@celery.task()
def print_current_time_job():
    print("START")
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string) 
    print("COMPLETE")
    return "Hello"

@celery.task()
def export_user_data(r):
    print("IN USER CELERY")
    print("R")
    print(r)
    print("type of r")
    print(type(r))
    # w=json.load(r)
    print("DICTQ")
    dictq= json.loads(r)
    df = pd.DataFrame(dictq)
    print("DATAFRAME")
    print(df)
    df.to_csv("/home/trivikram/Desktop/MAD2_Final_Project/USER_JOB_SCHEDULERS.CSV")
    print("kicko")



@celery.task()
def export_list_data(r):
    print("IN LIST CELERY")
    print("R")
    print(r)
    print("type of r")
    print(type(r))
    # w=json.load(r)
    print("DICTQ")
    dictq= json.loads(r)
    df = pd.DataFrame(dictq)
    print("DATAFRAME")
    print(df)
    df.to_csv("/home/trivikram/Desktop/MAD2_Final_Project/LIST_JOB_SCHEDULERS.CSV")

@celery.task()
def export_card_data(r):
    print("IN CARD CELERY")
    print("R")
    print(r)
    print("type of r")
    print(type(r))
    # w=json.load(r)
    print("DICTQ")
    dictq= json.loads(r)
    df = pd.DataFrame(dictq)
    print("DATAFRAME")
    print(df)
    df.to_csv("/home/trivikram/Desktop/MAD2_Final_Project/CARD_JOB_SCHEDULERS.CSV")

    
