//3 - Array: Rotate 
function rotateArr(array, shiftBy){
    console.log("Shift by: "+shiftBy);
    shiftBy = shiftBy % array.length
    if ( shiftBy%array.length == 0 && shiftBy !== 1){
        return array
    }
    for(var i=0; i < array.length/2; i++ ){
        var tempVal = array[i] ;
        array[i] = array[array.length - i -1];
        array[array.length - i - 1] = tempVal;
    }
    for(var i=0; i < (shiftBy)/2; i++ ){
        var tempVal = array[i] ;
        array[i] = array[shiftBy - i -1];
        array[shiftBy - i -1] = tempVal;
    }
    for(var i=shiftBy; i < (array.length+shiftBy)/2; i++ )
    {
        var tempVal = array[i] ;
        array[i] = array[array.length -i + shiftBy -1 ];
        array[array.length -i + shiftBy -1 ] = tempVal;
}
    return array
}
// console.log("[1,2,3,4,5,6], shiftBy 1");
console.log("output: ",rotateArr([1,2,3,4,5,6],-1))