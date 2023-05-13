var ourArray = ["Justice", 23]; // declared with brackets
var myArray = [["the universe", 42], ["everything", 101010]] //nested array
console.log(ourArray + " " + myArray)
console.log(myArray.length)
console.log(myArray[0][1])
ourArray.push("David", 54) 
console.log(ourArray)
// append data to the end of an array with the push function
var justArray = [["Feranmi", 21], ["DannyAce", 43]]
justArray.push(["Paul", 12])
console.log(justArray)

// removing from an array with the pop function
// removes last item of an array
var paul = justArray.pop()
console.log(paul)
console.log(justArray)

// removing the first item of an array with the shift function
// removes the first item
var feranmi = justArray.shift()
console.log(feranmi)
console.log(justArray)

// add element to the beginning of the array with unshift function
justArray.unshift(["David", 54])
console.log(justArray)