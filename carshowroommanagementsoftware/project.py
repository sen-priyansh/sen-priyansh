from projectimports import *

def checkstock():
    print('''1). CHECK FULL STOCK.
2). SEARCH STOCK BY CAR NAME.
3). SEARCH STOCK BY CAR TYPE.
4). BACK.''')
    c=int(input('enter your choise:'))
    if c==1:
        fullstock()
    elif c==2:
        nstk()
    elif c==3:
        mstk()
    elif c==4:
        mainapp()
    else :
        print('invalid input')
        mainapp()

def fullstock():
    cmd='''select m.carname,car_name , s.* from  stock s join car_name cn on (cn.car_no=s.car_no) join car_type m on (cn.model_type = m.carcode);'''
    stk=pd.read_sql(cmd,con)
    print(stk)
    checkstock()

def nstk():
    c=input('enter name of car:')
    cmd="select car_name , s.* from  stock s join car_name cn on (cn.car_no=s.car_no) where car_name='%s';"%c
    stk=pd.read_sql(cmd,con)
    print(stk)
    checkstock()

def mstk():
    c=input('enter type of car:')
    cmd='''select m.carname,car_name , s.* from  stock s join car_name cn on (cn.car_no=s.car_no) 
    join car_type m on (cn.model_type = m.carcode) where 
    carname='%s';
    '''%c
    stk=pd.read_sql(cmd,con)
    print(stk)
    checkstock()


def addcust():
    try:
        nm=input('enter customer name:')
        ph =int(input('enter phone no.:'))
        ad =input('enter adderess:')
        
        custlenght=len(pd.read_sql('select * from customer;'))

        l=(custlenght+1,nm,ph,ad)
        cmd='''insert into customer values(%f,'%s',%f,'%s');'''%l
        runcmd(cmd)
        
        cmd = '''select * from customer where cust_name = '%s';'''%nm
        s= pd.read_sql(cmd,con)
        print(s)
        mainapp()
    
    except:
        print('error due to invalid data.')
        mainapp()

def custdetil():
    
    cmd = '''select * from customer;'''
    s= pd.read_sql(cmd,con)
    print(s)
    mainapp()

def ncust():
    nm= input('enter name of customer').lower()
    
    try:
        cmd = '''select * from customer where cust_name = '%s';'''%nm
        s= pd.read_sql(cmd,con)
        print(s)
    except:
        print('data not found')
        mainapp()
    mainapp()

def scust():
    
    try:
        nm=int(input('enter sno:'))
        cmd = '''select * from customer where cust_no = '%f';'''%nm
        s= pd.read_sql(cmd,con)
        print(s)
    except:
        print('data not found')
        mainapp()
    mainapp()

def custd():
    try:
        x=int(input('''1). SHOW ALL DETAILS
2). SEARCH BY NAME
3).SEARCH BY S_NO
4).EXIT.'''))

        if x==1:
            custdetil()
        elif x==2:
            ncust()
        elif x==3:
            scust()
            
        elif x==4:
            mainapp()
        else:
            print('wrong input')
            mainapp()
    except:
        print('error due to wrong input ')
        mainapp()

def sell():
    try:
        cust=usetable('customer')
        ck_cno=list(cust.cust_no)
        n=int(input('enter cust_no:'))

        if n in ck_cno:
                
            st=input('state code:')    
            di =int(input('district code:'))
            secd =input('serial code:')
            seno =int(input('serial no:'))
            today=str(datetime.date.today())          
            cano =int(input("car's unique no:"))


            stk='''select stock_left from stock where car_no= %f;'''%cano
            stktable= pd.read_sql(stk,con)

            stkl=stktable.iloc[0,0]
            if stkl <= 0 :

                print('not enough stock')

            if stkl >0:

                l=(st,di,secd,seno,cano,n,today)
                cmd=''' insert into sell2 values('%s',%d,'%s',%d,%d,%d,'%s');'''%l
                cur.execute(cmd)
                con.commit()
                billcmd='select s.* ,car_name, sell_price as ammount_payable from sell2 s join car_name c on (c.car_no=s.car_no);'
                bill=pd.read_sql(billcmd,con)
                bill2=bill.iloc[-1]
                print(''' Your bill for purchase is:
    ''',bill2)
                ammount=bill2.loc[0,'ammount_payable']
                cmd2= '''update stock set stock_left= stock_left-1;'''
                
                cur.execute(cmd2)
                con.commit()
                
                print('congratulation the car is sold . Your ammount payable is :',ammount)

                mainapp()

        else :
            print("THIS CUST NO DON'T EXIST.")
            sell()

    except:
        print('error in some value')
        mainapp()

