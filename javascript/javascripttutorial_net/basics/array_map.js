let circles = [
    10, 30, 50
];

let areas = [];
let area = 0;
for(let i = 0; i < circles.length; i++) {
    area = Math.floor(Math.PI * circles[i] * circles[i]);
    areas.push(area);
}

console.log(areas);

function circleArea(radius) {
    return Math.floor(Math.PI * radius * radius);
}

let areass = circles.map(circleArea);
console.log(areass);

let areas3 = circles.map(function(radius) {
    return Math.floor(Math.PI * radius * radius);
});

console.log(areas3);

let areas4 = circles.map(radius => Math.floor(Math.PI * radius * radius));
console.log(areas4);
