/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
     pos = 1;
     count = 0
    for(let a of nums){
        pos += a;
        if (pos == 1){
            count++;
        }
    }
    return count;
};