'use strict';
// 1
var myNumber = 42;
var myName = 'Cameron';
var temp;
// 2
function swapMyNameNum(){
    temp = myName;
    myName = myNumber;
    myNumber = temp;
    console.log('myName: '+myName);
    console.log('myNumber:'+myNumber);
}
//swapMyNameNum();

// 3
function printInt(){
    for(var i = -52; i <= 1066; i++){
        console.log(i);
    }
}
//printInt();

// 4
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

// 5
function multiplesOf6(){
    var i = 0;
    while(i <= 60000){
        console.log(i);
        i += 6;
    }
}
//multiplesOf6();

// 6
function beCheerful(){
    var greeting = 'good morning!'
    for(var i = 1; i <= 98; i++){
        console.log(i+":"+greeting);
    }
}
//beCheerful();

// 7
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

// 8
function multiplesOf3(){
    for(var i = -300; i <= 0; i+=3){
        if(i == -6 || i == -3){
            continue;
        }
        console.log(i);
    }
}
//multiplesOf3();

// 9
function printParameter(input){
    console.log(input);
}
//printParameter("Hello World");

// 10
function printWhile(){
    var num = 2000
    while (num <= 5280) {
        console.log(num);
        num++;
    }
}
//printWhile();

// 11
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

// 12
function specialDay(num1, num2){
    if(num1 == 12 || num1 == 21 && num2 == 12 || num2 == 21){
        console.log("How did you know?")
    }else{
        console.log("Just another day...");
    }
}
specialDay(12, 10);

// 13
function fourDown(){
    var i = 2016;
    while(i > 0){
        console.log(i);
        i -= 4;
    }
}
//fourDown();

// 14
function flexibleCountdown(max, min, mult){
    for(var i = max; i > min; i -= mult){
        console.log(i);
    }
}
//flexibleCountdown(9,2,3);

// 15
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
//leapyear(2020);

// 16
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
