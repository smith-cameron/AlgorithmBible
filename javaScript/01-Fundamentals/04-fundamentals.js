'use strict';
// ToolBox
function reverse(input){
    for(var i = 0; i < input.length/2; i++){
        var temp = input[i];
        input[i] = input[input.length-1-i];
        input[input.length-1-i] = temp;
    }
    return input
}
function randomInt() {
    // return Math.floor(Math.random() * (Math.floor(100) - Math.ceil(50)) + Math.ceil(50)); //limit 50-100
    return Math.floor(Math.random() * 100); // limit 0-100
}

// 1- Only Keep the Last Few
function keepAFew(input, x){
    if(input.length < x ){
        return input;
    }
    reverse(input);
    input.length -= input.length-x;
    reverse(input);
    return input
}
// console.log(keepAFew([2,4,6,8,10],3))

//2- Math Help (Y = MX + B Solve for x when y=0)
function mathHelp(m, b){
    var y = 0
    y -= b
    y /= m
    return y
}
// console.log(mathHelp(20,12));

function whatHappensToday(){
    var meteors = 30/100;
    var blizzards = 25/100;
    var earthquakes = 20/100;
    var tsunamis = 15/100;
    var volcanos = 10/100;
    var today
    return today;
}
// console.log(whatHappensToday());

function whatReallyHappensToday(){

}

// 5- Soaring IQ
function soaringIQ(input){
    var iq = input;
    var increase = .01;
    for(var i = 1; i < 98 ; i++){
        iq += increase;
        increase += .01;
    }
    return iq;
}
console.log(soaringIQ(101));

// 6- Letter Grade
function letterGrade(input){
    if(input >= 90 && input <= 100){
        return "Score: "+input+". Grade: A";
    }
    if(input >= 80 && input < 90){
        return "Score: "+input+". Grade: B";
    }
    if(input >= 70 && input < 80){
        return "Score: "+input+". Grade: C";
    }
    if(input >= 60 && input < 70){
        return "Score: "+input+". Grade: D";
    }
    else{
        return "Score: "+input+". Grade: F";
    }
}
// console.log(letterGrade(80));

// 7- More Accurate Grades
function accurateLetterGrade(input){
    if(input >= 98 && input <= 100){
        return "Score: "+input+". Grade: A+";
    }
    if(input >= 92 && input < 98){
        return "Score: "+input+". Grade: A";
    }
    if(input >= 90 && input < 92){
        return "Score: "+input+". Grade: A-";
    }
    if(input >= 88 && input < 90){
        return "Score: "+input+". Grade: B+";
    }
    if(input >= 82 && input < 88){
        return "Score: "+input+". Grade: B";
    }
    if(input >= 80 && input < 82){
        return "Score: "+input+". Grade: B-";
    }
    if(input >= 78 && input < 80){
        return "Score: "+input+". Grade: C+";
    }
    if(input >= 72 && input < 78){
        return "Score: "+input+". Grade: C";
    }
    if(input >= 70 && input < 72){
        return "Score: "+input+". Grade: C-";
    }
    if(input >= 68 && input < 70){
        return "Score: "+input+". Grade: D+";
    }
    if(input >= 62 && input < 68){
        return "Score: "+input+". Grade: D";
    }
    if(input >= 60 && input < 62){
        return "Score: "+input+". Grade: D-";
    }
    else{
        return "Score: "+input+". Grade: F";
    }
}
// console.log(accurateLetterGrade(randomInt()));