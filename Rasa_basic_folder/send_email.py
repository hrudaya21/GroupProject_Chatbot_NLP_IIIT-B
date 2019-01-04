# Import smtplib for the actual sending function
import smtplib

import traceback
# Import the email modules we'll need
from email.message import EmailMessage

gmail_user = 'kurmakshetra@gmail.com'  
gmail_password = 'pho12kus'

sent_from = gmail_user  
to = ['amirisetty.vijayaraghavan@gmail.com']  
subject = 'Your Restraurant Search Results'  
body = 'Govindas Restraurant'

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:  
    print('Something went wrong...')
    traceback.print_exc()
