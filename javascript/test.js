function nextInLine(arr, item) {

    arr.push(item);

    return arr.shift();

}

var testArr = [1, 2, 3, 4, 5];

console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6));
console.log("After: " + JSON.stringify(testArr));
console.log("=============");

function convertToInteger(str) {
    return parseInt(str, 2);
}

console.log(convertToInteger("100"));

// multiple tenary operators

function checkSign(num) {
    return num > 0 ? "positive" : num < 0 ? "negative" : "zero";
}

console.log(checkSign(-1));