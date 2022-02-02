import { data } from "./input";

const inputData:string[] = data.split("\n")
const vowels:string = 'aeiou'

const findThreeVowels = (string:string):boolean => {
    return [...string].filter((char) => vowels.search(char) > -1).length > 2
    ? true
    : false
}

const hasForbiddenChars = (string:string):boolean => {
    return ((/ab|xy|cd|pq/).test(string)) ? true : false;
}

const hasDoubleChars = (string:string):boolean => {
    let prevChar = ""
    for (let char of string.split("")) {
        if (prevChar === char) {
            return true
        }
        prevChar = char
      }
    return false  
}

const hasTwoLettersTwice = (string:string):boolean => {
    const stringArr = [...string]
    let prevPair = []
    for (let index in stringArr) {
        let pair = stringArr[Number(index)] + stringArr[Number(index)+1]
        let prevPairIndex = prevPair.indexOf(pair)
        if (prevPairIndex !== -1) {
           if (prevPairIndex !== prevPair.length -1) {
               return true
           }
        }
        prevPair.push(pair)
    }

    return false  
}

const repeatWithMiddleChar = (string:string):boolean => {
    const stringArr = [...string]
    for (let index in stringArr) {
        if (stringArr[Number(index)] === stringArr[Number(index) + 2]) {
            return true
        }
    }
    return false  
}

const isNiceString = (string:string):boolean => {
    return hasForbiddenChars(string) 
    ? false
    : hasDoubleChars(string) && findThreeVowels(string)
    ? true
    : false
}

const isNiceStringRule2 = (string:string):boolean => {
    return hasTwoLettersTwice(string) && repeatWithMiddleChar(string)
}

const getNumOfNiceStrings = (inputData:string[]):number => {
    return inputData.filter((string) => isNiceString(string)).length
}

const getNumOfNiceStrings2 = (inputData:string[]):number => {
    return inputData.filter((string) => isNiceStringRule2(string)).length
}

console.log("Part 1:", getNumOfNiceStrings(inputData))
console.log("Part2:", getNumOfNiceStrings2(inputData))


