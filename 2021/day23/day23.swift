import Foundation

public class Task23 {
    
    class House: Hashable, CustomStringConvertible {
    
        class Amphipod: Hashable {
            
            enum AmphipodType: String {
                case amber = "A"
                case bronze = "B"
                case copper = "C"
                case desert = "D"
            }
            
            let type: AmphipodType
            var space: Space
            
            var energyPerStep: Int {
                switch type {
                case .amber:
                    return 1
                case .bronze:
                    return 10
                case .copper:
                    return 100
                case .desert:
                    return 1000
                }
            }
            
            var isHome: Bool {
                return type == space.type &&
                (space.sublevel == nil || (space.sublevel!.occupant != nil && space.sublevel!.occupant!.isHome))
            }
            
            init(type: AmphipodType, space: Space) {
                self.type = type
                self.space = space
            }
            
            static func == (lhs: Task23.House.Amphipod, rhs: Task23.House.Amphipod) -> Bool {
                return lhs.type == rhs.type && lhs.space == rhs.space
            }
            
            func hash(into hasher: inout Hasher) {
                hasher.combine(type)
                hasher.combine(space.number)
            }
            
        }
        
        class Space: Hashable, CustomStringConvertible {
            let number: Int
            let type: Amphipod.AmphipodType?
            var occupant: Amphipod?
            var paths: [Path] = []
            var sublevel: Space?
            
            var isEmpty: Bool { return occupant == nil }
            var isRoom: Bool { return type != nil }
            
            init(number: Int, type: Amphipod.AmphipodType? = nil) {
                self.number = number
                self.type = type
            }
            
            static func == (lhs: House.Space, rhs: House.Space) -> Bool {
                return lhs.number == rhs.number
            }
            
            func hash(into hasher: inout Hasher) {
                hasher.combine(number)
            }
            
            var description: String {
                return "\(isRoom ? "R" : "H"): \(number), amphipod: \(occupant?.type.rawValue ?? "none"), p: [\(paths.map { $0.description }.joined(separator: ","))]"
            }
        }
        
        struct Path: CustomStringConvertible {
            let destination: Space
            let via: [Space]
            let distance: Int
            
            var description: String {
                return "\(destination.number)"
            }
        }
        
        let rooms: [Space]
        let hallways: [Space]
        var amphipods: [Amphipod] = []
        
        var isFinished: Bool {
            return amphipods.allSatisfy({ $0.isHome })
        }
        
        init(rooms: [Space], hallways: [Space]) {
            self.rooms = rooms
            self.hallways = hallways
        }
        
        static func == (lhs: Task23.House, rhs: Task23.House) -> Bool {
            return lhs.hashValue == rhs.hashValue
        }
        
        func hash(into hasher: inout Hasher) {
            hasher.combine(amphipods)
        }
        
        var description: String {
            return ([amphipods.map { $0.type.rawValue }.joined(separator: ",")] + rooms.map { $0.description } + hallways.map { $0.description }).joined(separator: "\n")
        }
        
    }

    static func generateHouse() -> House {
        let hallways = [1,2,3,4,5,6,7].map { House.Space(number: $0) }
        let rooms = [
            House.Space(number: 8, type: .amber),
            House.Space(number: 9, type: .amber),
            House.Space(number: 10, type: .bronze),
            House.Space(number: 11, type: .bronze),
            House.Space(number: 12, type: .copper),
            House.Space(number: 13, type: .copper),
            House.Space(number: 14, type: .desert),
            House.Space(number: 15, type: .desert)
        ]
        
        [0,2,4,6].forEach {
            rooms[$0].sublevel = rooms[$0+1]
        }
        
        let distances = [[
            (3, [hallways[1]]),
            (4, [hallways[1], rooms[0]]),
            (5, [hallways[1], hallways[2]]),
            (6, [hallways[1], hallways[2], rooms[2]]),
            (7, [hallways[1], hallways[2], hallways[3]]),
            (8, [hallways[1], hallways[2], hallways[3], rooms[4]]),
            (9, [hallways[1], hallways[2], hallways[3], hallways[4]]),
            (10, [hallways[1], hallways[2], hallways[3], hallways[4], rooms[6]])
        ], [
            (2, []),
            (3, [rooms[0]]),
            (4, [hallways[2]]),
            (5, [hallways[2], rooms[2]]),
            (6, [hallways[2], hallways[3]]),
            (7, [hallways[2], hallways[3], rooms[4]]),
            (8, [hallways[2], hallways[3], hallways[4]]),
            (9, [hallways[2], hallways[3], hallways[4], rooms[6]])
        ], [
            (2, []),
            (3, [rooms[0]]),
            (2, []),
            (3, [rooms[2]]),
            (4, [hallways[3]]),
            (5, [hallways[3], rooms[4]]),
            (6, [hallways[3], hallways[4]]),
            (7, [hallways[3], hallways[4], rooms[6]])
        ], [
            (4, [hallways[2]]),
            (5, [hallways[2], rooms[0]]),
            (2, []),
            (3, [rooms[2]]),
            (2, []),
            (3, [rooms[4]]),
            (4, [hallways[4]]),
            (5, [hallways[4], rooms[6]])
        ], [
            (6, [hallways[2], hallways[3]]),
            (7, [hallways[2], hallways[3], rooms[0]]),
            (4, [hallways[3]]),
            (5, [hallways[3], rooms[2]]),
            (2, []),
            (3, [rooms[4]]),
            (2, []),
            (3, [rooms[6]])
        ], [
            (8, [hallways[2], hallways[3], hallways[4]]),
            (9, [hallways[2], hallways[3], hallways[4], rooms[0]]),
            (6, [hallways[3], hallways[4]]),
            (7, [hallways[3], hallways[4], rooms[2]]),
            (4, [hallways[4]]),
            (5, [hallways[4], rooms[4]]),
            (2, []),
            (3, [rooms[6]])
        ], [
            (9, [hallways[2], hallways[3], hallways[4], hallways[5]]),
            (10, [hallways[2], hallways[3], hallways[4], hallways[5], rooms[0]]),
            (7, [hallways[3], hallways[4], hallways[5]]),
            (8, [hallways[3], hallways[4], hallways[5], rooms[2]]),
            (5, [hallways[4], hallways[5]]),
            (6, [hallways[4], hallways[5], rooms[4]]),
            (3, [hallways[5]]),
            (4, [hallways[5], rooms[6]])
        ]]
        
        for h in hallways.indices {
            for r in rooms.indices {
                let distance = distances[h][r].0
                let via = distances[h][r].1
                rooms[r].paths.append(House.Path(destination: hallways[h], via: via, distance: distance))
                hallways[h].paths.append(House.Path(destination: rooms[r], via: via, distance: distance))
            }
        }
        
        return House(rooms: rooms, hallways: hallways)
    }

