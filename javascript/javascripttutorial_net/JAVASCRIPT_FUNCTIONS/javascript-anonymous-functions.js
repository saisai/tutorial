let show = function() {
    console.log("Anonymous function");
};

show();


setTimeout(function() {

    console.log('Execute later after 1 second');
}, 1000);


(function() {
    console.log('IIFE');
})();

let person = {
    firstName: 'John',
    lastName: 'Doe'
};

(function() {
    console.log(`${person.firstName} ${person.lastName}`);
})(person);


( () => console.log(`${person.firstName} ${person.lastName}`) )(person);

let showa = () => console.log('Anonymous function');

showa();
