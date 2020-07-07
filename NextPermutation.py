"""
31. Next Permutation

"""

def swap(nums,a,b):
    nums[a], nums[b] = nums[b],nums[a]

def reverse(nums,i):
    nums[i:] = nums[i:][::-1]

def nextPermutation(nums):
    k=len(nums)-2
    while k>=0 and nums[k]>=nums[k+1]:
        k-=1
    if k>=0:
        j = len(nums)-1
        while j>0 and nums[j] <= nums[k]:
            j-=1
        swap(nums,j,k)
    reverse(nums,k+1)
    return nums

lst = [1,5,1]
print(nextPermutation(lst))

