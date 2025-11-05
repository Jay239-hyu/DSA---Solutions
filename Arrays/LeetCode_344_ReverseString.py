'''
Problem Info:
Problem No - 344
Title       - Reverse String
Topic       - String
Difficulty  - Easy

Approach Summary:
--------------------------------------------------------------
Approach          | Time  | Space | In-place | Works on LeetCode
--------------------------------------------------------------
Two-pointer Swap  | O(n)  | O(1)  | ✅        | ✅
s.reverse()       | O(n)  | O(1)  | ✅        | ✅
Slicing s[::-1]   | O(n)  | O(n)  | ❌        | ❌
--------------------------------------------------------------

Notes:
- s[::-1] creates a new reversed list (not in-place).
- s.reverse() reverses the original list in-place.
- Two-pointer approach is language-agnostic and interview-friendly.
'''

# Example:
s = ["h","e","l","l","o"]

# Creates a new list, original remains same
s = s[::-1]

# Modifies the original list in-place
s.reverse()

print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
