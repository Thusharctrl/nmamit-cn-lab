div=[1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1]
m=len(div)
data=[]
n=int(input("enter the no of bits:"))

for i in range (n):
    data.append(int(input()))
cdata=data.copy()

for i in range (m-1):
    cdata.append(0)
print("intial codeword:",cdata)

for i in range (n):
    if cdata[i]==1:
        for j in range(m):
            cdata[i+j]=cdata[i+j]^div[j]
data=data+cdata[n:]
print("transmitted cd:",data)

ch=input("enter ur choic Y/N to introduce error")

if(ch.upper()=='Y'):
    p=int(input("enter a position:"))
    if 1<=p<=len(data):
        data[p-1]=1-data[p-1]
    else:
        print("invalid")
for i in range (n):
    if data[i]==1:
        for j in range (m):
            data[i+j]=data[i+j]^div[j]
            
if 1 in data[n:]:
    print("error")
else:
    print("Success!!")
