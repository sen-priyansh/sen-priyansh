from pandas import *
# This is a to do list project.

class todolist:
    global l
    l = DataFrame(columns=['task','status'])
    print(l)
    def addtask(self,t):
        
        l.loc[len(l)]= (t,False)

    def comtast(self,n):
        l['status'].iloc[n]= True

    def printlist(self):
        print(l)

    def showincomptask(self):
        print(l[l['status']==False]['task'])

    def showcomptask(self):
        print(l[l['status']==True]['task'])

p = todolist()
p.addtask('kill a cat')
p.showincomptask()
p.printlist()