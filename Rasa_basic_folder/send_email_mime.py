import smtplib
import email
import os
from email.mime.text import MIMEText


smtp_host = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP()
server.connect(smtp_host,smtp_port)
server.ehlo()
server.starttls()
server.login('kurmakshetra@gmail.com','pho12kus')

string = """Found Asia Kitchen By Mainland China in 136, Ground Floor, 1st Cross, 5th Block, Jyoti Niwas College Road, Koramangala 5th Block, Bangalore Cost: 1500
Found High Ultra Lounge in 26/1 , 31st Floor, Dr. Rajkumar Road, World Trade Centre, Brigade Gateway Campus, Malleshwaram, Bangalore Cost: 2600
Found Yo! Chow in 90/3 Sri Sapthagiri Complex,Outer ring road marathahalli,Opp to innovative Multiplex, Marathahalli, Bangalore Cost: 800
Found Yauatcha in 1 MG Mall, MG Road, Bangalore Cost: 2800
Found Mainland China in 28/2, 1st Floor, Siddapura, Whitefield Main Road, Whitefield, Bangalore near Dmart Cost: 1700 """

msg = MIMEText(string)

msg['Subject'] = 'Your restraurant search results'
msg['From'] = 'restraurantbot@zomato.com'
msg['To'] = 'amirisetty.vijayaraghavan@gmail.com'

#msg.attach(MIMEText(raw_input('Body: ')))

server.sendmail('kurmakshetra@gmail.com','amirisetty.vijayaraghavan@gmail.com',msg.as_string())

server.quit()
