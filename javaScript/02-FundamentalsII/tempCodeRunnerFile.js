function rFib(input){
    if(input <= 2){
        return 1
    }
    return rFib(input - 1) + rFib(input - 2)
}
console.log(rFib(7))