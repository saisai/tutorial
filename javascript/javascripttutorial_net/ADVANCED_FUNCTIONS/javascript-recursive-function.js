function countDown(fromNumber) {
    console.log(fromNumber);

    let nextNumber = fromNumber - 1;

    if(nextNumber > 0) {
        countDown(nextNumber);
    }
}


countDown(3);


let newYearCountDown = countDown;


countDown = null;

newYearCountDown(10);

