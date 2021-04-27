'use strict';
//Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?
function arrayCountdown(input){
    var newArray = [];
    for(var i = input; i >= 0; i--){
        newArray.push(i);
    }
    console.log("My Array is "+newArray.length+" indices long.");
    return newArray;
}
var digets = 4;
//console.log(arrayCountdown(digets));

//Your function will receive an array with two numbers. Print the first value, and return the second.
function printAndReturn(input){
    console.log("Printing: "+input[0]);
    return input[1];
}
var arrayOfTwo = [32, 44];
//console.log("Returning: "+printAndReturn(arrayOfTwo));

//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).
//A string of a number "32" or a word "what?" appended the length. return was 322 for ["32", 44] and what?2 for ["what?", 44]
//A boolean value [false, 44] returned only the length. [false, 44] returned the length plus one as 3.
function firstPlusLength(input){
    return input[0]+input.length;
}
var firstPLArray = [true, 44];
//console.log(firstPlusLength(firstPLArray));

//For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.
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
var index = 1;
var greaterThanArray = [1,3,5,7,9,13];
//console.log("Total values greater than "+greaterThanArray[index]+" : "+greaterThan(greaterThanArray, index));

//Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?
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
//console.log("Total values greater than "+greaterThanArray[index]+" : "+greaterThanAny(greaterThanArray, index));

//Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.
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
var that = 5;
var that2 = 5;
//console.log(thisAndThat(that, that2));

//Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".
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
var glArr = [4,2,3,4];
//console.log(goldielocks(glArr));

//Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.
function fahrenheitToCelsius(fDegrees){
    var celsius = (fDegrees - 32) / (9/5);
    return celsius;
}
var fDegrees = 14;
//console.log(fahrenheitToCelsius(fDegrees));

//Create celsiusToFahrenheit(cDegrees) that accepts number of degrees Celsius, and returns the equivalent temperature expressed in Fahrenheit degrees. (optional) Do Fahrenheit and Celsius values equate at a certain number? Scientific calculation can be complex, so for this challenge just try a series of Celsius integer values starting at 200, going downward (descending), checking whether it is equal to the corresponding Fahrenheit value.
function celsiusToFahrenheit(cDegrees){
    var fahrenheit = (9/5 * cDegrees) + 32;
    return fahrenheit;
}
var cDegrees = -10;
//console.log(celsiusToFahrenheit(cDegrees));