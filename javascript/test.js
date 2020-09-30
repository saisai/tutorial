
let test = {};

test['1'] = 1;
test[2] = 2;
//console.log(test);

for(var prop in test) {
    console.log(prop, test[prop]);
}
