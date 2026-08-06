from collections import defaultdict 

def group_anagrams(words):
    groups=defaultdict(list) # KEy : Sorted word , value : List of word 

    for word in words : 
        key="".join(sorted(word))
        groups[key].append(word)

    return list(groups.values()) 


# Alternative: use character frequency as key (avoids sorting)
# Key = tuple of 26 counts e.g. (1,0,0,...,1,...) for "ab"
def group_anagrams_v2(words):
    groups = defaultdict(list)

    for word in words:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        key = tuple(count)           # tuples are hashable → can be dict key
        groups[key].append(word)

    return list(groups.values())

# Same result, O(N * K) where K = average word length
# Better than O(N * K log K) from sort approach

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
result2 = group_anagrams(words)
print(result)
print("-----")
print(result2)

# How many pairs of anagrams exist in a word list?
def count_anagram_pairs(words2):
    groups = defaultdict(int)

    for word in words:
        key = "".join(sorted(word))
        groups[key] += 1 
    print(groups.values())

    # If a group has n words, there are n*(n-1)//2 pairs
    total = 0
    for n in groups.values():
        total += n * (n - 1) // 2

    return total

words2 = ["abcd", "dcba", "bcda", "xyz", "zyx"]
print(count_anagram_pairs(words2))   # 4 → C(3,2)+C(2,2) = 3+1