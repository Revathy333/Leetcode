/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
   grid = grid.flat();
   let check = [];
   let dup,mis;
   for(let a of grid){
      if(check.includes(a)){
         dup = a;
         break;
      }else{
        check.push(a)
      }
   }
   for(let i = 1; i <= grid.length; i++){
      if(!grid.includes(i) ){
        mis = i;
        break;
      }
   }
   return [ dup,mis]
};