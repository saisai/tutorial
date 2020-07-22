let countDown = function f(fromNumber) {
    console.log(fromNumber);

    let nextNumber = fromNumber - 1;

    if(nextNumber > 0) {
        f(nextNumber);
    }
};


countDown(3);

let newYearCountDown = countDown;

countDown = null;

newYearCountDown(10);


function sumOfDigits(num) {
    if(num == 0) {
        return 0;
    }

    return num % 10 + sumOfDigits(Math.floor(num / 10));
}

console.log(sumOfDigits(324));
