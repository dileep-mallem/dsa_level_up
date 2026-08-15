# Find nth Fibonacci Number F(n) = F(n-1) + F(n-2)   

# Base Conds : F(0) = 0 , F(1) = 1 

def Fibo(n) :
    if n < 2 :  #Base Condn
        return n
    return Fibo(n-1) + Fibo(n-2)

print(Fibo(3))

# Print Fibo 

# Binay Search 

def binarySearch(a,key,s,e) : 
    if s <= e :
        m= (s+e)// 2
        if a[m] == key :
            return m 
        elif a[m] < key : 
            return binarySearch(a,key,m+1,e)
        else :
            return binarySearch(a,key,s,m)

a=[0,1,2,3,4,5,6]
print(binarySearch(a,4,0,7)) # 4 






