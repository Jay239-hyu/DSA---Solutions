'''
Problem Info:
Problem No - 189
Title - Rotate Array
Topic - Array / Math
Diffculty - Medium
Time Complexity - O(n)
Space Complexity - O(1)
'''









nums = [1 , 2 , 3 , 4 , 5 , 6 , 7]
k = 3

#Reversal Approach For this Perticular Problem
def reverse(l , r):
    while l < r:
        nums[l] , nums[r] = nums[r] ,  nums[l]

        l += 1
        r -= 1

reverse(0 , len(nums)-1)
reverse(0 , k-1)
reverse(k , len(nums)-1)

print(f"Final List Rotated with {k} : {nums}")

#--------------------------------------------------------------
#Python slicing Approach For Real-World Scenarios

# def rotate(nums , k):
#     n = len(nums)
#     k %= n
#     nums[:] = nums[-k:] + nums[:-k]
#     print(f"Final List Rotated with {k} : {nums}")

# rotate(nums , k)