def addstock():
    print('''1).ADD CAR STOCK.
2).ADD NEW CAR .
3).ADD NEW CAR MODEL.
4).EXIT.''')
    c= int(input('Enter choise.'))
    if c== 1:
        try:
            showtable('stock')
            cmd= '''select * from stock;'''
            s=pd.read_sql(cmd,con)
            s2= pd.Series(s.get('car_no'))
            cn=int(input('enter car_no:'))
            no=int(input('enter no of stocks:'))
            s3=list(s2)
            l=(cn,no)
            if cn in s3:
                sel='''update stock set stock_left=stock_left+%f where car_no=%f;'''%l
                runcmd(sel)
            else :
                try:
                    cmd='''insert into stock (car_no,stock_left) values(%f,%f)'''
                    runcmd(cmd)
                except:
                    print('''car with this no does'nt exist in car table:''')
                    addstock()
            print('task compleated')
            mainapp()
        except(ValueError):
            print("ERROR DUE TO IN VALID DATA.")
            addcust()
        except:
            print("AN ERROR OCCURED.")
            addstock()
    elif c==2:
            
        try:
            showtable('car_name')
            name=input('ENTER NAME OF THE CAR :' )
            model=int(input('ENTER MODEL CODE OF THE CAR :'))
            check=usetable('car_type')
            check_model=list(check.carcode)
            
            if model in check_model:
                cp=int(input("ENTER IT'S COST PRICE : "))
                sp=int(input("ENTER IT'S SELL PRICE :"))
                c_no=int(input("GIVE IT A UNIQUE CAR_NO :"))
                check=usetable('car_name')
                ck_cno=list(check.car_no)
                
                if c_no not in ck_cno:
                    qty=int(input("ENTER QUANTITY :"))
                    cmd='''insert into car_name 
                    values("%s",%f,%f,%f,%f);'''%(name,model,cp,sp,c_no)
                    runcmd(cmd)
                    CMD=''' insert into stock (car_no,stock_left)
     values(%f,%f); '''%(c_no,qty)
                    runcmd(CMD)
                    print("NEW DATA  ADDED .")
                    addstock()
                    cmd=''

                else:
                    print('THIS CAR NO ALREADY EXIST.')
                    addstock()
            
            else:
                print("THIS MODEL DO NOT EXIST:")
                addstock
        
        except(ValueError):
            print("ERROR DUE TO IN VALID DATA.")
            addstock()

        except:
            print("ERROR DUE some INTERNAL PROBLEM.")
            addstock()

    elif c==3:
        try:
            showtable('car_type')
            x=usetable('car_type')
            name=input('Give name to the car model.:')
            code=int(input('Give an unique code for  model.:'))
            check=list(x.carname)
            check2=list(x.carcode)
            if name in check:
                print('This model already exist.')
                addstock()
            
            elif code in check2:
                print('This code is already used.')
                addstock()

            elif name not in check and code not in check2:
                cmd='insert into car_type values(%d,"%s"); '%(code,name)
                runcmd(cmd)
                print('Your task is done new model is added.')
                addstock()

        except(ValueError):
            print("ERROR DUE TO IN VALID DATA.")
            addstock()
        except:
            print("SOME ERROR OCCURED.")
            addstock()

    elif c==4:
        print('ok')
        mainapp()

    else:
        print('wrong input.')
        addstock()
        
     
