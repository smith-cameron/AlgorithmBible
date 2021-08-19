'use strict';
//1
function arrayCountdown(input){
    var newArray = [];
    for(var i = input; i >= 0; i--){
        newArray.push(i);
    }
    console.log("My Array is "+newArray.length+" indices long.");
    return newArray;
}
//console.log(arrayCountdown(4));

//2
function printAndReturn(input){
    console.log("Printing: "+input[0]);
    return input[1];
}
//console.log("Returning: "+printAndReturn([32, 44]));

//3
function sumStuff(input){
    return input[0]+input.length;
}
console.log(sumStuff([true, 44]));
// true evaluates as 1+ length
// false evaluates as 0+ length

//4
function return2(input){
    return input[0]+input.length
}
console.log(return2(["what?", 44]));
// string concatonates

//5
// ???

//6
function greaterThan(input, minIndex){
    var sum = 0;
    for(var i = 0; i < input.length; i++){
        if(input[i] > input[minIndex]){
            console.log(input[i]);
            sum += 1;
        }
    }
    return sum;
}
// console.log("Total values greater than "+[1,3,5,7,9,13][1]+" : "+greaterThan([1,3,5,7,9,13], 1));

//7
function greaterThanAny(input, index){
    if(input.length <=1){
        return "need more values than one.";
    }
    var sum = 0;
    for(var i = 0; i < input.length; i++){
        if(input[i] > input[index]){
            console.log(input[i]);
            sum += 1;
        }
    }
    return sum;
}
//console.log("Total values greater than "+[1,3,5,7,9,13][1]+" : "+greaterThanAny([1,3,5,7,9,13], 1));

//8
function thisAndThat(num1, num2){
    if(num1 == num2){
        return "Jinx!";
    }
    var newArray = [];
    for(var i = 0; i <= num1; i++){
        newArray.push(num2);
    }
    return newArray;
}
//console.log(thisAndThat(5, 5));

//9
function goldielocks(input){
    if(input[0] > input.length){
        return "Too big!";
    }
    else if(input[0] < input.length){
        return "Too small!";
    }
    else{
        return "Just right!";
    }
}
//console.log(goldielocks([4,2,3,4]));

//10
function fahrenheitToCelsius(fDegrees){
    var celsius = (fDegrees - 32) / (9/5);
    return celsius;
}
//console.log(fahrenheitToCelsius(14));

//11
function celsiusToFahrenheit(cDegrees){
    var fahrenheit = (9/5 * cDegrees) + 32;
    return fahrenheit;
}
//console.log(celsiusToFahrenheit(-10));