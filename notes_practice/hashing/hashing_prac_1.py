s="Dcileep Kumar".lower()

d={}

for i in s :
    d[i]=d.get(i,0) + 1
print(d)

# First Non Repeating Chracter in String 

for key , value in d.items():
    if value == 1 :
        print(s.index(key))
        break 
# MAximum Frequent ELement 
max_count = 1
for key , value in d.items():
    max_count=max(max_count,value) 
    if value == max_count :
        k=key

print("Max Occurence Element : ",k)

# Sort characters by Freyuent 

s1=[1,2,3,1,3,5,6,2,3,1]
n=len(s1)
d1={}
for i in s1 :
    d1[i]=d1.get(i,0) + 1
print(d1)
l=[]
for key , value in d1.items():
            l.append((key,value))
s=sorted(l,key= lambda x : (x[1],x[0]),reverse=True)
print(s)
print(s[1][1])
l2=[]
for i in s:
    l2.append(i[0])


# majority Elemet ( > n/3 appers) 
nums=[1,3,2,5,1,3,1,5,1] 
n=len(nums) 

# Key : Num , val : freq 
r={}
r1=[]
for i in nums :
    r[i]=r.get(i,0) + 1
for key , value in r.items() :
    if value > n / 3 :
        r1.append(key)
print("Majority Elements (Appears n/3 times) : ",r1)

# Union of two Arrays 
a1=[7,3,9]
a2=[6,3,9,2,9,4]




 