def createjob():
    try:
        jobcode= int(input('enter your job_code:'))
        job= input('enter name of your job')
        sal= int(input('enter salary'))
        l=(jobcode,job,sal)
        cmd='insert into job values(%f,"%s",%f);'%l
        runcmd(cmd)
        print('done')
        mainapp()
    except:
        print('some error occured.')
        mainapp()

def remove_employee():
    try:
        showtable('employee')
        emp_no=int(input('enter emp_no (press any alphabet to discontinue)'))
        print('Are you sure abut that(y for yes/any key)')
        choise=input()
        if choise=='y':
            cmd='delete from employee where emp_no=%d;'%emp_no
            runcmd(cmd)
            mainapp()
        else:
            print('Task terminated.')
            mainapp()
    except:
        print('some error occured.')
        mainapp()

def resetapp():
    x=input('''DO YOU REALLY WANT TO RESET SOFTWARE.
(WARNING:ONCE THE DATA IS PERMANENTLY ERASED IT CANNOT BE RECOVERED)
(TYPE "sure" for yes/any key for no) : ''')
    if x=="sure":

        cmd="delete from  sell2 ;"
        runcmd(cmd)
        cmd="delete from  customer ;"
        runcmd(cmd)
        cmd="delete from employee;"
        runcmd(cmd)
        cmd="delete from  stock;"
        runcmd(cmd)
        cmd="delete from car_name ;"
        runcmd(cmd)
        cmd="delete from car_type;"
        runcmd(cmd)
        cmd="delete from  job  ;"
        runcmd(cmd)
        cmd="delete from  profit_loss ;"
        runcmd(cmd)
        print('done')
    else:
        print('OK')
        mainapp()

def mainappuser():
    roll=0
    print('''PLEASE SPECIFY YOU CHOISE.
1).CHECK THE STOCK.
2).ADD CUSTOMER
3).CUSTOMERS DETAILS
4).SELL CAR
5).ADD STOCK
6).SHOW PURCHASE LIST
7).EXIT''')

    x=int(input('enter your choise: '))
    
    if x==1:
        checkstock()

    elif x==2:
        addcust()
    
    elif x==3:
        custd()
    elif x==4:
        sell()
    elif x==5:
        addstock()
    elif x==6:
        showtable('sell2')
        mainapp()
    elif x==7:
        print('bye')
        quit()
    
    else:
        print('wrong input')
        mainapp()

def mainappadmin():
    roll=1
    print('''PLEASE SPECIFY YOU CHOISE.
1).CHECK THE STOCK.
2).ADD CUSTOMER
3).CUSTOMERS DETAILS
4).SELL CAR
5).ADD STOCK
6).SHOW PURCHASE LIST
THESE ARE SPECIAL FUNCTION ONLY FOR ADMIN USER.
7).SHOW SALES DETAILS
8).CREATE JOB
9).NEW EMPLOYEE
10).REMOVE EMPLOYEE
11).SHOW DETAILS OF EMPLOYEE
12).EXIT
13).RESET APPLICATION''')

    x=int(input('enter your choise: '))
    
    if x==1:
        checkstock()

    elif x==2:
        addcust()
    
    elif x==3:
        custd()
    elif x==4:
        sell()
    elif x==5:
        addstock()
    elif x==6:
        showtable('sell2')
        mainapp()
    elif x==8:
        createjob()
    elif x==9:
        showtable('job')
        addemp()
    elif x==10:
        remove_employee()
    elif x==11:
        showtable('employee')
        mainapp()
    elif x==12:
        print('bye')
        quit()
    elif x==13:
        resetapp()
    else:
        print('wrong input')
        mainappadmin()

def mainapp():
    roleTXT=open('user','r+')
    role=roleTXT.read()
    print(role)
    roleTXT.close()
    if role =='1':
        mainappadmin()
    if role == '0':
        mainappuser()