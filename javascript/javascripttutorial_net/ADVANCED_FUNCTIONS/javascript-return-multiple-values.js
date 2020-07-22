function getNames() {
    // get names from the database or API
    let firstName = 'John',
        lastName = 'Doe';

    // return as an array
    return [firstName, lastName];
}

let names = getNames();
console.log(names[0]);
console.log(names[1]);


const [firstNames, lastNames] = getNames();

console.log(firstNames);
console.log(lastNames);


function getNamesObj() {
    // get names from the database or API
    let firstName = "John",
        lastName = "Doe";


    // return values


    return {
        firstName,
        lastName
    };
}

let objnames = getNamesObj();
console.log(objnames.firstName);
console.log(objnames.lastName);

let { firstName, lastName } = getNamesObj();
console.log('test ' + firstName);
console.log(lastName);

