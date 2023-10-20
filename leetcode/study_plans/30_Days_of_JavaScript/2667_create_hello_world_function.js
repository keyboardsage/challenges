/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        let hello = "Hello World";
        return hello;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */