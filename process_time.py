import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

def sendmail(sender_address,receiver_address,subject,mail,sender_pass):
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = subject
	message.attach(MIMEText(mail, 'plain'))
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')

#try:
st = time.time()
subprocess.call(['sh', '<path to the bash script doing the work'])
et = time.time()
elapsed_time = et - st
#x=subprocess.check_call(['sh', './nse_ftp_rclone_script',check==True])
print("               ")
print(elapsed_time)
if elapsed_time<300:
 sendmail("<sender id>","<reciever id>","FTP TRANSFER STATUS","LOGIN ERROR ENCOUNTERED","<sneder pass>")
 sendmail("<sneder id>","<reciever id>","FTP TRANSFER STATUS","LOGIN ERROR ENCOUNTERED","<senser pass>")
else:
 sendmail("<sneder id>","<reciever id>","FTP TRANSFER STATUS","FTP TRANSFER SUCCESSFUL","<senser pass>")
 sendmail("<sneder id>","<reciever id>","FTP TRANSFER STATUS","FTP TRANSFER SUCCESSFUL","<senser pass>")
