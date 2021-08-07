'use strict';
//1
function biggieSize(input){
    for(var i = 0; i < input.length; i++){
        if(input[i] > 0){
            input[i] = "big";
        }
    }
    return input;
}
//console.log(biggieSize([-1,3,5,-5]));

//2
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

//3
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

//4
function addSeven(input){
    var newArray = [];
    for(var i = 1; i < input.length; i++){
        newArray.push(input[i]+7);
    }
    return newArray;
}
//console.log(addSeven([2,1,3,4]));

//5
function printAndReturn(input){
    console.log(input[input.length-2]);
    for(var i = 0; i < input.length; i++){
        if(input[i] % 2 != 0){
            return input[i];
        }
    }
}
//console.log(printAndReturn([1,14,3,4]));

//6
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

//7
function doubleVision(input){
    var newArray = [];
    for(var i = 0; i < input.length; i++){
        newArray.push(input[i]*2);
    }
    return newArray;
}
//console.log(doubleVision([2,3,4,5]));

//8
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

//9
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

//10
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

//11
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

//12
function swapInwards(arr){
    for(var i = 0; i < arr.length/2; i+=2){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}
console.log(swapInwards([1,2,3,4,5,6]));

//13
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

//14
function scaleTheArray(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] *= num;
    }
    return arr;
}
//console.log(scaleTheArray([1,2,3,4,5,6], 2));