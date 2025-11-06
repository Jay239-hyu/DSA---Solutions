'''
Problem Info:
Problem No - 1752
Title - Check if Array Is Sorted and Rotated
Topic - Array
Diffculty - Easy
Time Complexity - O(n)
Space Complexity - O(1)
'''

nums = [2,1,3,4]
count = 0
for i in range(len(nums)):
    if (nums[i] > nums[(i+1) % len(nums)]):#Condition of Breaking point
        count = count + 1

if count <= 1:
    print("True")
else :
    print("False")
         
