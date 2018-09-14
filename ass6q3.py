d1={'python':3, 'java':6,'perl':2,'c++':5,'angular':3}
ans=sorted(d1, key=d1.get, reverse=True)
for each in ans[:3]:
    print(each,end='\n')



    
