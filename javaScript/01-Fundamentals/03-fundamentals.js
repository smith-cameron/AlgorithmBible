'use strict';
//Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].
function biggieSize(input){
    for(var i = 0; i < input.length; i++){
        if(input[i] > 0){
            input[i] = "big";
        }
    }
    return input;
}
//console.log(biggieSize([-1,3,5,-5]));

//You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.
function prevLen(input){
    for(var i = input.length-1; i >= 0 ; i--){
        if(i == 0){
            input[i] = 0;
            return input;
        }
        input[i] = input[i-1].length;
    }
    return input;
}
//console.log(prevLen(["boo3", "haha", "gotchya", "kiddo"]));

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
//console.log(printLowReturnHigh([-34,5,-5,24,14]));

//Build function that accepts array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.
function addSeven(input){
    var newArray = [];
    for(var i = 1; i < input.length; i++){
        newArray.push(input[i]+7);
    }
    return newArray;
}
//console.log(addSeven([2,1,3,4]));

//Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.
function printAndReturn(input){
    console.log(input[input.length-2]);
    for(var i = 0; i < input.length; i++){
        if(input[i] % 2 != 0){
            return input[i];
        }
    }
}
//console.log(printAndReturn([1,14,3,4]));

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
//console.log(reverseArray([1,2,3,4,5,6]));

//Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.
function doubleVision(input){
    var newArray = [];
    for(var i = 0; i < input.length; i++){
        newArray.push(input[i]*2);
    }
    return newArray;
}
//console.log(doubleVision([2,3,4,5]));

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
//console.log(negativeOutlook([12,3,-5]));

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
//console.log(endPositive([-1,1,1,1]));

//Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.
function alwaysHungry(arr){
    var food = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy");
            food += 1;
        }
    }
    if(food == 0){
        console.log("I'm hungry");
    }
}
//alwaysHungry(["word", false, "food", 34, "no", "blah"]);

//Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"
function evenAndOdds(arr){
    for(var i = 0; i < arr.length-2; i++){
        if(arr[i] % 2 != 0 && arr[i+1] % 2 != 0 && arr[i+2] % 2 != 0){
            console.log("That’s odd!");
        }
        else if(arr[i] % 2 == 0 && arr[i+1] % 2 == 0 && arr[i+2] % 2 == 0){
            console.log("Even more so!");
        }
    }
}
//evenAndOdds([1,3,5,4,5,6,7,8,9,2]);

//Given array, swap first and last, third and third-to- last, etc. Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true]. Change [1,2,3,4,5,6] to [6,2,4,3,5,1].
function swapInwards(arr){
    for(var i = 0; i < arr.length/2; i+=2){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}
console.log(swapInwards([1,2,3,4,5,6]));

//Given arr, add 1 to odd elements ([1], [3], etc.), console.log all values and return arr.
function incrementTheSeconds(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 != 0){
            arr[i] += 1;
            console.log(arr[i]);
        }
        console.log(arr[i]);
    }
    return arr;
}
//console.log(incrementTheSeconds([1,2,3,4,5,6]));

//Given array arr and number num, multiply each arr value by num, and return the changed arr.
function scaleTheArray(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] *= num;
    }
    return arr;
}
//console.log(scaleTheArray([1,2,3,4,5,6], 2));