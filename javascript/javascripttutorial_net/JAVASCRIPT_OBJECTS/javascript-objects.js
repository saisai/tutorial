let website = {
    title: 'JavaScript Tutorial',
    url: 'https://www.javascripttutorial.net',
    tags: ['es6', 'javascript', 'node.js']
};

for(const key in website) {
    console.log(website[key]);


}


let person = {
    firstName: "John",
    lastName: "Doe"
};

person.greet = function() {
    console.log("Hello world");
}

person.greet();


let person2 = {
    firstName: "John",
    lastName: "Doe",
    greet() {

        console.log("Hello world");
    },

    getFullName: function() {
        return this.firstName + " " + this.lastName;
    },

    get() {
        return this;
    }
};

person2.greet();
console.log(person2.getFullName());
console.log(person2.get());
console.log(person2.get().firstName);
console.log(person2.get().get().getFullName());
