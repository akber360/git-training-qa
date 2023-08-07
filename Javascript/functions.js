"use strict";
let subtracter = (num1,num2) =>{
    return num1 - num2;
}
console.log(subtracter(10,2));

let welcome = function(fname,lname,age,gender){
    return (`My name is ${fname} ${lname}, i am ${age} years old and of gender ${gender}`);
};
console.log(welcome("akber", "Ali", 20, "male"));

let powerup = (n1,n2) =>{
 return Math.pow(n1,n2);   
};
console.log(powerup(6,6));