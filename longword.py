sent=input("Please enter a sentence!!!")
lst=sent.split()
longestword=''
for each in lst:
    if len(longestword)<len(each):
        longestword=each
print(longestword)

    
