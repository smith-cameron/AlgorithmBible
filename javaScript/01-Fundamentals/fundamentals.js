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
//specialDay(21, 10);

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
var year = 2000;
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
    var celsius = (fDegrees- 32) / (9/5);
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

//Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].
function biggieSize(input){
    for(var i = 0; i < input.length; i++){
        if(input[i] > 0){
            input[i] = "big";
        }
    }
    return input;
}
var biggieArray = [-1,3,5,-5];
//console.log(biggieSize(biggieArray));

//You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.
function previeousLengths(input){
    for(var i = input.length-1; i >= 0 ; i--){
        if(i == 0){
            input[i] = 0;
            return input;
        }
        input[i] = input[i-1].length;
    }
    return input;
}
var plStrings = ["boo3", "haha", "gotchya", "kiddo"];
//console.log(previeousLengths(plStrings));

//Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.
function printLowReturnHigh(input){
    var min = input[0];
    var max = input[0];
    for(var i = 0; i < input.length; i++){
        if(input[i] < min)
            min = input[i];
        if(input[i] > max)
            max = input[i];
    }
    console.log(min);
    return max;
}
var pLrHArray = [-34,5,-5,24,14];
//console.log(printLowReturnHigh(pLrHArray));

//Build function that accepts array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.
function addSeven(input){
    var newArray = [];
    for(var i = 1; i < input.length; i++){
        newArray.push(input[i]+7);
    }
    return newArray;
}
var add7Array = [2,1,3,4];
//console.log(addSeven(add7Array));

//Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.
function printAndReturn(input){
    console.log(input[input.length-2]);
    for(var i = 0; i < input.length; i++){
        if(input[i] % 2 != 0){
            return input[i];
        }
    }
}
var pAndRArray = [1,14,3,4];
//console.log(printAndReturn(pAndRArray));

//Given array, write a function to reverse values, in-place. Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].
function reverseArray(input){
    if(input.length < 2){
        return input;
    }
    for(var i = 0; i < input.length/2; i++){
        var temp = input[i];
        input[i] = input[input.length-1-i];
        input[input.length-1-i] = temp;
    }
    return input;
}
var reverseArayArray = [1,2,3,4,5,6];
//console.log(reverseArray(reverseArayArray));

//Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.
function doubleVision(input){
    var newArray = [];
    for(var i = 0; i < input.length; i++){
        newArray.push(input[i]*2);
    }
    return newArray;
}
var dVisionArray = [2,3,4,5];
//console.log(doubleVision(dVisionArray));

//Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].
function negativeOutlook(input){
    var newArray = [];
    for(var i = 0; i < input.length; i++){
        if(input[i] > 0){
            newArray.push(input[i]*(-1));
        }
        else if(input[i] <= 0){
            newArray.push(input[i]);
        }
    }
    return newArray;
}
var negOutArray = [12,3,-5];
//console.log(negativeOutlook(negOutArray));

//Given array of numbers, create function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
function endPositive(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            sum += 1;
        }
    }
    arr[arr.length-1] = sum;
    return arr;
}
var endPosArray = [-1,1,1,1];
//console.log(endPositive(endPosArray));

//Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.
function alwaysHungry(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy");
            sum += 1;
        }
    }
    if(sum == 0){
        console.log("I'm hungry");
    }
}
var hungryArray = ["word", false, "food", 34, "no", "blah"];
//alwaysHungry(hungryArray);