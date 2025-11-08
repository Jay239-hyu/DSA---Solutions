
'''
Problem Info:
Problem No  - 169
Title       - Majority Element
Topic       - Array/Counting
Difficulty  - Easy
Approach    - Boyer - Moore Majority vote algo
Tc          - O(n)
Sc          - O(1)

'''




nums = [2,2,1,1,1,2,2]


#As per Boyer - Moore majority vote Algo
candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num
    if num == candidate:
        count+=1
    else:
        count-=1

print(f"The majority Element in nums: {candidate}")


    
        


