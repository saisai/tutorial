var scores = [10, 20, 30, 10, 40, 20];

console.log(scores.indexOf(10)); // 0
console.log(scores.indexOf(30)); // 2
console.log(scores.indexOf(50)); // -1
console.log(scores.indexOf(20)); // 1

console.log(scores.indexOf(20,-1)); // 5 (fromIndex = 6+ (-1) = 5)
console.log(scores.indexOf(20,-5)); // 1 (fromIndex = 6+ (-5) = 1)

var guests = [
    {name: 'John Doe', age: 30},
    {name: 'Lily Bush', age: 20},
    {name: 'William Gate', age: 25}
];

console.log(guests.indexOf({
    name: 'John Doe',
    age: 30
})); // -1


function find(needle, haystack) {
    var results = [];
    var idx = haystack.indexOf(needle);
    while (idx != -1) {
        results.push(idx);
        idx = haystack.indexOf(needle, idx + 1);
    }
    return results;
}

console.log(find(10,scores)); // [0, 3]

console.log(scores.lastIndexOf(10));// 3
console.log(scores.lastIndexOf(20));// 5

