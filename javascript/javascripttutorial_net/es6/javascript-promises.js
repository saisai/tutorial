function makePromise(completed) {
    return new Promise(function( resolve, reject ){
        setTimeout(() => {
            if(completed) {
                resolve("I have completed learning js.");
            } else {
                reject("I haven't completed learning JS yet.")
            }
        }, 3 * 1000);
    })
}

let learnJS = makePromise(true);

learnJS.then(
    success => console.log(success),
    reason => console.log(reason)
);


learnJS.then(
    value => console.log(value)
);


let masterJS = makePromise(false);

masterJS.then(
    undefined,
    reason => console.log(reason)
);


learnJS.catch(
    reason => console.log(reason)
)
