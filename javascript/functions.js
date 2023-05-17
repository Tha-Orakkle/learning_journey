function wordBlanks(myNoun, myAdjectives, myVerb, myAdverb) {
    var result = "";

    result += "The " + myAdjectives + " " + myNoun + " " + myVerb + " to the store " + myAdverb +"."

    return result;
}

console.log(wordBlanks("dog", "big", "ran", "quickly"))

var myGlobal = 10;

function foo1() {
    oopsGlobal = 5; //declaring a variable without the var keyword makes the variable global
}

function foo2() {
    output = "";
    if (typeof myGlobal != "undefined") {
        output += "myGlobal: " + myGlobal;
    }

    if (typeof oopsGlobal != "undefined") {
        output += "\noopsGlobal: " + oopsGlobal;
    }
    console.log(output);

}
foo1();
foo2();

// Anonymous function: Using arrow function
var magic = function () {
    return new Date();
};

// same as 
var magic = () => new Date();

//arrow function with args

var myConcat = (arr1, arr2) => arr1.concat(arr2);

console.log(myConcat([1, 2], [3, 4, 5]));


//
const realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2];
const squareList = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredIntegers;
}

console.log(realNumberArray);
const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);

