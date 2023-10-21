/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    let intermediate = 0;
    
	return function(x) {
        if (functions.length === 0) return x; // trivial case

        // apply the functions in reverse order, note that index 0 now holds the last fn
        for (i in functions.reverse()) {
            // ensure the first time `x` is the input, after that use the previous return value
            // Note: object keys are treated as strings in JavaScript, even if they represent
            // numeric indices, so `Number` or `parseInt` have to called
            intermediate = (Number(i) === 0) ? functions[0](x) : functions[i](intermediate);
        }

        return intermediate;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */