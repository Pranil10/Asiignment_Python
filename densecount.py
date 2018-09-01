st=input("Enter a sentence")
key=input("Enter a word of which density you want to search")
lst=st.split()
for each in lst:
    if each==key:
        counter = lst.count(each)
leng=len(lst)
density=counter/leng
print('Density :', density)
