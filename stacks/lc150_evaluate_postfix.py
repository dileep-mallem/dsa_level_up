class Solution(object):
    def evalRPN(self, tokens):
        stack=[]

        ops={'+','-','*',"/"}
        
        for i in tokens :
            # if i.isdigit(): # it doenst evaluate neg nus like "-11"
            #     stack.append(int(i))
            if i not in ops :
                stack.append(int(i))
            else : # Operators
                n2=stack.pop()
                n1=stack.pop()
                if i=='+':
                    result=n1+n2
                elif i=='-':
                    result=n1-n2
                elif i=='*':
                    result=n1*n2
                elif i=='/':
                    result=int(float(n1)/n2)
                stack.append(result)
        return stack[0]
