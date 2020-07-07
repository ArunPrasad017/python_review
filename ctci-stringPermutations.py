def stringPermutations(s1,s2):
    if len(s1)!=len(s2):
        return False
    d1={}
    for c in s1:
        if c not in d1:
            d1[c] = 1
        else:
            d1[c]+=1
    for c in s2:
        if c not in d1:
            d1[c]=1
        else:
            d1[c]-=1
    res = all(v==0 for k,v in d1.items())
    return res

s1="abcd"
s2="acdb"
print(stringPermutations(s1,s2))