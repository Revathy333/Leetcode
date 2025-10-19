/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    let sum1 = "";
    let sum2 = "";
    for(let a of word1){
         sum1+=a;
    }
    for(let b of word2){
        sum2+=b;
    }
    return sum1 == sum2 ? true : false
};