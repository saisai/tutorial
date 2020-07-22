let scores = [80, 90, 70];

for(let score of scores) {
    score = score + 5;
    console.log(score);
}


let str = 'abcd';

for(let c of str) {
    console.log(c);
}

var colors = new Map();
colors.set('red', '#ff0000');
colors.set('green', '#00ff00');
colors.set('blue', '#0000ff');

for (let color of colors) {
    console.log(color);
}

let nums = new Set([1, 2, 3]);

for (let num of nums) {
    console.log(num); //
}
