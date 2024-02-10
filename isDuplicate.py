#Given an array of integers, find if the array contains any duplicates. 
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. 
nums = [1,2,3,1]

def isDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(isDuplicate(nums))