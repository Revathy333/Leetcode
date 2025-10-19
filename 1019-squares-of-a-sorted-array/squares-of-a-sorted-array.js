/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
   let num2 = nums.map((item) => item*item);
   return num2.sort((a,b) => a-b);
};