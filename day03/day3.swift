import Foundation


class Task3 {
    
    static func compute() {
        let data = load(file: "input_3")
        let stats = data?.split(separator: "\n") ?? []

        let splitStats = stats.map { stat -> Array<Int> in
            let number = Array(stat)
            return number.compactMap { $0.wholeNumberValue }
        }

        let splitResults = splitStats.reduce(Array(repeating: 0, count: splitStats.first?.count ?? 0)) { partialResult, stats in
            return zip(partialResult, stats).map { $0 + $1 }
        }

        let gammaString = splitResults.map { $0 > (splitStats.count / 2) ? "1" : "0" }.joined()
        let epsilonString = splitResults.map { $0 > (splitStats.count / 2) ? "0" : "1" }.joined()

        let gamma = Int(gammaString, radix: 2)
        let epsilon = Int(epsilonString, radix: 2)

        if let gamma = gamma, let epsilon = epsilon {
            let result = gamma * epsilon
            print("Result: \(result)")
        } else {
            print("Failed")
        }
    }
    
    enum Rating {
        case oxygen
        case co2
    }
    
    static func computeSecondPart() {
        let data = load(file: "input_3")
        let stats = data?.split(separator: "\n").filter { !$0.isEmpty } ?? []

        let splitStats = stats.map { stat in
            return Array(stat)
        }

        func reduceStats(stats: [[Substring.Element]], position: Int, type: Rating) -> [Substring.Element]? {
            guard stats.count > 1 && position < (stats.first?.count ?? Int.max) else { return stats.first }
            
            var splitStats: (zeroes: [[Substring.Element]], ones: [[Substring.Element]]) = (zeroes: [], ones: [])
            stats.forEach { stat in
                if stat[position] == "0" { splitStats.zeroes.append(stat) }
                else { splitStats.ones.append(stat) }
            }
            
            let reducedStats: [[Substring.Element]]
            switch type {
            case .oxygen:
                reducedStats = splitStats.ones.count >= splitStats.zeroes.count ? splitStats.ones : splitStats.zeroes
            case .co2:
                reducedStats = splitStats.ones.count < splitStats.zeroes.count ? splitStats.ones : splitStats.zeroes
            }
            
            return reduceStats(stats: reducedStats, position: position + 1, type: type)
        }

        let oxyStats = String(reduceStats(stats: splitStats, position: 0, type: .oxygen)!)
        let co2Stats = String(reduceStats(stats: splitStats, position: 0, type: .co2)!)

        let oxy = Int(oxyStats, radix: 2) ?? 0
        let co2 = Int(co2Stats, radix: 2) ?? 0

        let result = oxy * co2
        print(result)
    }
    
}