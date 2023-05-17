console.log("Hello World!");

// declaration of vars
var myName = "Paul"; // var used throughout program 
let yourName = "David"; // only used within declaration scope
const pi = 3.14 // var that never changes. It is read-only

console.log(myName + " " + yourName);
var a = 2.0 * 2.5;
console.log(a);
console.log(pi)

// finding length of string
var name = "Justice"
nameLength = name.length; // finds length of string
console.log(nameLength);
console.log(name[0])

// ARRAYS
var ourArray = ["Justice", 23]; // declared with brackets
var myArray = [["the universe", 42], ["everything", 101010]] //nested array
console.log(ourArray + " " + myArray)
console.log(myArray.length)
console.log(myArray[0][1])