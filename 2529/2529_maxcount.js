function maximumCount(nums) {
    var pos = 0;
    var neg = 0;
    for (var _i = 0, nums_1 = nums; _i < nums_1.length; _i++) {
        var num = nums_1[_i];
        if (num > 0)
            pos++;
        if (num < 0)
            neg++;
    }
    return Math.max(pos, neg);
}
;
function main() {
    var nums = [-3, -2, -1, 0, 0, 1, 2];
    var nums1 = [5, 20, 66, 1314];
    var nums2 = [-2, -1, -1, 1, 2, 3];
    var nums_arr = [nums, nums1, nums2];
    for (var _i = 0, nums_arr_1 = nums_arr; _i < nums_arr_1.length; _i++) {
        var num_arr = nums_arr_1[_i];
        console.log(maximumCount(num_arr));
    }
}
main();
/*
Time Complexity: O(n)
Space Complexity: O(1)
*/ 