    static func processData(_ data: String, house: inout House) {
        var lines = data.components(separatedBy: "\n")
        lines.removeFirst(2)
        
        var line = lines.removeFirst()
        house.rooms[0].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[3]))!, space: house.rooms[0])
        house.rooms[2].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[5]))!, space: house.rooms[2])
        house.rooms[4].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[7]))!, space: house.rooms[4])
        house.rooms[6].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[9]))!, space: house.rooms[6])
        
        line = lines.removeFirst()
        house.rooms[1].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[3]))!, space: house.rooms[1])
        house.rooms[3].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[5]))!, space: house.rooms[3])
        house.rooms[5].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[7]))!, space: house.rooms[5])
        house.rooms[7].occupant = House.Amphipod(type: House.Amphipod.AmphipodType(rawValue: String(line[9]))!, space: house.rooms[7])
        
        house.amphipods = house.rooms.compactMap { $0.occupant }.sorted(by: { $0.energyPerStep < $1.energyPerStep })
        
    }
    
    public static func compute() {
        let data = load(file: "input_23")!.trimmingCharacters(in: .whitespacesAndNewlines)
        var house = generateHouse()
        processData(data, house: &house)
        print(house)
        
        var bestPrice = Int.max
        var priceCache: [Int: Int] = [:]

        func moveAmphipods(price: Int) {
            guard price < bestPrice && (priceCache[house.hashValue] == nil || priceCache[house.hashValue]! > price) else { return }
            priceCache[house.hashValue] = price
            
            if house.isFinished {
                bestPrice = min(price, bestPrice)
                return
            }
                                                            
            for amphipod in house.amphipods {
                guard !amphipod.isHome else { continue }
                for path in amphipod.space.paths.filter({ path in
                    return path.destination.isEmpty &&
                    path.via.allSatisfy({ $0.isEmpty }) &&
                    (!path.destination.isRoom || (amphipod.type == path.destination.type && (path.destination.sublevel == nil || (!path.destination.sublevel!.isEmpty && path.destination.sublevel!.occupant!.isHome))))
                }) {
                    let previous = amphipod.space
                    previous.occupant = nil
                    amphipod.space = path.destination
                    path.destination.occupant = amphipod
                    
                    moveAmphipods(price: price + path.distance * amphipod.energyPerStep)
                    
                    previous.occupant = amphipod
                    amphipod.space = previous
                    path.destination.occupant = nil
                }
            }
                        
        }
        
        moveAmphipods(price: 0)

        //print(priceCache)
        print("Best solution: \(bestPrice)")
    }
    
}

public extension String {

    var length: Int {
        return count
    }

    subscript (i: Int) -> String {
        return self[i ..< i + 1]
    }

    func substring(fromIndex: Int) -> String {
        return self[min(fromIndex, length) ..< length]
    }

    func substring(toIndex: Int) -> String {
        return self[0 ..< max(0, toIndex)]
    }

    subscript (r: Range<Int>) -> String {
        let range = Range(uncheckedBounds: (lower: max(0, min(length, r.lowerBound)),
                                            upper: min(length, max(0, r.upperBound))))
        let start = index(startIndex, offsetBy: range.lowerBound)
        let end = index(start, offsetBy: range.upperBound - range.lowerBound)
        return String(self[start ..< end])
    }
}