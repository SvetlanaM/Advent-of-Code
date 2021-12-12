import Foundation

class Task9 {
    
    static func processData(_ data: String) -> [[Int]] {
        data.split(separator: "\n").map { row in String(row).compactMap { Int(String($0)) } }
    }
    
    static func print2DArray(_ array: [[Any]]) {
        array.forEach { print($0) }
    }
    
    static func compute() {
        
        let testData = """
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
        """
        
        let data = load(file: "input_9")?.trimmingCharacters(in: .whitespacesAndNewlines)
        let caveMap = data.flatMap { processData($0) } ?? []

        var risk = 0
        for x in 0..<caveMap.count {
            let row = caveMap[x]
            for y in 0..<row.count {
                let position = caveMap[x][y]
                let left = y-1
                let right = y+1
                let up = x-1
                let down = x+1
                if left >= 0 && caveMap[x][left] <= position { continue }
                if right < row.count && caveMap[x][right] <= position { continue }
                if up >= 0 && caveMap[up][y] <= position { continue }
                if down < caveMap.count && caveMap[down][y] <= position { continue }
                risk += (position + 1)
            }
        }

        print(risk)
    }
    
    static func compute2OptimizedBugged() {

        let data = load(file: "input_9")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var caveMap = data.flatMap { processData($0) } ?? []

        var tag = 10
        var counters: [Int: Int] = [:]

        for x in 0..<caveMap.count {
            let row = caveMap[x]
            for y in 0..<row.count {
                switch caveMap[x][y] {
                case 9:
                    continue
                case 0...8:
                    caveMap[x][y] = tag
                    counters[tag] = 0
                    tag += 1
                    fallthrough
                default:
                    let currentTag = caveMap[x][y]
                    counters[currentTag]? += 1
                    
                    if y-1 >= 0 && caveMap[x][y-1] > currentTag {
                        let mergedTag = caveMap[x][y-1]
                        let countToMerge = counters[mergedTag] ?? 0
                        counters[mergedTag] = 0
                        counters[currentTag]? += countToMerge
                        
                        // Backward recovery
                        for recoveryY in 0..<row.count {
                            if caveMap[x][recoveryY] == mergedTag {
                                caveMap[x][recoveryY] = currentTag
                            }
                            if x+1 < caveMap.count && caveMap[x+1][recoveryY] == mergedTag {
                                caveMap[x+1][recoveryY] = currentTag
                            }
                        }
                    }
                    
                    // Right
                    if y+1 < row.count && caveMap[x][y+1] < 9 {
                        caveMap[x][y+1] = currentTag
                    }
                    
                    // Down
                    if x+1 < caveMap.count && caveMap[x+1][y] < 9 {
                        caveMap[x+1][y] = currentTag
                    }
                    
                    //print2DArray(caveMap)
                    //print()
                }
            }
        }

        print2DArray(caveMap)
        let sortedCounters = counters.sorted { $0.value > $1.value }.prefix(3)
        let result = sortedCounters.reduce(1, { $0 * $1.value })
        // 828768 too low
        // 2668050 too high
        print(result)
        
    }
    
    static func compute2Greedy() {
        
        let data = load(file: "input_9")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var caveMap = data.flatMap { processData($0) } ?? []

        typealias Position = (x: Int, y: Int)

        var tag = 10
        var counters: [Int: Int] = [:]
        var queue: [Position] = []

        for x in 0..<caveMap.count {
            let row = caveMap[x]
            for y in 0..<row.count {
                if caveMap[x][y] >= 9 { continue }
                
                queue.append((x, y))
                caveMap[x][y] = tag
                counters[tag] = 0
                
                while let position = queue.popLast() {
                    counters[tag]! += 1
                    let x1 = position.x
                    let y1 = position.y
                    if y1-1 >= 0 && caveMap[x1][y1-1] < 9 {
                        caveMap[x1][y1-1] = tag
                        queue.append((x1, y1-1))
                    }
                    if y1+1 < row.count && caveMap[x1][y1+1] < 9 {
                        caveMap[x1][y1+1] = tag
                        queue.append((x1, y1+1))
                    }
                    if x1-1 >= 0 && caveMap[x1-1][y1] < 9 {
                        caveMap[x1-1][y1] = tag
                        queue.append((x1-1, y1))
                    }
                    if x1+1 < caveMap.count && caveMap[x1+1][y1] < 9 {
                        caveMap[x1+1][y1] = tag
                        queue.append((x1+1, y1))
                    }
                }
                
                tag += 1
            }
        }

        //print2DArray(caveMap)
        let sortedCounters = counters.sorted { $0.value > $1.value }.prefix(3)
        print(counters)
        let result = sortedCounters.reduce(1, { $0 * $1.value })

        print(result)
        
    }
    
}