'use strict';

var obj = {
    a: 10
};

 Object.defineProperty(obj, 'b', {
    get: () => {
        console.log(this.a, typeof this.a, this);
        return this.a + 10;
    }
});




