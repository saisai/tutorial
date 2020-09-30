const  KadaneAlgo = (array) => {

    let cummulativeSum = 0
    let maxSum = 0
    for(let i=0; i < array.length; i++){
        cummulativeSum += array[i]
        if(cummulativeSum < 0){
            cummulativeSum = 0
        }else if(maxSum < cummulativeSum){
            maxSum = cummulativeSum
        }
    }
    return maxSum


}

const main = () =>{
    let myArray=[1,2,3,4,-6]
    let result = KadaneAlgo(myArray)
    console.log(result)
}

main()

