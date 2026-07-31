class Solution(object):
    def minimumPushes(self, word):
        
        total=0
        freq={}
        l=[]
        for i in word :
            freq[i]=freq.get(i,0)+1
            # if freq[i]==1 :
            #     l.append(i)

        # l should be Sort based on freq to get Min Push
        for key,value in freq.items() :
            l.append((key,value))  
        sorted_l=sorted(l,key = lambda x : (x[1],x[0]),reverse = True)
 
        for i in range(len(sorted_l)) :
            total += freq[sorted_l[i][0]] * ((i//8) +1 )
        return total 
        


    # for key,value in freq.items() :
    #         l.append(key)  
    #     sorted_l=sorted(l,key = lambda x : (freq[x],x),reverse = True)