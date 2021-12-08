import Foundation

public class Task2 {
    
    enum Op: String {
        case forward
        case up
        case down
    }
    
    public static func compute() {
        let data = load(file: "input_2")
        let adjustments = data?.split(separator: "\n")
        
        var sums: (height: Int, distance: Int) = (0, 0)
        adjustments?.forEach({ adjustment in
            let separated = adjustment.split(separator: " ")
            
            guard separated.count == 2 else { return }
            
            let op = Op(rawValue: String(separated[0]))
            let amount = Int(String(separated[1]))
            
            guard let op = op, let amount = amount else { return }
            
            switch op {
            case .forward:
                sums.distance += amount
            case .down:
                sums.height += amount
            case .up:
                sums.height -= amount
            }
        })

        let result = sums.height * sums.distance
        
        print(result)
        
    }
    
    public static func computeComplex() {
        enum Op: String {
            case forward
            case up
            case down
        }

        let data = load(file: "input_2_alt")
        let adjustments = data?.split(separator: "\n")
            
        var sums: (depth: Int, distance: Int, aim: Int) = (0, 0, 0)
        adjustments?.forEach({ adjustment in
            let separated = adjustment.split(separator: " ")
            
            guard separated.count == 2 else { return }
            
            let op = Op(rawValue: String(separated[0]))
            let amount = Int(String(separated[1]))
            
            guard let op = op, let amount = amount else { return }
            
            switch op {
            case .forward:
                sums.distance += amount
                sums.depth += amount * sums.aim
            case .down:
                sums.aim += amount
            case .up:
                sums.aim -= amount
            }
        })

        print(sums)
        let result = sums.depth * sums.distance
        print(result)
        
    }
    
}