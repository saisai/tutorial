let cities = [
    {name: 'Los Angeles', population: 3792621},
    {name: 'New York', population: 8175133},
    {name: 'Chicago', population: 2695598},
    {name: 'Houston', population: 2099451},
    {name: 'Philadelphia', population: 1526006}
];

let bigCities = [];

for(let i = 0; i < cities.length; i++) {
    if(cities[i].population > 3000000) {
        bigCities.push(cities[i]);
    }
}

console.log(bigCities);


let bigCi = cities.filter(function(e) {
    return e.population > 3000000;
});

console.log(bigCi);

let bigA = cities.filter( city => city.population > 3000000 );

console.log(bigA);


cities
    .filter(city => city.population < 3000000)
    .sort((c1, c2) => c1.population - c2.population)
    .map(city => console.log(city.name + ':' + city.population));


function isInRange(value) {

    if(typeof value !== 'number') {
        return false;
    }
    return value >= this.lower && value <= this.upper;
}


let data = [10, 20, "30", 1, 5, 'JavaScript filter', undefined, 'example'];

let range = {
    lower: 1,
    upper: 10
};

let numberInRange = data.filter(isInRange, range);

console.log(numberInRange);
