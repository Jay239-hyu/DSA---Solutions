'''
Problem Info:
Problem No - 35
Title - Search Insert Position
Topic - Array / Binary Search
Diffculty - Easy
Time Complexity - O(logn)
Space Complexity - O(1)
'''

#Binary Search Approach for batter Tc
nums = [1,3,5,6]
target = 7

#Set left and Right Variables
left = 0  
right = len(nums) - 1

while left<=right:
    mid = (left + right) // 2 #Find mid index with floor division

    if nums[mid] == target:
        print(mid)
        break

    if nums[mid] > target: # if Target is small than mid so update right 
        right = mid - 1 

    else:                  # Otherwise update left
        left = mid + 1
    
print(f"Insertion Position for Target is {left}")

    

