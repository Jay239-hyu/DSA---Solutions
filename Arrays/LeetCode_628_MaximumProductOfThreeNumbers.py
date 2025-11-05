'''
Problem Info:
Problem No - 628
Title - Maximum Product of Three numbers
Topic - Array
Diffculty - Easy
Time Complexity - O(nlogn)
Space Complexity - O(1)
'''

nums = [-10, -10, 5, 2]

# Step - 1 : Sort the Array

nums.sort()

# Step - 2 : Calculate Two possible max prducts

option1 = nums[-1] * nums[-2] * nums[-3] #Top 3 largest Elements
option2 = nums[0] * nums[1] * nums[-1] #two smallest + one largest

#Step - 3: Return the maximum
print(f"Maximum Product of Three numbers: {max(option1 ,option2)}")



