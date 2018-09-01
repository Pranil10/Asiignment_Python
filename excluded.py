Excluded_words=['a', 'as', 'the', 'is', 'of', 'it', 'in', 'into', 'to', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was']
sent=input("Enter a sentence")
lst=sent.split()
count=0
for each in lst:
    if each in Excluded_words:
        count+=1
print('The no. of count word are',count)
