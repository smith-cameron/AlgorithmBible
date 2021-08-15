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
    output = "";
    if(num > 74){
        return "{} Excedes character limit.".format(num);
    }
    if(num < 1){
        return "Please input a positive integer value of characters.";
    }
    for(i = 0; i <= num; i++){
        output += "*";
    }
    return output;
}
// console.log(drawLeftStars(25));

// 3.2
function drawRightStars(num){
    output = "";
    if(num > 74){
        return "{} Excedes character limit.".format(num);
    }
    if(num < 1){
        return "Please input a positive integer value of characters."
    }

}