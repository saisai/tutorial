let ranks = ['A', 'B', 'C'];


for(let i=0; i < ranks.length; i++) {
    console.log(ranks[i]);
}


ranks.forEach(function(e) {
    console.log(e);
});


ranks.forEach((e) => console.log(e));

function Counter() {
    this.count = 0;
    let self =this;
    return {
        increase: function() {
            self.count++;
        },
        current: function() {
            return self.count;
        },
        reset: function() {
            self.coutn = 0;
        }

    }
}

var counter = new Counter();

var numbers = [1, 2, 3];

var sum = 0;

numbers.forEach(function(e) {
    sum += e;
    this.increase();

}, counter);

console.log(sum);
console.log(counter.current());
