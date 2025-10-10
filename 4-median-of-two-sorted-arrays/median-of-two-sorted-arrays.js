/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let num3 = nums1.concat(nums2);
    num3.sort((a, b) => a - b);
    let len = num3.length;
    return len % 2 == 0 ? ((num3[len/2])+(num3[(len/2)-1]))/2 : num3[Math.floor(len/2)];
};