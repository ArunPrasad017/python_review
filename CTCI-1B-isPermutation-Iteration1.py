def isPermutation(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(isPermutation("abc", "bac"))
print(isPermutation("aabbc", "bcaba"))
print(isPermutation("abc", "ab"))


### needs improvement in speed - use the Count characters method