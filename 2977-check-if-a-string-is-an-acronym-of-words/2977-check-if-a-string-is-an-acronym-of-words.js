/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    let newone = [];
    for(let a of words){
       newone.push(a[0])
    }
    return newone.join("") == s ? true : false
};