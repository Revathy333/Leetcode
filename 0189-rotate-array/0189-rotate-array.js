/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    if(nums.length>k){
       nums.unshift(...nums.splice(-k))
    }else{
       for(let i = 1; i<= k; i++){
             nums.unshift(nums.pop());
           }
        }
    return nums;
};