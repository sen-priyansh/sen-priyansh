from project import *
import pwinput as pw
#import setup
from projectimports import *
x=1
def startapp():
    
    print('''______WELCOME______''')

    idpq='select * from employee;'
    idp=pd.read_sql(idpq,con)
    if len(idp) == 0:
        print('the first user will be registered as admin with jobcode 1')
        
        jobcode= int(input('enter your job_code:'))
        job= input('enter name of your job')
        sal= int(input('enter salary'))
        l=(jobcode,job,sal)
        cmd='insert into job values(%f,"%s",%f);'%l
        runcmd(cmd)
        print('DEAR OWNER NEW JOB IS SECCESFULLY CREATERD NOW YOU HAVE TO ENTER YOUr DETAILS TO CONTINUE.')
        addemp(jobcode,1)
        print('NOW YOU CAN START YOU WORK.')
    
    elif len(idp)!=0:
        while True:
            print('HELLO')
            u = input('please enter your user id:')
            psd= pw.pwinput('enter password now:')
        
            uid= pd.Series(list(idp.get('passwd')),index=idp.get('user_id'))
            try:
                if uid[u] == psd:
                    users= pd.Series(list(idp.get('emp_name')),index=idp.get('user_id'))
                    userl=str(users[u])
                    print(userl)
                    role= pd.read_sql('select role from employee where user_id="%s";'%u,con)
                    role = role.iloc[0,0]
                    print(role)
                    if role=='admin':
                        role=open('user','w+')
                        role.write('1')
                        role.close()
                        mainappadmin()
                        quit()
                        
                        break
                    else:
                        role=open('user','w+')
                        role.write('0')
                        role.close()
                        mainappuser()
                        quit()
                        
                        break
                        
                        
                else:
                    print('wrong id or password please try again')
            except:
                print('wrong id or password please try again')
        quit()
startapp()