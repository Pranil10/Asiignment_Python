d1={'python':3, 'java':6,'perl':2}
d2={'c++':5,'angular':3,'python':5}
d3={}

for k,v in d2.items():
    d3[k]=v
    
for k,v in d1.items():
    if (k in d2):
        d3[k]=d3[k]+v
    else:
        d3[k]=v

print(d3)


