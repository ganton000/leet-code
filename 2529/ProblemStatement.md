# 2529. Maximum Count of Positive Integer and Negative Integer

Given an array `nums` sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

* In other words, if the number of positive integers in `nums` is `pos` and the number of negative integers is `neg`, then return the maximum of `pos` and `neg`.

Note that `0` is neither positive nor negative.



#### <b>Example 1:</b>
```
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
```
#### <b>Example 2:</b>
```
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
```
#### <b>Example 3:</b>
```
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
```

#### <b>Constraints:</b>

* `1 <= nums.length <= 2000`
* `-2000 <= nums[i] <= 2000`
* `nums` is sorted in a non-decreasing order.

#### My Notes:

* Since the list is sorted, we can use <b>Binary search</b> which has a time complexity of `O(logn)`.

<b>Binary search </b> searches for a specific element in a sorted list by repeatedly dividing the search interval in half.
It begins by comparing the middle element of the list, and searches the left half or right half depending on whether
the element to find is smaller or larger, respectively, to the middle element.
It iterates this process until finding the element.