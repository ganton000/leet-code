#include <iostream>
#include <vector>
#include <algorithm>

int maximumCount(const std::vector<int>& nums) {
	int n = nums.size();
	int pos=0, neg = 0;
	for (int i {}; i<n; i++) {
		if (nums[i]<0) neg++;
		else if (nums[i]>0) pos++;
	}
	return std::max(neg,pos);
}


/*
Time Complexity: O(n)
Space Complexity: O(1)
*/

// Note: std::lower_bound performs a binary search in a sorted range for a specific value.
// It returns an iterator pointing to the first element in the range that is not less than the value being searched for
int maximumCount_optimal(const std::vector<int>& v) {
	int n = v.size();
	int firstPos = std::lower_bound(v.begin(), v.end(), 1) - v.begin();
	int firstZero = std::lower_bound(v.begin(), v.end(), 0) - v.begin();
	int numOfZeros = firstPos - firstZero;
	return std::max(n- firstPos, firstPos - numOfZeros);

}


/*
Time Complexity: O(logn)
Space Complexity: O(1)
*/

int main() {

	std::vector<int> nums= {-3,-2,-1,0,0,1,2};
	std::vector<int> nums1= {5,20,66,1314};
	std::vector<int> nums2= {-2,-1,-1,1,2,3};

	std::vector<std::vector<int>> outerVector{nums, nums1, nums2};

	for (const auto &vect: outerVector) {
		int result = maximumCount(vect);
		std::cout << "result: " << result << std::endl;
	}

	std::cout << std::endl;

	for (const auto &vect: outerVector) {
		int result = maximumCount_optimal(vect);
		std::cout << "result: " << result << std::endl;
	}


	return 0;
}