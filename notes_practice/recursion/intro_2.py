# numbers 1 - 5
# Recusrsive fns have Same Body and Sturcture  ( Thasts y fun calls Itelf instead of Creating Multiple Fns)

# Every Fn call Take Memory Seprately , If no Base Condn -> Memory Exceed -> recurion Error(Max Recn Depth Exceeded) and Stack OverFlow Error  

def number(n): 
    if n>5:      # Base Conditon in Recursion(Fn call Itself) , Condition where Our Recursion Stop making Calls 
        return 
    print(n)
    number(n+1) # Tial Recusrion

number(1)

# Why Recursion -> It Helps in Solving Bigger . Cpmplex Problems in a Simpler Way
#                   You can Convert Recursion Soln into Iteration & vice Versa 
#                   Space Complexity is not constant coz of Recursive Calls 
#                     Bigger -> Smaller Problems 
print()
def fun(n):
    if n > 0 :
        print(n)
        fun(n-1)
fun(5)

print()

# Facotrail 

def factorial(n):
   if n==1 or n==0 :
    return 1 
   return n * factorial(n-1)

print(factorial(5))

print()

# Sum of n Numners
def sum1(n) : 
    if n == 1 :
        return 1
    return n + sum1(n-1)
print(sum1(5))

print()
# Sum of Digts 
def digitSum(n) : 
    if n==0 :
        return 0
    return digitSum(n//10) + (n%10)
print(digitSum(1342))

print()
# Product of Digts 
def digitProd(n) : 
    if n==0 : # or n%10 == n : return n
        return 1
    return digitProd(n//10) * (n%10)
print(digitProd(1302))


# Reverse a Number 

def rev(n,sum=0) : 
    if n%10 == n : 
        return sum * 10 + n
    rem = n % 10 
    sum = sum * 10 + rem 
    return rev(n//10,sum)

print(rev(1432))
# Palindrome 1 . palin(n,s,e)

def palin(n):
    return n==rev(n)
print(palin(1441))
# Count of Zeores 
def zeores(n,count) : 
    if n == 0 : 
        return count
    if n%10 == 0 : 
        return zeores(n//10,count+1)
    else : 
        return zeores(n//10,count)

print(zeores(30402,0))