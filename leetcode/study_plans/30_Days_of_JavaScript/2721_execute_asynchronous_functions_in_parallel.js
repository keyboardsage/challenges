/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
  

    return await new Promise ((resolve, reject) => {
      let count = 0;
      let finalArr = Array(functions.length);
      
      const results = functions.map((fn, index) => {
        fn()
          .then((value) => {
            finalArr[index] = value;
  
            count++;
            if (count == functions.length) resolve(finalArr);
          })
          .catch((error) => reject(error));
      });
    });
  };
  
  /**
   * const promise = promiseAll([() => new Promise(res => res(42))])
   * promise.then(console.log); // [42]
   */