import requests
import json
import pandas as pd
import datetime
from datetime import datetime
from datetime import date, timedelta
import pprint
import os
import sys
import time
import glob
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import tarfile
import time
import shutil
from pathlib import Path
import sys
import dateutil
from dateutil.parser import parse
import gzip
import shutil

datelist=[]
#date=input("Enter yesterday's date to compare positions\n")
now = datetime.today()
yesterday = now - timedelta(days = 1)
date = yesterday.strftime("%d%m%Y")
#print(sys.argv[1])
print("Zipping up")

with gzip.open('/tmp/optPositionsConcillation.csv.gz', 'rb') as f_in:                                      #UNZIPPING ZIPPED FILE
    with open('/tmp/optPositionsConcillation.CSV', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

with gzip.open("/home/akshay/Downloads/From_api_ftp/Automatic/"+date+"_FO/F_PS03_90185_"+date+".CSV.gz", 'rb') as f_in:        #UNZIPPING ZIPPED FILE
    with open("/home/akshay/Downloads/From_api_ftp/Automatic/"+date+"_FO/F_PS03_90185_"+date+".CSV", 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

print("gzip done")

print("OP POSITIONS FILE-----------------------------\n")                        #Using the columns of our file
df1 = pd.read_csv("/tmp/optPositionsConcillation.CSV",header=None)
print(df1)
 
column_net_positions = df1.iloc[:, 6]
#print(column_net_positions)
column_strike_price = df1.iloc[:, 4]
#print(column_strike_price)
column_expiry_date = df1.iloc[:, 3]
#print(column_expiry_date)
column_type=df1.iloc[:, 5]
column_indices=df1.iloc[:, 1]
#print(column_indices)

print("PS03 FILE-------------------------------\n")                              #Using the columns of nse file
#print(sys.argv[2])
df2 = pd.read_csv("/home/akshay/Downloads/From_api_ftp/Automatic/"+date+"_FO/F_PS03_90185_"+date+".CSV",header=None)
print(df2)

nse_column28 = df2.iloc[:,28]
nse_column30 = df2.iloc[:,30]
nse_strike_price = df2.iloc[:,11]
nse_expiry_date = df2.iloc[:,10]
nse_type = df2.iloc[:,12]
nse_indices = df2.iloc[:,9]
#print(nse_indices)
i=0
j=3
print("########################### COMPARISION POSITIONS START ################################\n")

for idx0,k in enumerate(column_strike_price):
 print("************NOW IN OP POSITIONS FILE ROW NO "+str(idx0)+"*****************")
 l=0                                                                               #for calculating if any unequal element occurs
 j=0
 for idx1, x in enumerate(nse_strike_price):
  if k==x:
   j=j+1                                                                           #for calculating times strike price repeats in file with different attributes
   dt1 = parse(column_expiry_date[idx0])
   dt2 = parse(nse_expiry_date[idx1])
   print("strike price same")
   print(str(j)+" time")
   if dt1==dt2:
    print("Expiry date same")
    if column_type[idx0][4:6]==nse_type[idx1]:
     print("Option Type same")
     if column_indices[idx0] == nse_indices[idx1]:
      print("Market Index same")
      print("MATCH FOUND FOR STRIKE PRICE ----------> "+str(x))
      l=1
      print("TOTAL PS03 FILE ROW NO "+str(idx1))
      lhs=column_net_positions[idx0]
      rhs=nse_column28[idx1]-nse_column30[idx1]
      print(lhs)
      print(rhs) 
      if lhs==rhs:
       print("Equal")
       break
      else:
       print("Unequal")
       i=1
       break

print("#################### END ################################\n")

if i==0:
 print("Quantity is equal")
else:
 print("Quantity is unequal")
