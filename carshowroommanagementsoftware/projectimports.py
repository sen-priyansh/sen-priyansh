import pandas as pd
import mysql.connector as ql
import datetime



con = ql.connect(host= 'localhost', user ='root', passwd='',database='car_showroom')
cur=con.cursor()

def runcmd(cmd):
    cur.execute(cmd,multi=True)
    con.commit()

def addemp(jobcode,admin):
    name=input('Enter your name:')
    while True:
       
       try:
        ddob=int(input('enter day of birth:'))
        mdob=int(input('enter month of birth:'))
        ydob=int(input('enter year of birth:'))
        s=datetime.date(ydob,mdob,ddob)
        today=datetime.date.today().year
        if today-s.year >50:
           print( ' are to old to hire.')
        elif today-s.year <17:
           print('you are to young to be hired.')
        else:
           break
       except:
          print('Enter valid date. Try again')

    while True:
       
       try:
         dh=int(input('enter day of hire:'))
         mh=int(input('enter month of hire:'))
         yh=int(input('enter year of hire:'))
         sh=datetime.date(yh,mh,dh)
         today=datetime.date.today().year


         if today - sh.year <0:
            print('This hire date is not possible.')
         elif today - sh.year >81:
            print('wrong hiredate.')

         else:
            print('OK')
            break
       except:
          print('Enter valid date. Try again')
    while True:
        idpq='select * from employee;'
        idp=pd.read_sql(idpq,con)
        uid=input('Create user id:')
        users= list(idp.get('user_id'))
        if uid in users:
           print('This user id is alredy used by some one.')

        elif uid not in users:
           break
    if admin==1:
       admin='admin'
    elif admin==0:
       admin=''       
    upwd=input('Create password:')
    l=(name,str(s),str(sh),jobcode,uid,upwd,admin)
    cmd='''insert into employee (emp_name ,dob ,hire_date,job_code ,user_id  ,passwd ,role )
    values("%s","%s","%s",%f,"%s","%s","%s")   ; 
)'''%l
    runcmd(cmd)

def showtable(tablename):
   cmd='''select * from %s;'''%tablename
   table=pd.read_sql(cmd,con)
   print(table)
 

def usetable(tablename):
   cmd='''select * from %s;'''%tablename
   table=pd.read_sql(cmd,con)
  
   return table
