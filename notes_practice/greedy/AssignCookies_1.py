# greed factor : list n , x accept of size x>=x , 
# cookimies : list m 
# to assign max no of Cooking , retunr no of children getting cookins 

# sort cookines array 
# sort greedy factors arr
# two pointer , l to cookiees and r to greedy 
# satify  l+=1,r+=1 
# no satisfy , r+=1 until satisfy , if no cookie satisfy wrong (0) ans l+=1 and then repeat 

# fn(greed , size) : 
#     n=len(greed),m=len(size)
#     l=0
#     r=0
#     greed.sort(),size.sort()
#     while l<=m : 
#         if(greed[r]<=size[l]) : 
#             r+=1
#         l+=1
#     return r 

# TC : n logn + mlog m + m -> 
# SC : O(1)


greed=[1,5,3,3,4]
size=[4,2,1,2,1,3]

def assignCookies(g,s):
    n=len(g)
    m=len(s)

    g.sort()
    s.sort()

    l=0
    r=0
    while l<m: # m 
        if(g[r]<=s[l]):
            r+=1
        l+=1
    return r 

print(assignCookies(greed,size)) # 3 




