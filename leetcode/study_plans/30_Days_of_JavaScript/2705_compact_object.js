/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    let finalObj = {};

    // adding to an object is different from adding to an array, this function
    // creates a standard interface for adding to both
    function addTo(arrOrObj, theKey, theValue) {
        (Array.isArray(arrOrObj)) ? arrOrObj.push(theValue) : arrOrObj[theKey] = theValue;
    }

    function compact(arrOrObj) {
        let tmp = (Array.isArray(arrOrObj)) ? [] : {};
        let value = 0;
        
        for (key in arrOrObj) { // for each key...
            value = arrOrObj[key];
            if (Boolean(value)) // if its true...
                addTo(tmp, key, (typeof value !== 'object') ? value : compact(value)); // ...save it
        }

        return tmp;
    }

    // do the work
    finalObj = compact(obj);

    return (Array.isArray(obj)) ? Object.values(finalObj) : finalObj;
};