class employee:
    'This program has a class which derives two subclasses'
    def __init__(self,eid,name,age):
        self.eid=eid
        self.name=name
        self.age=age
    def display(self):
        print("Eid:-",self.eid,"Name:-",self.name,"Age:-",self.age)
        
    def __add__(self,manager_list):
        max1=self.salary
        for i in range(len(manager_list)):
            if max1<=manager_list[i].salary:
                max1=manager_list[i].salary
                z=i
        print('manager having highest salary')
        print('eid :',manager_list[z].eid,'|  name :',manager_list[z].name,'|  age :',manager_list[z].age,'|  salary :',manager_list[z].salary)
    def __mul__(self,manager_list):
        min1=self.salary
        for i in range(len(manager_list)):
            if min1>=manager_list[i].salary:
                min1=manager_list[i].salary
                w=i
        print('develoer having lowest salary')
        print('eid :',manager_list[w].eid,'|  name :',manager_list[w].name,'|  age :',manager_list[w].age,'|  salary :',manager_list[w].salary)

        

class manager(employee):
    def __init__(self,salary,eid1,name1,age1):
        self.salary=salary
        employee.__init__(self,eid1,name1,age1)


class developer(employee):
    def __init__(self,salary,eid1,name1,age1):
        self.salary=salary
        employee.__init__(self,eid1,name1,age1)

manager_list=[]
developer_list=[]
n=int(input('How many MANAGERS would you want to add in your company?'))
for i in range(n):
    print("Details of Manager", i+1)
    eid1=int(input("Enter Eid:-"))
    name1=input("Enter name:-")
    age1=input("Age:-")
    salary=float(input("Enter Salary:-"))
    manager_list.append(manager(salary,eid1,name1,age1))

no=int(input('How many Developers would you want to add in your company?'))
for i in range(no):
    print("Details for Developer", i+1)
    eid1=int(input("Enter eid:-"))
    name1=input("Enter name:-")
    age1=input("Age:-")
    salary=float(input("Enter Salary:-"))
    developer_list.append(developer(salary,eid1,name1,age1))

print("--------------------------------------------")
print("THE DETAILS OF ALL EMPLOYEES")
for i in range(len(manager_list)):
    manager_list[i].display()
for i in range(len(manager_list)):
    developer_list[i].display()    
print("---------------------------------------------")
manager_list[0]+(manager_list)
developer_list[0]*(developer_list)
        
