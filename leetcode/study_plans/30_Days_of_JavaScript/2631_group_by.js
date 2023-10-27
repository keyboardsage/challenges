/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let obj = {};
    let key, value;

    for(const value of this) {
        key = fn(value); // determine what the key should be called
        
        // add/update it in the object
        if (key in obj) obj[key].push(value);
        else obj[key] = [value];
    };
    
    return obj;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */