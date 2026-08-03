# Everything Wortr Correctly , But insted of Prepend I concat and then reversed the Strings h1,h2 -> Which Get Some BUg
class Solution(object):
    def decodeString(self, s):
        s2=[]
        r=""
        for ch in s :
            if ch.isalnum():
                s2.append(ch)
            elif ch=='[' :
                s2.append(ch)
            elif ch==']':
                h1=""
                while s2 and s2[-1]!='[':
                    h1=s2.pop() + h1 # Prepend
                s2.pop() # pop [
                
                h2=""
                while s2 and s2[-1].isdigit():
                    h2 = s2.pop() + h2
                h2=int(h2)
                s2.append(h1 * h2)
    
        return "".join(s2) # Learn This