# Removes all a's from string 

# pass the ans str in arg
# create the ans var in fun body 

def f1(s,ans,index):
    if index == len(s) : 
        return ans
    if s[index]!='a' :
        ans+=s[index]
        return f1(s,ans,index+1)
    else :
        return f1(s,ans,index+1)
print(f1("abcca",'',0))

# def f2(s,index) : 
#     ans=""
#     if index==len(s) : 
#         return ans 
#     if s[index]!='a' :
#         ans+=s[index]
#         return f2(s,index+1)
    
#     answer = f2(s,index+1)
#     ans.join(answer)
#     return ans
# print(f2("abcabc",0))

# skip apple 

def f3(s,index):
    if index == len(s) : 
        return ""
    if s.startswith("apple",index) : # cheacks strings from that index
        return f3(s,index+5)
    else :
        
        return s[index] + f3(s,index+1)
    
print(f3("abapplecca",0))

# Skip app but not apple 
def f4(s,index):
    if index == len(s) : 
        return ""
    if s.startswith("app",index) and not s.startswith("apple",index) : # cheacks strings from that index
        return f4(s,index+3)
    else :
        
        return s[index] + f4(s,index+1)
    
print(f4("appabapplecca",0)) # abapplecca






    





