// https://leetcode.com/contest/weekly-contest-327/problems/maximum-count-of-positive-integer-and-negative-integer/

#include <iostream>
#include <vector>

int maximumCount(const std::vector<int>& nums) {
	int n = nums.size();
	int pos=0, neg = 0;
	for (int i {}; i<n; i++) {
		if (nums[i]<0) neg++;
		else if (nums[i]>0) pos++;
	}
	return std::max(neg,pos);
}

int main() {

	std::vector<int> nums= {-3,-2,-1,0,0,1,2};
	std::vector<int> nums1= {5,20,66,1314};
	std::vector<int> nums2= {-2,-1,-1,1,2,3};

	std::vector<std::vector<int>> outerVector{nums, nums1, nums2};

	for (const auto &vect: outerVector) {
		int result = maximumCount(vect);
		std::cout << "result: " << result << std::endl;
	}


	return 0;
}


/*
Time Complexity: O(n)
Space Complexity: O(1)
*/