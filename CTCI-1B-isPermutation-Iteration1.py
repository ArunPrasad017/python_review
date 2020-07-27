def isPermutation(s1,s2):
    return sorted(s1) == sorted(s2)

print(isPermutation("abc", "bac"))
print(isPermutation("aabbc", "bcaba"))
print(isPermutation("abc", "ab"))


### needs improvement in speed - use the Count characters method