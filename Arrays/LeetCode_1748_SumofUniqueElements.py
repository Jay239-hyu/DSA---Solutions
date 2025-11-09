
'''
Problem Info:
Problem No  - 1748
Title       - Sum of Unique Elements
Topic       - Array/Hashmap/Counting
Difficulty  - Easy
Tc          - O(n)
Sc          - O(n)
'''



nums = [1 , 2 , 3 , 2]

#By HashMap Approach

freq = {}

#Stores elements and their frequencies in Dict 
for x in nums:
    freq[x] = freq.get(x , 0) + 1

#Sum of Unique elements using Generator Expression

Sum_of_Unique_elements = sum(x for x , c in freq.items() if c == 1)

print(Sum_of_Unique_elements)





