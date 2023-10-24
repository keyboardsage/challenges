var TimeLimitedCache = function() {
    this.data = {}; // using an object/dictionary as a cache
  };
  
  /** 
   * @param {number} key
   * @param {number} value
   * @param {number} duration time until expiration in ms
   * @return {boolean} if un-expired key already existed
   */
  TimeLimitedCache.prototype.set = function(key, value, duration) {
    // does the key already exist?
    let returnVal = (JSON.stringify(key) in this.data) ? true : false;
    
    // function for setting a time limit on how long it will stay
    let fnRemoveKey = () => delete this.data[JSON.stringify(key)];
  
    // add/overwrite it
    if (returnVal) clearTimeout(this.data[JSON.stringify(key)].timer);
    this.data[JSON.stringify(key)] = {value, timer: setTimeout(fnRemoveKey, duration)};
  
    // return a boolean indicating if it already existed
    return returnVal;
  };
  
  /** 
   * @param {number} key
   * @return {number} value associated with key
   */
  TimeLimitedCache.prototype.get = function(key) {
    return (JSON.stringify(key) in this.data) ? this.data[JSON.stringify(key)].value : -1;
  };
  
  /** 
   * @return {number} count of non-expired keys
   */
  TimeLimitedCache.prototype.count = function() {
    return Object.keys(this.data).length;
  };
  
  /**
   * const timeLimitedCache = new TimeLimitedCache()
   * timeLimitedCache.set(1, 42, 1000); // false
   * timeLimitedCache.get(1) // 42
   * timeLimitedCache.count() // 1
   */