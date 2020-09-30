let circles = [
    10, 30, 50
];

let areas = [];
let area = 0;
for(let i=0; i < circles.length; i++) {
    area = Math.floor(Math.PI * circles[i] * circles[i]);
    areas.push(area);
}

console.log(areas);

function circleArea(radius) {
    return Math.floor(Math.PI * radius * radius);
}

let areass = circles.map(circleArea);
console.log(areass);

let areasAnon = circles.map(function(radius) {
    return Math.floor(Math.PI * radius * radius);
});

console.log(areasAnon);

let areas_arrow = circles.map( radius => Math.floor(Math.PI * radius * radius) );

console.log(areas_arrow);

let numbers = [16, 25, 36];

let results = numbers.map(Math.sqrt);

console.log(results);
