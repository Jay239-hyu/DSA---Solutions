
'''
Problem Info:
Problem No - 1796
Title - Second Largest Digit in a String
Topic - String/Array
Diffculty - Easy
Time Complexity - O(n)
Space Complexity - O(1)
'''



s = "dfa12321afd"

#Step - 1 : Extract Digits and Convert into int
digits = {int(ch) for ch in s if ch.isdigit()} #Extract Unique Digits

if len(digits) < 2:
    print("-1")
 

print(sorted(digits)[-2]) #Second Largest