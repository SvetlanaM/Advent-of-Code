import Foundation

public class Task14 {
    
    static let testData = """
    NNCB

    CH -> B
    HH -> N
    CB -> H
    NH -> C
    HB -> C
    HC -> B
    HN -> C
    NN -> C
    BH -> H
    NC -> B
    NB -> B
    BN -> B
    BB -> N
    BC -> B
    CC -> N
    CN -> C
    """

    static func processData(_ data: String) -> (polymer: String, replacements: [String: String]) {
        var lines = data.split(separator: "\n")
        let polymer = String(lines.removeFirst())
            
        let replacements: [String: String] = lines.map { line -> [String] in
            let parts: [String] = String(line).components(separatedBy: " -> ")
            guard parts.count == 2 else { fatalError() }
            return parts
        }.reduce(into: [String: String](), { $0[$1[0]] = $1[1] })
        
        return (polymer: polymer, replacements: replacements)
    }
    
    static func processDataOptimized(_ data: String) -> (polymer: [String: Int], replacements: [String: String], counter: [Character: Int]) {
        var lines = data.split(separator: "\n")
        let polymerString = String(lines.removeFirst())
        var polymer: [String: Int] = [:]
        var counter: [Character: Int] = [:]
        for index in polymerString.indices {
            counter[polymerString[index]] = (counter[polymerString[index]] ?? 0) + 1
            let indexTwo = polymerString.index(after: index)
            if indexTwo != polymerString.endIndex {
                let pair = "\(polymerString[index])\(polymerString[indexTwo])"
                polymer[pair] = (polymer[pair] ?? 0) + 1
            }
        }
        
        let replacements: [String: String] = lines.map { line -> [String] in
            let parts: [String] = String(line).components(separatedBy: " -> ")
            guard parts.count == 2 else { fatalError() }
            return parts
        }.reduce(into: [String: String](), { $0[$1[0]] = $1[1] })
        
        return (polymer: polymer, replacements: replacements, counter: counter)
    }
    
    public static func compute() {
        
        let data = load(file: "input_14")?.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let data = data else { exit(-1) }

        let polymerData = processData(data)
        //let polymerData = processData(testData)

        var polymer = polymerData.polymer
        for _ in 0..<10 {
            for index in polymer.indices.reversed() {
                let indexTwo = polymer.index(after: index)
                if indexTwo != polymer.endIndex, let insertLetter = polymerData.replacements["\(polymer[index])\(polymer[indexTwo])"] {
                    polymer.insert(insertLetter.first!, at: indexTwo)
                }
            }
        //    print(polymer)
        //    print(polymer.count)
        //    print("---")
        }

        let frequencies = polymer.reduce(into: [Character:Int](), { $0[$1] = ($0[$1] ?? 0) + 1 })
        let counts = frequencies.values
        let result = counts.max()! - counts.min()!

        print(frequencies)
        print(result)
        
    }
    
    public static func computeOptimized() {
        
        let data = load(file: "input_14_alt")?.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let data = data else { exit(-1) }

        let polymerData = processDataOptimized(data)
        //let polymerData = processDataOptimized(testData)

        var polymer = polymerData.polymer
        var polymerNext = polymer
        var polymerCounter = polymerData.counter

        for _ in 0..<40 {
            polymerNext.keys.forEach { polymerNext[$0] = 0 }
            for (pair, count) in polymer {
                if let insertLetter = polymerData.replacements[pair] {
                    let newPair = "\(pair.first!)\(insertLetter)"
                    polymerNext[newPair] = (polymerNext[newPair] ?? 0) + count
                    let newPairTwo = "\(insertLetter)\(pair.last!)"
                    polymerNext[newPairTwo] = (polymerNext[newPairTwo] ?? 0) + count
                    polymerCounter[insertLetter.first!] = (polymerCounter[insertLetter.first!] ?? 0) + count
                } else {
                    polymerNext[pair] = (polymerNext[pair] ?? 0) + count
                }
            }

            polymer = polymerNext
        }

        let result = polymerCounter.values.max()! - polymerCounter.values.min()!

        print(result)
        
    }
    
}