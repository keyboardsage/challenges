/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    let start = Date.now;

	return async function(...args) {
        let fnUserPromise = fn(...args); // user's function

        let fnTimeoutPromise = new Promise ( (resolve, reject) => { // time limit reached function
            setTimeout(() => { reject("Time Limit Exceeded") }, t)
        });

        return Promise.race([fnUserPromise, fnTimeoutPromise]); // first one to resolve, returns
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */