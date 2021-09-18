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

console.log("Total: "+threesFives(0,30));