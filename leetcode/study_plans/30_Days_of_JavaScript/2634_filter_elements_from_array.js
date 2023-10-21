/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    for (let i = arr.length-1; i > -1; i--)
        if (!fn(arr[i], i)) arr.splice(i, 1);

    return arr;
};