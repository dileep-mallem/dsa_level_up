# Iterative Apprpach for PnC 
# List of Lists 

def subset1(arr) :  # Time : O(n * 2**n) Space : O(2**n *n) Total subsets , space taken by each subset
    outer = []

    outer.append([])

    for num in arr : 
        n = len(outer)

        for i in range(n) : 
            internal=outer[i].copy()
            internal.append(num)
            outer.append(internal)

    return outer
print(subset1([1,2,3]))


# Handling Duplicates 

def subset2(arr : list[int] , ) : 
    arr.sort()
    outer = []
    outer.append([])

    start,end =0,0 



    for i in range(len(arr)) : 
        start=0 
        # if current and prevous elemnt is same , start = end + 1

        if i > 0 and arr[i]==arr[i-1] :
            start=end+1
        
        n = len(outer)
        end = n-1

        for j in range(start , n) :  # **
            internal=outer[j].copy()
            internal.append(arr[i])
            outer.append(internal)

    return outer
print(subset2([1,2,2]))