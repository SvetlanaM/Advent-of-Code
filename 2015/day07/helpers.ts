type wireDict = Map<string, number>

export function isNumeric(val:string) {
    return /^-?\d+$/.test(val);
}

export const regexPattern = /\W\s?/g;

export const findWireNumber = (wiresDictionary:wireDict, number:string):boolean => {
    return wiresDictionary.has(number) || isNumeric(number)
}
