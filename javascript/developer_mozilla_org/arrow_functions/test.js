const materials = [
    "Hydrogen",
    "Helinum",
    "Lithuium",
    "Beryllium"
]

console.log(materials.map(material => material.length));


var elements = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium'
];

results = elements.map(function (element){
    return element.length;
});
console.log(results);


results2 = elements.map(element => {
    return element.length;
});

console.log(results2);

console.log(elements.map(element => element.length));

console.log(elements.map(({ length: lengthFooBArX }) => lengthFooBArX));

console.log(elements.map(( { length }) => length))


var adder = {

    base: 1,

    add: function(a) {
        var f = v => v + this.base;
        return f(a);
    },

    addThruCall: function(a) {
        var f = v => v + this.base;
        var b = {
            base: 2
        };

        return f.call(b, a);
    }
};

console.log(adder.add(1)); // this would log 2
console.log(adder.addThruCall(1)); // this would log 2 still
