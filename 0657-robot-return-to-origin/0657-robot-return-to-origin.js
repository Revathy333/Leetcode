/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    let obj = {"U":0,"D":0,"R":0,"L":0};
    for(let a of moves){
        obj[a]+=1;
    }
    return obj["U"] == obj["D"] && obj["R"] == obj["L"] ? true:false; 
   
};