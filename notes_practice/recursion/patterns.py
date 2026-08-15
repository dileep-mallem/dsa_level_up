def f1(r,c) :
    if r==0 :
        return 
    if c<r :
        print("*",end=" ")
        f1(r,c+1) 
    else : 
        print()
        f1(r-1,0)
f1(4,0) 

# here below function f2 prints when functions leaves the stack ,after BAse Condition Occurs
def f2(r,c) :
    if r==0 :
        return 
    if c<r :
        f2(r,c+1) 
        print("*",end=" ")
    else : 
        f2(r-1,0)
        print()
f2(4,0) 
print()