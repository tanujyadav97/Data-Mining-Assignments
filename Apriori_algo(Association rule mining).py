import numpy as np
import itertools
def findsubsets(S,m):
    liss=[]
    for i in range(1,m):
        liss+=list(itertools.combinations(S, i))
    return liss

data=np.array([[1,1,0,0,1],[0,1,0,1,0],[0,1,1,0,0],[1,1,0,1,0],[1,0,1,0,0],[0,1,1,0,0],[1,0,1,0,0],[1,1,1,0,1],[1,1,1,0,0]])

def count(li):
    c=0
    for j in range(1,10):
        cc=0
        for k in range(0,len(li)):
            cc+=data[j-1][li[k]-1]
        if cc==len(li):
            c+=1
    return c

thr=2
min_con=.7
dic1={}

newkey=[[1],[2],[3],[4],[5]]
for i in range(0,len(newkey)):
    dic1[i+1]=count(newkey[i])

print("c1 and l1")
print(dic1)
print("\n")

dic2={}
for i in dic1:
    if dic1[i]>=thr:
        dic2[i]=dic1[i]

key=dic2.keys()

for cc in range(2,8):
    newkey=[]
    for i in range(0,len(key)):
        for j in range(i+1,len(key)):
            if(cc==2):
                nl = []
                nl.append(key[i])
                nl.append(key[j])
                newkey.append(nl)
            else:
                if(key[i][:(cc-2)]==key[j][:(cc-2)]):
                    nl=key[i][:]
                    nl.append(key[j][len(key[j])-1])
                    newkey.append(nl)

    dic1.clear()
    for i in range(0,len(newkey)):
        dic1[i]=count(newkey[i])

    print("c"+str(cc))
    print(newkey)
    print(dic1)
    print("\n")

    key=[]
    dic2.clear()
    for i in dic1:
        if dic1[i]>=thr:
            dic2[i]=dic1[i]
            key.append(newkey[i])

    if len(dic2)==0:
        break

    print("l"+str(cc))
    print(key)
    print(dic2)
    print("\n")

    key3=[]
    key3=key

key=key3
result1=[]
result2=[]
for i in key:
    ss=findsubsets(i,len(i))
    for j in ss:
        if count(i)/count(j)>min_con:
            com=[item for item in i if item not in j]
            result1.append(j)
            result2.append(com)

print("Final associations")
for i in range(0,len(result2)):
    print(str(result1[i])+"->"+str(result2[i]))