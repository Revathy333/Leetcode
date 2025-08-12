/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function(s) {
   let maxDepth = 0;
  let currentDepth = 0;
  for(let a of s){
    if((a == "(")){
      currentDepth++;
      if(currentDepth > maxDepth){
      maxDepth = currentDepth;
    }
    }else if(a == ")") {
      currentDepth--;
    }
  }
  return maxDepth;
};