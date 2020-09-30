const SieveOfEratosthenes = n => {

    const primes = new Array(n + 1)
    primes.fill(true) // set all as true initially
    primes[0] = primes[1] = false // handling case for 0 and 1
    const sqrtn = Math.ceil(Math.sqrt(n))
    for(let i = 2; i <= sqrtn; i++) {
        console.log('sqrtn =>', sqrtn)
        if(primes[i]){
            for(let j = 2 * i; j <=n ; j += i) {
                primes[j] = false
             }
         }
     }

    return primes

}

function main() {
    const n = 69 // number till where we wish to find primes
    const primes = SieveOfEratosthenes(n)
    for(let i = 2; i <= n; i++){
        if(primes[i]){
            console.log(i)
        }
    }
    // console.log(primes)
 }


main()

//https://github.com/TheAlgorithms/Javascript/blob/master/Dynamic-Programming/SieveOfEratosthenes.js
