// 2.1 & 2.2
function threesFives(start, end){
    var sum = 0;
    for(var i = start; i <= end; i++){
        if(i % 3 == 0 || i % 5 == 0){
            if(i % 3 == 0 && i % 5 == 0){
                continue
            }
            // console.log(i);
            sum += i;
        }
    }
    return sum;
}

// console.log("Total: "+threesFives(0,30));

// 3.1
function makingCents(input){
    if(input > 100) {
        dl = input/100;
        console.log("Dollars: "+dl);
        input -= (dl*100)
    }
    return input
}
console.log(makingCents(297));