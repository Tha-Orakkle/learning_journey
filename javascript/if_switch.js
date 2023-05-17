/* The equality sign "==" is used to compare values
and it does the type conversion. E.g 3 == '3' will give you a true
when compared with "=="
However with the strict equality sign "===" the result will be false
"!==" - strict inequality
 
*/
function testStrict(val) {
    if (val === 10) {
        return "Equal"
    }
    return "Not Equal"
}

function testSize(num) {
    if (num < 5) {
        return "Tiny"
    } else if (num < 5) {
        return "Small"
    } else if (num < 15) {
        return "Medium"
    } else if (num < 20) {
        return "Large"
    } else {
        return "Huge"
    }
}


console.log(testStrict('10'))
console.log(testSize(20))

//using switch cases

var count = 0;

function cc(card) {
    switch(card) {
        case 1:
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            count++;
            break;
        case 10:
        case "J":
        case "Q":
        case "K":
        case "A":
            count--;
            break;
    }

    var holdbet = "Hold";

    if (count > 0) {
        holdbet = "Bet"
    }

    return count + " " + holdbet;
}

cc(2); cc(3); cc(10); cc(2); cc(3);
console.log(count);
console.log(cc(4));