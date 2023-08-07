// let car = new Object();
// car["make"] = "Audi";
// car["model"] = "A5";
// car["carReg"] = "W8M8";

// console.log(car) // shows all attributes
// console.log(car.make); //show the value of make
// console.log(car.model); //show the value of model
// console.log(car.carReg); //show the value of carReg

// //The object can have new properties added at any time. Known as an expando property.

// car.numberOfDoors = 4;
// console.log(car.numberOfDoors); //Shows the value referring to number of doors.
//a lot simpler and quicker to declare objects

// let car = { make: "Audi", model: "A5", carReg: "W8M8" };
 let carPark = [
    { make: "Audi", model: "A5", carReg: "AB12CDE" },
    { make: "hyundai", model: "i30", carReg: "AB11CDE" },
    { make: "Audi", model: "A5", carReg: "W8M8" } 
]    
// the lack of comma at end of the listmeans last of list, no more new lists,
// but can work if was there also.
// console.log(carPark);

// for (let i = 0; i < carPark.length; i++) {
//     for (let key in carPark[i]) {
//         console.log(`${key} : ${carPark[i][key]}`);
//     }  // loop in loop prints out all the key and values in array 
// }
// below is the temperalliteral version of the same thing
// for(let obj in carPark){
//     for(let key in carPark[obj]){
//         console.log(`${key}: ${carPark[obj][key]}`)
//     }
// }



//ex1
let darthVader = new Object()
darthVader ["allegiance"] = "empier";
darthVader ["wepon"]        ="lightsabre" ;
darthVader ["sith"]         ="true";
console.log(darthVader);

// QA SOLUTION BELOW
// let darthVader = {
//     allegiance: "Empire",
//     weapon: "lightsaber",
//     sith: true
// };
// console.log(darthVader);


// let jedi;
// if (darthVader.sith == true){
//     jedi = false;
// }
// else{
//     jedi = true;
// }