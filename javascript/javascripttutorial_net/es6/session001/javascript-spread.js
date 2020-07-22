const odd = [1, 3, 5];
const combined = [2, 4, 5, ...odd];
console.log(combined);


function compare(a, b) {
    return a - b;
}

var result = compare.apply(null, [1, 3]);
console.log(result);

