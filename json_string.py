import json
book={};

book['tom']={
    "name":"tom",
    "address":"162/a , yatigala, beliatta",
    'phone':764492334
}

book['bob']={
    "name":'bob',
     "address":"1/T, hakmana",
    "phone":"771253346"
}

#write the json strin to .txt file

s= json.dumps(book)
with open("c://L2S2/book.txt","w")  as f:
    f.write(s)
print(s)


f=open("c://L2S2/book.txt","r")
q=f.read();
print(q) #string
book=json.loads(q)
print(book) #dictonery

print(book["bob"])
print(book['bob']['phone'])


#print  all the book data strings


for person in book:
    print(book[person])

