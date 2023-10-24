/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    // appraoch 1: concurrent resolving
    const [answer1, answer2] = await Promise.all([promise1, promise2]);
    return answer1 + answer2;

    // approach 2: sequential resolving
    //return (await promise1) + (await promise2);
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */