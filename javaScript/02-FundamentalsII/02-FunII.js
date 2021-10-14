// 2.1 & 2.2
function threesFives(start, end){
    var sum = 0;
    for(var i = start; i <= end; i++){
        if(i % 3 == 0 || i % 5 == 0){
            if(i % 3 == 0 && i % 5 == 0){
                continue
            }
            console.log(i);
            sum += i;
        }
    }
    return sum;
}

// console.log("Total: "+threesFives(0,30));

// 3.1
function makingCents(input){
    if(input >= 100) {
        console.log("Dollars: "+Math.floor(input/100));
        input -= (Math.floor(input/100)*100)
    }
    if(input >= 50) {
        console.log("Half-Dollar: "+Math.floor(input/50));
        input -= (Math.floor(input/50)*50)
    }
    if(input >= 25) {
        console.log("Quarters: "+Math.floor(input/25));
        input -= (Math.floor(input/25)*25)
    }
    if(input >= 10) {
        console.log("Dimes: "+Math.floor(input/10));
        input -= (Math.floor(input/10)*10)
    }
    if(input >= 5) {
        console.log("Nickles: "+Math.floor(input/5));
        input -= (Math.floor(input/5)*5)
    }
    if(input >= 1) {
        console.log("Pennies: "+Math.floor(input/1));
        input -= (Math.floor(input/1)*1)
    }
    return input
}
console.log(makingCents(15));

function mathMashUp(bound){
    var sum = 0;
    for(var i = 1; i <= bound; i++){
        console.log(i)
        if (i == (bound % 3 == 0)){
            return -1
        }
        if(i % 7 == 0 ){
            console.log("adding twice")
            sum += (i*2);
            continue
        }
        if(i % 3 == 0 ){
            console.log("skipping")
            continue
        }
        else{
            sum += i;
        }
    }
    return sum;
}
// console.log(mathMashUp(8));

function twelveBarBlues(){  
    for(var i = 1; i <= 12; i++){
        console.log(i)
        console.log("chick boom chick")
    }
}

// twelveBarBlues();

