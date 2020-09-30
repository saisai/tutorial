let re = /hi/i;

let result = re.test('hi john');

console.log(result);


let message = "Hi, are you there? hi, HI...";
let ree = /hi/gi;

let matches = [];

while((match = ree.exec(message)) != null) {
    matches.push(match);
}

console.dir(matches);


let str = "Are you ok? Yes, I'm OK";

let result1 = str.match(/OK/gi);
console.log(result1);


let str1 = "Are you OK/ Yes, I'm OK.";
let result2 = str.replace('OK', 'fine');
console.log(result2);



let str2 = "Are you ok? yes, I'm ok";
let result3 = str2.replace(/OK/g, 'fine');
console.log(result3);

