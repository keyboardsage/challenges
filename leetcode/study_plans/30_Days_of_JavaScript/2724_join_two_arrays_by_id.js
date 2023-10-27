/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let combined = [...arr1, ...arr2]; // concatenate the arrays
    let returnValue = {};
    
    // for each element...
    combined.forEach((curr) => {
        // ...if the element doesn't exist, add it
        if (!returnValue[curr.id]) returnValue[curr.id] = curr;
        // ...but if it does exist, add any missing keys, or overwrite existing ones
        else
            for (const key in curr)
                returnValue[curr.id][key] = curr[key];
    });

    return Object.values(returnValue);
};