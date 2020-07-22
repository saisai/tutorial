class Sequence{
    constructor(start=0, end=Infinity, interval=1) {
        this.start= start;
        this.end= end;
        this.interval = interval;
    }

    [Symbol.iterator]() {
        let counter = 0;
        let nextIndex = this.start;
        return {
            next:() => {
                if(nextIndex <= this.end) {
                    let result = {value: nextIndex, done:false}
                    nextIndex += this.interval;
                    counter++;
                    return result;
                }
                return {value: counter, done:true}
            }
        }
    }
}

let evenNumbers = new Sequence(2, 10, 2);
for(const num of evenNumbers) {
    console.log(num);
}
