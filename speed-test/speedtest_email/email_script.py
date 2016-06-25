import smtplib
import subprocess
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#This gets the speed test info, and saves it to a .txt file
def getInfo():
	with open("speedtest_results.txt", "w+") as output:
    		subprocess.call(["python", "./speedtest_cli.py"], stdout=output);


#This script sends an email
def sendEmail():
	fromaddr = "pythonscript4444@gmail.com"
	toaddr = "harveymark1994@gmail.com"
 
	msg = MIMEMultipart()
 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Speed Test Results"
 
	body = "Written by Harvey Mark"
 
	msg.attach(MIMEText(body, 'plain'))
 
	filename = "speedtest_results.txt"
	attachment = open("speedtest_results.txt", "rb")
 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
	msg.attach(part)
 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "gderfboy1")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()

getInfo()
sendEmail()
