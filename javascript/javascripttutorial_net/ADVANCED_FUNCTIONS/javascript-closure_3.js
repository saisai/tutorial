function greeting() {
    let message = "Hi";

    function sayHi() {
        console.log(message);
    }

    sayHi();
}

greeting();



for(let i = 1; i <=3; i++) {


    setTimeout(function() {
        console.log("after " + i + " Second(s): " + i);
    }, i * 1000);
}

