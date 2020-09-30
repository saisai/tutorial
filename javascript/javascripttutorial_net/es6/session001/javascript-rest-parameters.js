function sum(...args) {
    let total = 0;
    for(const a of args) {
        total += a;
    }
    return total;
}

console.log(sum(1, 2, 3));


function sum2(...args) {
    return args.filter(e => typeof e === 'number')
    .reduce((prev, curr)=> prev + curr);
}

let result = sum2(10, "Hi", null, undefined, 20);
console.log(result);

