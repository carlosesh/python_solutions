"""
Find the Highest Integer in the List Using Recursion
Create a function that finds the highest integer in the list using recursion.

Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8
Notes
Please use the recursion to solve this (not the max() method).
"""

def find_highest(lst, max = float('-inf')):	
	lst_len = len(lst)
	if lst_len <= 1:
		return lst[0] if lst[0] > max else max
	else:
		max = lst[0] if lst[0] > max else max
		lst_len -= 1
		return find_highest(lst[1:], max)
