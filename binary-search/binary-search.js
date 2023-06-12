/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let startIdx = 0;
    let endIdx = nums.length - 1;

    while (startIdx <= endIdx) {
        let middleIdx = Math.floor((startIdx + endIdx) / 2);
        if (target > nums[middleIdx]) {
            startIdx = middleIdx + 1;
        } else if (target < nums[middleIdx]) {
            endIdx = middleIdx - 1;
        } else {
            return middleIdx;
        }
    }
    return -1;
    
};