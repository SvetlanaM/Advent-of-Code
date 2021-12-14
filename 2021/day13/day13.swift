import Foundation

public class Task13 {
    
    let testData = """
    6,10
    0,14
    9,10
    0,3
    10,4
    4,11
    6,0
    6,12
    4,1
    0,13
    10,12
    3,4
    3,0
    8,4
    1,10
    2,14
    8,10
    9,0
    fold along y=7
    fold along x=5
    """
    
    typealias Fold = (axis: Axis, position: Int)

    enum Axis: String {
        case x = "x"
        case y = "y"
    }

    class Point: CustomStringConvertible, Equatable, Hashable {
        
        var x: Int
        var y: Int
        
        init(x: Int, y: Int) {
            self.x = x
            self.y = y
        }
        
        var description: String {
            return "x:\(x) y:\(y)"
        }
        
        static func == (lhs: Point, rhs: Point) -> Bool {
            return lhs.x == rhs.x && lhs.y == rhs.y
        }
        
        func hash(into hasher: inout Hasher) {
            hasher.combine(x)
            hasher.combine(y)
        }
        
    }
    
    static func processData(_ data: String) -> (data: [Point], folds: [Fold]) {
        let lines = data.split(separator: "\n")
        var points: [Point] = []
        var folds: [Fold] = []
        
        for line in lines {
            if line.starts(with: "fold along") {
                let foldParts = line.replacingOccurrences(of: "fold along ", with: "").split(separator: "=")
                guard foldParts.count == 2 else { continue }
                folds.append((axis: Axis(rawValue: String(foldParts[0]))!, position: Int(foldParts[1])!))
            } else {
                let pointParts = line.split(separator: ",")
                guard pointParts.count == 2 else { continue }
                points.append(Point(x: Int(pointParts[0])!, y: Int(pointParts[1])!))
            }
        }
        
        return (data: points, folds: folds)
    }
    
    static func print2DArray(_ points: [Point]) {
        let maxY = points.max(by: { $0.y < $1.y })!.y
        let maxX = points.max(by: { $0.x < $1.x })!.x
        var tempArray: [[String]] = Array.init(repeating: Array.init(repeating: " ", count: maxX+1), count: maxY+1)
        
        for point in points {
            tempArray[point.y][point.x] = "█"
        }
        
        tempArray.map {
            print($0.joined(separator: ""))
        }
    }
    
    public static func compute() {
        
        let data = load(file: "input_13")?.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let data = data else { exit(-1) }

        let instructions = processData(data)
        //var instructions = processData(testData)
        let fold = instructions.folds.first!
        var points = instructions.data

        for point in points {
            switch fold.axis {
            case .x:
                if point.x > fold.position {
                    point.x = point.x - (point.x - fold.position) * 2
                }
            case .y:
                if point.y > fold.position {
                    point.y = point.y - (point.y - fold.position) * 2
                }
            }
        }

        points = Array(Set(points))

        print("Result: \(points.count)")
        
    }
    
    public static func computeFinal() {
        
        let data = load(file: "input_13")?.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let data = data else { exit(-1) }

        let instructions = processData(data)
        //var instructions = processData(testData)
        
        var points = instructions.data

        for fold in instructions.folds {

            for point in points {
                switch fold.axis {
                case .x:
                    if point.x > fold.position {
                        point.x = point.x - (point.x - fold.position) * 2
                    }
                case .y:
                    if point.y > fold.position {
                        point.y = point.y - (point.y - fold.position) * 2
                    }
                }
            }
            
            points = Array(Set(points))
            
        }

        print("-----")
        print2DArray(points)
        
    }
    
    
}