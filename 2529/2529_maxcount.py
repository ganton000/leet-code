# https://leetcode.com/contest/weekly-contest-327/problems/maximum-count-of-positive-integer-and-negative-integer/


from typing import List

def maximumCount(nums: List[int]) -> int:
	if nums[0] > 0: return print(len(nums))

	pos = len(list(filter(lambda x: x > 0, nums)))
	neg = len(list(filter(lambda x: x < 0, nums)))
	print(max(pos, neg))
	return max(pos, neg)

if __name__ == "__main__":
	nums = [-3,-2,-1,0,0,1,2]
	maximumCount(nums) # 3
	nums = [5,20,66,1314]
	maximumCount(nums) # 4
	nums = [-2,-1,-1,1,2,3]
	maximumCount(nums) # 3


'''
Time Complexity: O(n)
Space Complexity: O(n)
'''