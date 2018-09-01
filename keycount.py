st=input("Enter a sentence")
key=input("Enter the word you want to search")
lst=st.split()
for each in lst:
    if each==key:
        counter = lst.count(each)
print(key, ':', counter)        

