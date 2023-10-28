function sumArray(arr) {
    return arr.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  }
  
  /**
   * @param {number[]} nums
   * @return {void}
   */
  var ArrayWrapper = function(nums) {
      this.store = nums;
  };
  
  /**
   * @return {number}
   */
  ArrayWrapper.prototype.valueOf = function() {
      return sumArray(this.store);
  }
  
  /**
   * @return {string}
   */
  ArrayWrapper.prototype.toString = function() {
      return '[' + String(this.store) + ']';
  }
  
  /**
   * const obj1 = new ArrayWrapper([1,2]);
   * const obj2 = new ArrayWrapper([3,4]);
   * obj1 + obj2; // 10
   * String(obj1); // "[1,2]"
   * String(obj2); // "[3,4]"
   */