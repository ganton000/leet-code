function maximumCount (nums: number[]): number {
	let pos = 0;
	let neg = 0;

	for(let num of nums) {
		if (num > 0) pos++;
		if (num < 0) neg ++;
	}

	return Math.max(pos, neg)
};


function main(): void {

	const nums: number[] = [-3,-2,-1,0,0,1,2];
	const nums1: number[] = [5,20,66,1314];
	const nums2: number[] = [-2,-1,-1,1,2,3];

	const nums_arr: Array<number[]> = [nums, nums1, nums2]

	for (let num_arr of nums_arr) console.log(maximumCount(num_arr));

}

main()

/*
Time Complexity: O(n)
Space Complexity: O(1)
*/