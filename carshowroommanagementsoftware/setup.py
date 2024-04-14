import os
os.system('pip install pwinput')
os.system('pip install mysql.connector')
os.system('pip install pandas')
os.system('pip install wexpect')

import wexpect
import sys

ch = wexpect.spawn('mysql -u root -p')
ch.logfile = sys.stdout.buffer
ch.expect('Enter password')
ch.sendline('')
ch.expect('mysql>')
ch.sendline('create database car_showroom;')
ch.expect('mysql>')
ch.sendline('use car_showroom;')
ch.expect('mysql>')
ch.sendline(r' source d:\Users\LENOVO\Desktop\ip_project\backup.sql ;')
ch.expect('mysql>')
ch.sendline('quit;')