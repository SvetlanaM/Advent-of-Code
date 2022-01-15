import Foundation


public class Task25 {
    
    static let testData = """
    v...>>.vv>
    .vv>>.vv..
    >>.>v>...v
    >>v>>.>.v.
    v>v.vv.v..
    >.>>..v...
    .vv..>.>v.
    v.v..>>v.v
    ....v..v.>
    """

    class SeaCucumber: Comparable, CustomStringConvertible {
        
        enum Direction {
            case east
            case south
        }
        
        let moveDirection: Direction
        var bottomTile: Bottom?
        
        init(moveDirection: Direction) {
            self.moveDirection = moveDirection
        }
        
        static func < (lhs: SeaCucumber, rhs: SeaCucumber) -> Bool {
            return lhs.moveDirection == .east && rhs.moveDirection == .south
        }
        
        static func == (lhs: SeaCucumber, rhs: SeaCucumber) -> Bool {
            return lhs.moveDirection == rhs.moveDirection
        }
        
        var description: String {
            switch moveDirection {
            case .south:
                return "v"
            case .east:
                return ">"
            }
        }
        var canMove: Bool {
            switch moveDirection {
            case .east:
                return bottomTile!.nextEast!.isEmpty == true
            case .south:
                return bottomTile!.nextSouth!.isEmpty == true
            }
        }
        
        func move() {
            switch moveDirection {
            case .east:
                bottomTile!.nextEast!.occupant = self
                bottomTile?.occupant = nil
                bottomTile = bottomTile!.nextEast
            case .south:
                bottomTile!.nextSouth!.occupant = self
                bottomTile?.occupant = nil
                bottomTile = bottomTile!.nextSouth
            }
        }
    }

    class Bottom: CustomStringConvertible {
        var occupant: SeaCucumber?
        var nextEast: Bottom?
        var nextSouth: Bottom?
        
        var isEmpty: Bool {
            return occupant == nil
        }
        
        init(occupant: SeaCucumber? = nil) {
            self.occupant = occupant
            self.occupant?.bottomTile = self
        }
        
        var description: String {
            return occupant.flatMap { $0.description } ?? "."
        }
        
    }

    class SeaFloor: CustomStringConvertible {
        var seaCucumbers: [SeaCucumber]
        var bottomTiles: [[Bottom]]
        
        init(seaCucumbers: [SeaCucumber], bottomTiles: [[Bottom]]) {
            self.seaCucumbers = seaCucumbers
            self.bottomTiles = bottomTiles
        }
        
        var description: String {
            return bottomTiles
                .map({ row in row.map { $0.description }.joined() })
                .joined(separator: "\n")
        }
        
        func moveAll() -> Bool {
            let willMoveEast = seaCucumbers.filter { $0.moveDirection == .east && $0.canMove }
            willMoveEast.forEach { $0.move() }
            let willMoveSouth = seaCucumbers.filter { $0.moveDirection == .south && $0.canMove }
            willMoveSouth.forEach { $0.move() }
            return !willMoveEast.isEmpty || !willMoveSouth.isEmpty
        }
        
    }

    static func processData(_ data: String) -> SeaFloor {
        let lines = data.components(separatedBy: "\n")
        let bottomTiles: [[Bottom]] = lines.map { line in
            line.map { char in
                switch char {
                case ".":
                    return Bottom()
                case ">":
                    return Bottom(occupant: SeaCucumber(moveDirection: .east))
                case "v":
                    return Bottom(occupant: SeaCucumber(moveDirection: .south))
                default:
                    fatalError("Uknown character in input")
                }
            }
        }
        for (x, row) in bottomTiles.enumerated() {
            for (y, tile) in row.enumerated() {
                tile.nextEast = bottomTiles[x][(y+1) % row.count]
                tile.nextSouth = bottomTiles[(x+1) % bottomTiles.count][y]
            }
        }
        let seaCucumbers: [SeaCucumber] = bottomTiles
            .reduce(into: [], { acc, row in acc += row.compactMap { $0.occupant } })
            .sorted()
        
        return SeaFloor(seaCucumbers: seaCucumbers, bottomTiles: bottomTiles)
    }
    
    public static func compute() {
        let data = load(file: "input_25")!.trimmingCharacters(in: .whitespacesAndNewlines)
        var seaFloor = processData(data)
        //var seaFloor = processData(testData)
        print(seaFloor.seaCucumbers.map{ $0.description }.joined())
        print(seaFloor)
        print()

        var moves = 0

        while seaFloor.moveAll() {
            moves += 1
            //print(seaFloor)
            //print()
        }

        print(seaFloor)
        print()

        print(moves+1)
    }
    
}