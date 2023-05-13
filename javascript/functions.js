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