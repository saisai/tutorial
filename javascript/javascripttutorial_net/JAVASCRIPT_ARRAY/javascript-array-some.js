let marks = [ 4, 5, 7, 9, 10, 3 ];


let lessThanFive = false;

for(let index = 0; index < marks.length; index++) {
    if(marks[index] < 5) {
        lessThanFive = true;
        break;
    }
}

console.log(lessThanFive);


let lessThanFiveb = marks.some(function(e){
    return e < 5;
});

console.log(lessThanFiveb);


let lessThanFivea = marks.some( e => e < 5 );

console.log(lessThanFivea);

function exists(value, array) {
    return array.some(e => e === value);
}

let markss = [4, 5, 7, 9, 10, 2];

console.log(exists(4, markss));
console.log(exists(11, markss));

let afunc = function(value, array) {
    //console.log(value);
    return array.some(e => e === value);
}

console.log(markss);
let afuncc = afunc;

console.log(afuncc(4, markss));
console.log(afuncc(19, markss));


let dd = [2, 3, 4]
let afun = (value, array) => (array.some( e => e === value ));

let aa = afun
console.log(aa(2, dd));
console.log(aa(5, dd));
console.log(afun(3, dd));
console.log(afunc(3, markss));
console.log(afunc(4, markss));

let marksa = [4, 5, 7, 9, 10, 2];

const range = {
    min: 8,
    max: 10

};

let rr = marksa.some(function(e) {
    return e >= this.min && e <= this.max;
}, range);

console.log(rr);
// not working for this kind of arrow function
let rra = marksa.some( (e) => { e >= this.min && e <= this.max }, range );

console.log(rra);

