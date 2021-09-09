// 1 - Sigma
function sigma(num){
    sum = 0;
    for(i = 1; i <= num; i++){
        sum += i;
    }
    return sum;
}
// console.log(sigma(5));

// 2 - Factorial
function factorial(num){
    fact = 1;
    for(i = 1; i <= num; i++){
        fact *= i;
    }
    return fact;
}
// console.log(factorial(5))

// 3 - Star Art
// 3.1
function drawLeftStars(num){
    output = "|";
    if(num > 74){
        return num+" Excedes character limit.";
    }
    if(num < 1){
        return "Please input a positive integer value of characters.";
    }
    for(i = 0; i <= num; i++){
        output += "*";
    }
    for(i = 0; i <= (75-num); i++){
        output += " ";
    }
    output += "|";
    return output;
}
console.log(drawLeftStars(60));

// 3.2
function drawRightStars(num){
    output = "|";
    if(num > 74){
        return num+" Excedes character limit.";
    }
    if(num < 1){
        return "Please input a positive integer value of characters.";
    }
    for(i = 0; i <= (75-num); i++){
        output += " ";
    }
    for(i = 0; i <= num; i++){
        output += "*";
    }
    output += "|";
    return output;
}
console.log(drawRightStars(60));

// 3.3
function drawCenteredStars(num){
    output = "|";
    boundary = (75-num)/2;
    if (num > 73){
        return num+" excedes character limit.";
    }
    if (num < 1){
        return "Please input a positive integer value of characters.";
    }
    for(i = 0; i <= boundary; i++){
        output += " ";
    }
    for(i = 0; i <= num; i++){
        output += "*";
    }
    for(i = 0; i <= boundary; i++){
        output += " ";
    }
    output += "|";
    return output;
}
console.log(drawCenteredStars(60));

