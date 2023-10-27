/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    // trivial case
    if (n === 0) return arr;

    // helper function that removes one level of arrays
    function unarray(currArr, unArr) {
        currArr.forEach((elementOfElement) => {
            if (Array.isArray(elementOfElement)) unArr.push(...elementOfElement);
            else unArr.push(elementOfElement);
        });

        return currArr;
    }

    // put the array's elements into an object...
    let resultValue = {}; // used as a temp
    let intermediate = [];
    arr.forEach((item, index) => {
        resultValue[index] = [item]; // ...wrapped with an extra enclosing array

        // then, unarray it `n`-1 times
        for (let i = 0; i < (n-1); i++)
            for (let j = 0; j < resultValue[index].length; j++)
                if (Array.isArray(resultValue[index][j]))
                {
                    intermediate = [];
                    unarray(resultValue[index][j], intermediate);
                    resultValue[index][j] = intermediate;
                }
    });

    // unarray one last time, because earlier we put stuff in an array
    let finalValue = []; // final answer
    Object.values(resultValue).forEach ((element) => {
        unarray(element, finalValue);
    });

    return finalValue;
};