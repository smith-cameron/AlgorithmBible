function print1to255(){
let num = 1;
while (num <= 255) {
console.log(num);
num = num + 1;
}
}
// print1to255()

function printMaxOfArray(arr) {
    if (arr.length == 0) {
        console.log("[], no max val.");     
        return;
    }
    var max = 0;
    for (var idx = 0; idx < arr.length; idx++) {
        if (arr[idx] > max){ 
            max = arr[idx]; 
        }
    }
    console.log("Max val is:", max);
}

function printMaxOfArray(arr) {
    if (arr.length == 0) {
    console.log("[], no max val.");
    return;
    }
    var max = 0;
    for (var idx = 0;
    idx < arr.length; idx++) {
    if (arr[idx] > max)
    { max = arr[idx]; }
    }
    console.log("Max val is:", max);
    }
    
printMaxOfArray([])


function printOdds1to255()
{
var num = 1;
while (num <= 255)
{
console.log(num + 2);
}
num ++
}
printOdds1to255()