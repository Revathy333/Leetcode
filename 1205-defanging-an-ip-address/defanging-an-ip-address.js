/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    let newstring = address.replaceAll('.', '[.]');
    return newstring; 
};