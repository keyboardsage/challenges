class EventEmitter {
    constructor() {
        this.stack = []; // stack from array
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
	subscribe(eventName, callback) {
      	this.stack.push({the_name: eventName, the_callback: callback});
        
		return {
			unsubscribe: () => {
                // search for the object's position
                const searchObject = {the_name: eventName, the_callback: callback};
                const positionToRemove = this.stack.findIndex(theObj => theObj.the_name === searchObject.the_name && theObj.the_callback === searchObject.the_callback);
                
                // remove it
				if (positionToRemove !== -1) this.stack.splice(positionToRemove, 1);
			}
		};
	}
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
	emit(eventName, args = []) {
        let callbacks = [];
		
        for(const index in this.stack)
            if (this.stack[index].the_name === eventName)
                callbacks.push(this.stack[index].the_callback(...args));
        
        return callbacks;
	}
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */