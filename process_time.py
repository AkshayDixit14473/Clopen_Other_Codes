#rclone copy -P --transfers 1 ftpcm:90185 /home/akshay/Downloads/FTP_CM_FO_FILES/CM90185/
#rclone copy -P --transfers 1 ftpfo:FaoFtp/F90185 /home/akshay/Downloads/FTP_CM_FO_FILES/FO90185/
#rclone -v copy /home/akshay/Downloads/FTP_CM_FO_FILES/ spaces:cleanluffy/NSEFTP/   

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
subprocess.call(['sh', '/home/akshay/Cron_scripts/nse_ftp_rclone_script'])
et = time.time()
elapsed_time = et - st
#x=subprocess.check_call(['sh', './nse_ftp_rclone_script',check==True])
print("               ")
print(elapsed_time)
if elapsed_time<300:
 sendmail("emailprojectd@gmail.com","aashish@clopen-research.com","FTP TRANSFER STATUS","LOGIN ERROR ENCOUNTERED","qinrzvmhfusnwzyw")
 sendmail("emailprojectd@gmail.com","akshay.dixit@clopen-research.com","FTP TRANSFER STATUS","LOGIN ERROR ENCOUNTERED","qinrzvmhfusnwzyw")
else:
 sendmail("emailprojectd@gmail.com","akshay.dixit@clopen-research.com","FTP TRANSFER STATUS","FTP TRANSFER SUCCESSFUL","qinrzvmhfusnwzyw")
 sendmail("emailprojectd@gmail.com","aashish@clopen-research.com","FTP TRANSFER STATUS","FTP TRANSFER SUCCESSFUL","qinrzvmhfusnwzyw")
