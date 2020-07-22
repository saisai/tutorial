let person = {
    name: "John Doe",
    getName: function() {
        console.log(this.name);
    }
};

setTimeout(person.getName, 1000);

let f = person.getName;
setTimeout(f, 1000);


setTimeout(function() {
    person.getName();
}, 1000);


let g = person.getName.bind(person);
setTimeout(g, 1000);

let runner = {
    name: 'Runner',
    run: function(speed) {
        console.log(this.name + ' runs at ' + speed + ' mph.');
    }
};


let flyer = {
    name: 'Flyer',
    fly: function(speed) {
        console.log(this.name + ' flies at ' + speed + ' mph.');
    }
};

let run = runner.run.bind(flyer, 20);
run();

