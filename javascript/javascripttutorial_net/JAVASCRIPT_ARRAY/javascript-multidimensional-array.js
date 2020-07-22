let activities = [
    ['Work', 9],
    ['Eat', 1],
    ['Commute', 2],
    ['Play Game', 1],
    ['Sleep', 7]
];

activities.push(['Study', 2]);
activities.splice(1, 0, ["Programming", 2]);
console.log(activities);

activities.forEach(activity => {
    let precentage = ((activity[1]/24) * 100).toFixed();
    activity[2] = precentage + '%';
})

console.log(activities);

activities.pop();
console.log(activities);

activities.forEach((activity) => {
    activity.pop(2);
});
console.log(activities);


for(let i=0; i < activities.length; i++) {
    // get the size of the inner array
    var innerArrayLength = activities[i].length;

    // loop the inner array
    for(let j=0; j < innerArrayLength; j++) {
        console.log('[' + i + ',' + j + ' ] =' + activities[i][j]);
    }
}


activities.forEach( (activity) => {
    activity.forEach ((data) => {
        console.log(data);
    });
});
