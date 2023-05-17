// creating up objects in javascript

var testObj = {
    "hat": "ballcap",
    "shirt": "jersey",
    "shoes": "cleats",
    12: "Lebron",
    16: "Kyrie"
};

var hatValue = testObj.hat;
var shirtValue = testObj["shirt"]; // brackets or dot can be used to access obj properties

var playerNum = 12;
var player = testObj[playerNum];    
console.log(hatValue);
console.log(shirtValue);
console.log(player);
delete testObj[16] //deletes a property in an object
console.log(testObj);

console.log("====================");

function phoneticLookup(val) {
    var result = "";

    var lookup = {
        "alpha": "Adams",
        "bravo": "Boston",
        "charlie": "Chicago",
        "delta": "Denver",
        "echo": "Easy",
        "foxtrot": "Frank"
    };
    result = lookup[val];
    return result;
}

console.log(phoneticLookup("charlie")) 

// the hasOwnProperty() method is used to check if an object has a property
// returns True of False
var myObj = {
    "gift": "pony",
    "pet": "kitten",
    "bed": "sleigh"
};

function checkObj(prop) {
    if (myObj.hasOwnProperty(prop)) {
        return myObj[prop];
    } else {
        return "Not Found";
    }
}

console.log(checkObj("gift"));