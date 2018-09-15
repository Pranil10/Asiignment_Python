marks_lst=[]


def stud_data():
    num_sub=int(input("Enter the number of subjects:-"))
    print("Enter Your Marks:-")
    for i in range(num_sub):
        marks=int(input(""))
        marks_lst.append(marks)



def percent():
    global percentage       
    percentage=((sum(marks_lst))/(len(marks_lst)*100))*100
    return percentage


def grade():
    if percentage>=90:
        return 'O'
    elif percentage>=75 and percentage<90:
        return 'A'
    elif percentage>=60 and percentage<75:
        return 'B'
    elif percentage>=45 and percentage<60:
        return 'C'
    elif percentage>=35 and percentage<45:
        return 'D'
    else:
        return 'F'
        
name=input("Enter your name:-")
rollno=int(input("Enter your roll no:-"))
stud_data()
print("The Percentage of", name, "is :-",percent())
print("The grade is", grade())

        
