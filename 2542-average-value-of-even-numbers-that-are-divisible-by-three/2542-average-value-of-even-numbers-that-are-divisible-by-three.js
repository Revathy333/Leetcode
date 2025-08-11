/**
 * @param {number[]} nums
 * @return {number}
 */
var averageValue = function(nums) {
    let sum = 0;
    let count = 0;
    for(let a of nums){
        if(a % 3 == 0 && a % 2 == 0){
            count++;
            sum += a;
        }
    }
    return sum != 0 ? Math.floor(sum / count)  : 0;
};