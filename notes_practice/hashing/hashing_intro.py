# We can use Dic's for hashmaps 

# Frequncey Count , for Brute O(n*k) k is size ofarray 
# We can compute it with maps [key : count ]
# Keys must be hashable and Immutable (int , float , tuple , str)
# hash is mapped to a slot index in an internal array (table size is always a power of 2).
nums=[1,2,1,4,3,2,5]
n=len(nums)

d={}

for i in nums : # TC : O(n)
    d[i] = d.get(i,0) + 1 # d.get(i,0) == { i : 0 } assing anf +1 -> { i : 1 }

print(" Frequency of Each Element : ",d)
# Count of 1 
print(d[1])






