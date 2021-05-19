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
    for(var i = 1; i <= 100; i++){
        if(i % 10 == 0){
            console.log("Coding Dojo");
        }
        else if(i % 5 == 0){
            console.log("Coding");
        }
        else{
            console.log(i);
        }
    }
}
//ninjaCounting();

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

//Your function will be given an input parameter incoming. Please console.log this value.
function printParameter(input){
    console.log(input);
}
var someThing = "Hello World";
//printParameter(someThing);

//Print integers from 2000 to 5280, using a WHILE.
function printWhile(){
    var num = 2000
    while (num <= 5280) {
        console.log(num);
        num++;
    }
}
//printWhile();

//Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?
function largeNum(){
    var i = 1;
    var sum = 0;
    while(i <= 299999){
        sum += i;
        i += 2;
    }
    console.log(sum*2);
}
//largeNum();

//If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day...."
function specialDay(num1, num2){
    if(num1 == 12 || num1 == 21 && num2 == 12 || num2 == 21){
        console.log("How did you know?")
    }else{
        console.log("Just another day...");
    }
}
specialDay(12, 10);

//Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
function fourDown(){
    var i = 2016;
    while(i > 0){
        console.log(i);
        i -= 4;
    }
}
//fourDown();

//Based on earlier fourDown(), given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines).
function flexibleCountdown(max, min, mult){
    for(var i = max; i > min; i -= mult){
        console.log(i);
    }
}
//flexibleCountdown(9,2,3);

//Write a function that determines whether a given year is a leap year. If a year is divisible by four, it is a leap year, unless it is divisible by 100. However, if it is divisible by 400, then it is.
function leapyear(input){
    if(input % 4 ==0){
        if(input % 100 == 0){
            if(input % 400 == 0){
                console.log("Special Leap Year.")
            }else{
                console.log("Not a Leap Year.")
            }
        }else{
            console.log("Leap Year.")
        }
    }else{
        console.log("Not a Leap Year.")
    }
}
var year = 2020;
//leapyear(year);

//This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) it. Do this using a WHILE. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, and excluding the value 9).
function finalCountdown(mult, from, to, except){
    var i = from;
    while(i <= to){
        if(i % mult == 0){
            if(i == except){
                i ++;
                continue
            }
            console.log(i);
        }
        i ++;
    }
}
//finalCountdown(3,5,17,9);

