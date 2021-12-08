import Foundation

public class Task1 {
    
    public static func compute() {
        let data = load(file: "input_1_alt")
        let depths = data?.split(separator: "\n").compactMap { Int($0) } ?? []
        print("Total depths: \(depths.count)")

        var increases = 0
        for (key, value) in depths.enumerated() {
            guard key > 0 else { continue }
            if value > depths[key-1] { increases += 1 }
        }

        print("Simple increases: \(increases)")

        var slideIncrease = 0
        for (key, _) in depths.enumerated() {
            guard key > 2 else { continue }
            if (depths[key-2...key].reduce(0, +)) > (depths[key-3...key-1].reduce(0, +)) { slideIncrease += 1 }
        }

        print("Sliding window increases: \(slideIncrease)")
    }
    
}