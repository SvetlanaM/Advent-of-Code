
import { findWireNumber, isNumeric, regexPattern } from "./helpers";
import { data } from "./input";


let inputInstructions = data.split("\n").map((item) => item.split(regexPattern).filter(n => n))
let wiresDictionary = new Map<string, number>();
const stack = [...inputInstructions]

const Operators = {
      AND: (x:number, y:number) => x & y,
      OR: (x:number, y:number) => x | y,
      LSHIFT: (x:number, y:number) => (x << y) & 65535,
      RSHIFT: (x:number, y:number) => x >> y,
      NOT: (x:number) => (~(x)) & 65535,
}

const hasBitwiseOperator = (item:string[]):string => {
    return item.filter((i) => i.match(/^[A-Z]*$/))[0]
}

const canComputeWire = (bitwiseOperator:string, wire:string[]):boolean => {
    const [x, y, z] = wire

    return bitwiseOperator === 'NOT' 
    ? (findWireNumber(wiresDictionary, y)) 
    : ((findWireNumber(wiresDictionary, x)) && (findWireNumber(wiresDictionary, z)));
}

const getWireNumber = (string:string):number => {
    return wiresDictionary.has(string) 
    ? wiresDictionary.get(string) || 0
    : Number(string)
}

const setWire = (op: (x:number, y:number) => number, ...item:string[]) => {
    const [x, y, z] = item
    let bitwiseResult = op(getWireNumber(x), getWireNumber(y))
    wiresDictionary.set(z, bitwiseResult)
}

const part1 = (stack:string[][]):number => {
    do {
        const item = stack.shift() || []
        const bitwiseOperator = hasBitwiseOperator(item)
        const [x, y, z, w] = item

        if (bitwiseOperator) {  
            if (canComputeWire(bitwiseOperator, item)) {
                bitwiseOperator === 'NOT'
                ? setWire(Operators[bitwiseOperator], y, '', z)  
                : setWire(Operators[bitwiseOperator], x, z, w) 
            }
            else {
                stack.push(item)
            }
        } else {
            findWireNumber(wiresDictionary, x)
            ? wiresDictionary.set(y, getWireNumber(x) || 0)
            : stack.push(item)
        }
    } while (!wiresDictionary.has('a'))

    return wiresDictionary.get('a') || 0
}

const part2 = ():number => {
    const indexOfB = inputInstructions.findIndex((item) => item[1] === 'b')
    inputInstructions[indexOfB][0] = String(wiresDictionary.get('a'))
    wiresDictionary.clear()
    const stack2 = [...inputInstructions]
    return part1(stack2)
}

console.log("Part1:", part1(stack))
console.log("Part2:", part2())
