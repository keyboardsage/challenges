/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let cache = {};
    let inputAsString = undefined;

    return function(...args) {
        // if already known, look it up
        inputAsString = JSON.stringify(args);
        if (inputAsString in cache) return cache[inputAsString];

        // otherwise, process it
        cache[inputAsString] = fn(...args);

        return cache[inputAsString];
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */