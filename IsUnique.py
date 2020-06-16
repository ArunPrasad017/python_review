# Key: ask if the string is supposed to be an ascii or unicode character
# with a datastructure:

def isUnique(str1):
    set_str1 = set(str1)
    if len(str1)==len(set_str1):
        return True
    return False

def isUniqueNoDS(str1):
    # we are not using the sort here because the space complexity of python sort 
    # is already o(n) and we want to avoid extra space requirements
    # this implementation TC = o(n^2) and SC = o(1)
    for i in range(len(str1)):
        for j in range(len(str1)):
            if str1[i] == str1[j] and i!=j:
                return False
    return True


str1 = "Data"
print(isUniqueNoDS(str1))