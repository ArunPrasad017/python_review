def isUnique(string):
    if string == "" or len(string)==1:
        return True
    hash_set=set()
    for c in string:
        if c not in hash_set:
            hash_set.add(c)
        else:
            return False
    return True

print(isUnique(""))
print(isUnique("abcde"))
print(isUnique("abcda"))

## o(n) time and o(n) space