dict2={'Taj Mahal':'Agra ,Uttar Pradesh',
       'Sachi Stupa':'Vidisha ,Madhya Pradesh',
       'Qutub Minar':'Delhi',
       'Khajuraho Temple':'Khajuraho ,Madhya Pradesh',
       'Nanda Devi':'Uttrakhand'}
dict1={'sidd2006':1234,'cruise':1234}
k=0
z='Yes'
p='No'
d=''
l='Skip'
def user():
    while True:
        print('''
        1.Add
        2.Modify
        3.Delete
        4.Show Site Names
        5.Show Details
        6.Search
        7.Log Out''')
        q2=int(input('enter your choice'))
        if q2 ==1:
            a=input('enter heritage site')
            b=input('enter the city/state')
            dict2[a]=b
        elif q2 ==2:
            a1=input('enter the already existing site')
            b1=input('enter its city/state')
            dict2.update({a1:b1})
        elif q2 == 3:
            a2=input('enter the site to be deleted')
            del dict2[a2]
        elif q2 == 4:
            print(dict2.keys())
        elif q2 == 5:
            print(dict2.values())
        elif q2 == 6:
            try:
                sl=input('enter the name of the city').lower()
                for i in dict2:
                    w=dict2[i].lower().split(' ')
            
                    if sl in w:
                        print(i)
            except:
                '''print('no heritage site like this')'''
        elif q2== 7:
            print('Successfully Logged Out')
            break
while True:
    try :
        a=input('enter your id')
        b=int(input('enter your passsword'))
        if dict1[a] == b:
            print('Logged In')
            user()
            break
        else:
            print('oops ,id or password may be wrong')
            d=input('do you want to continue yes/no')
            if d==p:
                print('okay')
                break 
    except :
        print('there is no such user id')

