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