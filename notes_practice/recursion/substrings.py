# Permutaions and COmbinations 
# Subset -> Non-adjacent Colection 

s="abc" # a,b,ab,ac,bc,abc

#***** This pattern taking some elements and removing some -> Subset Patterns

def substring1(ans,s) : 
    if s=="" :
        print(ans,end=" ")
        return 
    ch = s[0]
    substring1(ans+ch,s[1:]) # take it
    substring1(ans,s[1:]) # Ignore

substring1("",s)

print()

# Return list of Substrings without passing in args

def substring2(ans,s) : 
    left,right=[],[]
    if s=="" :
        l=[]
        l.append(ans)
        return l
    ch = s[0]
    left.extend(substring2(ans+ch,s[1:])) # take it
    right.extend(substring2(ans,s[1:])) # Ignore
    left.extend(right)
    return left

print(substring2("",s)) # Total 8 (2**3) = ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']

# Print substring also constits ASCII values

def substring3(ans,s) : 
    if s=="" :
        print(ans,end=" ")
        return 
    ch = s[0]
    substring3(ans+ch,s[1:]) # take it
    substring3(ans,s[1:]) # Ignore
    substring3(ans + str(ord(ch)),s[1:])

substring3("",s)

print()






