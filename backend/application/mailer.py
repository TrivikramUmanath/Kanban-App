import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
from email.mime.base import MIMEBase
from email import encoders
import weasyprint
from weasyprint import HTML
import uuid

SMTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT=1025
SENDER_ADDRESS="vikram.umanath@gmail.com"
SENDER_PASSWORD=""

def send_email(to_address,subject,message,content="text",attachment_file=None):
    msg=MIMEMultipart()
    msg["From"]=SENDER_ADDRESS
    msg["To"]=to_address
    msg["Subject"]=subject
    if content=="html":
        msg.attach(MIMEText(message,"html"))
    else:
        msg.attach(MIMEText(message,"plain"))
    if attachment_file:
        with open(attachment_file,"rb") as attachment:
            part=MIMEBase("application","ocean-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition",f"attahcment; filename={attachment_file}",)
        msg.attach(part)
    s=smtplib.SMTP(host=SMTP_SERVER_HOST  ,port=SMPTP_SERVER_PORT)
    s.login(SENDER_ADDRESS,SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()
    return True

def format_report(template_file,data={}):
    with open(template_file) as file:
        template = Template(file.read())
        return template.render(data=data)

def create_pdf_report(data):
    print("Outside")
    message=format_report("/home/trivikram/Desktop/MAD2_Final_Project/backend/templates/report_template.html",data=data[0])
    html=HTML(string=message)
    file_name=str("/home/trivikram/Desktop/MAD2_Final_Project/backend/templates/"+data[0]["name"])+".pdf"
    print(file_name)
    html.write_pdf(target=file_name)
    return file_name



def send__montly_message(data,fi):
    send_email(data[0]["email"],subject="Montly Report",message="Good Morning ! \n Please find the Montly Report attached herwrith.",content="html",attachment_file=fi)

def send_daily_reminder(data,email):
    send_email(email,subject="Daily Reminders",message=data,content="html")


