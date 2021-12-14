import Foundation

public class Task12 {
    
    let testData = """
    fs-end
    he-DX
    fs-he
    start-DX
    pj-DX
    end-zg
    zg-sl
    zg-pj
    pj-he
    RW-he
    fs-DX
    pj-RW
    zg-RW
    start-pj
    he-WI
    zg-he
    pj-fs
    start-RW
    """

    class Point {
        
        init(name: String) {
            self.name = name
            self.neighbours = []
        }
        
        let name: String
        var neighbours: [Point]
        
        lazy var isStart: Bool = { return name == "start" }()
        lazy var isEnd: Bool = { return name == "end" }()
        lazy var isBig: Bool = { return name.first?.isUppercase == true }()
    }

    static func processData(_ data: String) -> [String: Point] {
        data.split(separator: "\n").reduce([:]) { graph, strPair in
            let points = String(strPair).split(separator: "-")
            guard points.count > 1 else { return graph }
            
            let first = String(points[0])
            let second = String(points[1])
            
            let firstPoint = graph[first] ?? Point(name: first)
            let secondPoint = graph[second] ?? Point(name: second)
            
            firstPoint.neighbours.append(secondPoint)
            secondPoint.neighbours.append(firstPoint)
            
            let newNodes = [
                first: firstPoint,
                second: secondPoint
            ]
            
            return graph.merging(newNodes) { $1 }
        }
    }
    
    static func traverse(currentCave: Point, finished: [String], pathCount: inout Int) {
        currentCave.neighbours.filter({ neighbour in !neighbour.isStart && !finished.contains(where: { $0 == neighbour.name }) }).forEach { cave in
            
            if cave.isEnd {
                pathCount += 1
                return
            }
            
            let newFinished = !cave.isBig ? finished + [cave.name] : finished
            
            traverse(currentCave: cave, finished: newFinished, pathCount: &pathCount)
        }
    }
    
    public static func compute() {

        let data = load(file: "input_12_alt")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var caveGraph = data.flatMap { processData($0) } ?? [:]
        //var caveGraph = processData(testData)
        var pathCount = 0
        traverse(currentCave: caveGraph["start"]!, finished: [], pathCount: &pathCount)

        print(pathCount)
    }
    
    
    static func traverseRevisit(currentCave: Point, finished: [String], visitedTwice: Bool, pathCount: inout Int) {
        currentCave.neighbours.filter({ neighbour in !neighbour.isStart }).forEach { cave in

            let visited = finished.contains(where: { $0 == cave.name })
            if (visited && visitedTwice) {
                return
            }

            if cave.isEnd {
                pathCount += 1
                return
            }

            let newVisitedTwice = visitedTwice || visited

            let newFinished = !cave.isBig ? finished + [cave.name] : finished

            traverseRevisit(currentCave: cave, finished: newFinished, visitedTwice: newVisitedTwice, pathCount: &pathCount)
        }
    }
    
    public static func computeReenter() {
        
        let data = load(file: "input_12_alt")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var caveGraph = data.flatMap { processData($0) } ?? [:]
        //var caveGraph = processData(testData)
        var pathCount = 0
        traverseRevisit(currentCave: caveGraph["start"]!, finished: [], visitedTwice: false, pathCount: &pathCount)

        print(pathCount)
    }
    
}