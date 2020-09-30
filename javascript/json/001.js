var json_text = '{"name":"John", "birth":"1986-12-14", "city":"New York"}';

var obj = JSON.parse(json_text, function(key, value){
    if (key == "birth"){

        return new Date(value);
    } else {
        return value;

    }

});

console.log(obj.name +", " + obj.birth);


var obja = JSON.parse(json_text, (key, value) =>
    ((key == "birth") ? new Date(value) : value)
)

console.log(obja.name + ", " + obj.birth);

myObj = { "name":"John", "age":30, "car":null };

for (let x in myObj){
    console.log(myObj[x]);
}



