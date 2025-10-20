/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var getCommon = function(nums1, nums2) {
    // let obj = {};
    // for(let n of nums1){
    //   obj[n] = true
    //     }
    //     let com = nums2.filter((n) => obj[n])
    
    // return Math.min(...com)
    if(nums1[nums1.length-1] < nums2[0])return -1
    for(let i = 0; i < nums1.length; i++){
        for(let j = 0; j < nums2.length; j++){
            if(nums1[i] == nums2[j])return nums1[i]
            
        }
    }return -1
};