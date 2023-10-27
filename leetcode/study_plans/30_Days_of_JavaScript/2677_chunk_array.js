/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let returnVal = [];

    for (let i = 0; i < arr.length; i += size)
        if ((i+size) <= arr.length)
            returnVal.push(arr.slice(i, i+size)); // next chunk of elements
        else
            returnVal.push(arr.slice(i)); // remaining elements

    return returnVal;
};
