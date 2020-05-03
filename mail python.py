import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from twilio.rest import Client
# base64 helps use to encoding and decoding the data
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imwrite('C:\\Users\\HP\\Documents\\interfacing internet with python\\aks.jpg',frame)
cv2.waitKey(0) & 0xff

email_user = 'xxxxxx@gmail.com'
email_password = 'zxcvbnm12345678'
email_send ='xxxxxxx@gmail.com'

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='aks.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)



# Your Account SID from twilio.com/console
account_sid = "AC1a7db905b9f8be54e4780fadf2c1f372"
# Your Auth Token from twilio.com/console
auth_token  = "5eb7d7d05ed6192a480cf344fa1cabc4"
subject1="python"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="enter owners number", 
    from_="+14159854342",
    body="person out of the door is criminal, be alert")


server.sendmail(email_user,email_send,text)
cap.release()
server.quit()
