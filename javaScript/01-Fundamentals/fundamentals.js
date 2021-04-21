'use strict';
//Set myNumber to 42. Set myName to your name.
var myNumber = 42;
var myName = 'Cameron';
var temp;
//Now swap myNumber into myName & vice versa.
function swapMyNameNum(){
    temp = myName;
    myName = myNumber;
    myNumber = temp;
    console.log('myName: '+myName);
    console.log('myNumber:'+myNumber);
}
//swapMyNameNum();

//Print integers from -52 to 1066 using a FOR loop.
function printInt(){
    for(var i = -52; i <= 1066; i++){
        console.log(i);
    }
}
//printInt();

//Print all integer multiples of 5, from 512 to 4096. Afterward, also log how many there were.
function printAndCount(){
    var count = 0;
    for(var i = 512; i <=4096; i++){
        if(i % 5 == 0){
            console.log(i);
            count += 1;
        }
    }
    return count;
}
//console.log(printAndCount());

//Print multiples of 6 up to 60,000, using a WHILE
function multiplesOf6(){
    var i = 0;
    while(i <= 60000){
        console.log(i);
        i += 6;
    }
}
//multiplesOf6();

//Create beCheerful(). Within it, console.log string "good morning!" Call it 98 times.
function beCheerful(){
    var greeting = 'good morning!'
    for(var i = 1; i <= 98; i++){
        console.log(i+":"+greeting);
    }
}
//beCheerful();

//Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
function ninjaCounting(){
    
}

//Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
function multiplesOf3(){
    for(var i = -300; i <= 0; i+=3){
        if(i == -6 || i == -3){
            continue;
        }
        console.log(i);
    }
}
//multiplesOf3();

//Print integers from 2000 to 5280, using a WHILE.
function printWhile(){
    var num = 2000
    while (num <= 5280) {
        console.log(num);
        num++;
    }
}
//printWhile();

//If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...."
function specialDay(num1, num2){
    if(num1 == 12 || num1 == 21 && num2 == 12 || num2 == 21){
        console.log("How did you know?")
    }else{
        console.log("Just another day...");
    }
}
//specialDay(21, 10);
