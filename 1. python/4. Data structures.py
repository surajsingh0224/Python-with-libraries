# Write a program to remove duplicates from the list:
'''
num = [1, 2, 2, 3, 4, 4, 5]
unique_nums = []
for items in num:
    if items not in unique_nums:
        unique_nums.append(items)
        
print(f"removed duplicates are {unique_nums}")
'''

# Find Second Largest Number - nums = [10, 30, 20, 50, 40] Find the second largest number without sorting the list.
'''
nums = [10, 30, 20, 50, 40]
largest = float('-inf')
second_largest = float('-inf')


for num in nums:
    if num > largest:    
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
        
print(f"The second largest number is : {second_largest}")
'''

# Reverse a List Using a Loop (no built-ins)

# data = [1, 2, 3, 4, 5]
# left = 0
# right = len(data) - 1
# while left < right:
#     data[left], data[right] = data[right], data[left]
#     left += 1
#     right -= 1
    
# print(data)

from collections import Counter
items = ["a", "b", "a", "c", "b", "a"]
frequency = Counter(items)
print(frequency)