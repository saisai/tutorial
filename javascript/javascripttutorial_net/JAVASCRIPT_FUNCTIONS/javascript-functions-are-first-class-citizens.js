function add(a, b) {
    return a + b;
}


let sum = add;

console.log(sum);
console.log(add);

console.log(sum(1, 3));
console.log(add(3, 4));


function average(a, b, fn) {
    return fn(a, b) / 2;
}


console.log(average(10, 20, sum));

function compareBy(propName) {
    return function (a, b) {
        let x = a[propName],
            y = b[propName];

        if (x > y) {
            return 1;
        } else if (x < y) {
            return -1
        } else {
            return 0;
        }
    }
}

let products = [
    {name: 'iPhone', price: 900},
    {name: 'Samsung Galaxy', price: 850},
    {name: 'Sony Xperia', price: 700}
];

console.log('Products sorted by name:');
console.table(products);
products.sort(compareBy('name'));

console.table(products);

