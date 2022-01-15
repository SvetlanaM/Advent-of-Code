import Foundation

public class Task16 {
    
    static let testData = "9C0141080250320F1802104A08"

    struct Packet {
        let version: Int
        let content: Content
        let subpackets: [Packet]
        
        var versionSum: Int {
            return subpackets.reduce(version, { $0 + $1.versionSum })
        }
        
        var result: Int {
            switch content {
            case .literal(let val):
                return val
            case .operation(let op):
                switch op {
                case .sum:
                    return subpackets.reduce(0, { $0 + $1.result })
                case .product:
                    return subpackets.reduce(1, { $0 * $1.result })
                case .minimum:
                    return subpackets.min(by: { $0.result < $1.result })!.result
                case .maximum:
                    return subpackets.max(by: { $0.result < $1.result })!.result
                case .greater:
                    return subpackets[0].result > subpackets[1].result ? 1 : 0
                case .less:
                    return subpackets[0].result < subpackets[1].result ? 1 : 0
                case .equal:
                    return subpackets[0].result == subpackets[1].result ? 1 : 0
                case .literal:
                    fatalError("Literal should not be in op")
                }
            }
        }
    }

    enum Content: CustomStringConvertible {
        case literal(Int)
        case operation(Operation)
        
        var description: String {
            switch self {
            case .literal(let value):
                return String(value)
            case .operation(let op):
                return "\(op)"
            }
        }
    }

    enum Operation: String {
        case literal = "100"
        case sum = "000"
        case product = "001"
        case minimum = "010"
        case maximum = "011"
        case greater = "101"
        case less = "110"
        case equal = "111"
    }

    static func processData(_ binary: String) -> (packet: Packet, remainder: Substring?) {
        let versionIndex = binary.index(binary.startIndex, offsetBy: 3)
        let version = binary[..<versionIndex]
        let versionNumber = Int(version, radix: 2)
        
        let typeIndex = binary.index(versionIndex, offsetBy: 3)
        let type = Operation(rawValue: String(binary[versionIndex..<typeIndex]))!
        
        switch type {
        case .literal:
            var startIndex: String.Index? = typeIndex
            var endIndex = binary.index(typeIndex, offsetBy: 5, limitedBy: binary.endIndex)
            var shouldStop = false
            var literal = ""
            while startIndex != nil && endIndex != nil && !shouldStop {
                shouldStop = binary[startIndex!] == "0"
                literal += binary[binary.index(after: startIndex!)..<endIndex!]
                let newEndIndex = binary.index(endIndex!, offsetBy: 5, limitedBy: binary.endIndex)
                startIndex = endIndex
                endIndex = newEndIndex
            }
            let number = Int(literal, radix: 2)
            let remainder = startIndex.flatMap { binary[$0..<binary.endIndex] }
            return (packet: Packet(version: versionNumber!, content: .literal(number!), subpackets: []), remainder: remainder)
        default:
            let lengthType = binary[typeIndex]
            let lengthIndex = binary.index(after: typeIndex)
            switch lengthType {
            case "0":
                let subpacketsIndex = binary.index(lengthIndex, offsetBy: 15)
                let length = Int(binary[lengthIndex..<subpacketsIndex], radix: 2)!
                let remainderIndex = binary.index(subpacketsIndex, offsetBy: length)
                
                var processing: Substring? = binary[subpacketsIndex..<remainderIndex]
                var subpackets: [Packet] = []
                while processing != nil && !processing!.isEmpty {
                    let packetData = processData(String(processing!))
                    subpackets.append(packetData.packet)
                    processing = packetData.remainder
                }
                
                let remainder = binary[remainderIndex..<binary.endIndex]
                return (packet: Packet(version: versionNumber!, content: .operation(type), subpackets: subpackets), remainder: remainder)
            case "1":
                let subpacketsIndex = binary.index(lengthIndex, offsetBy: 11)
                let length = Int(binary[lengthIndex..<subpacketsIndex], radix: 2)!
                var processing: Substring? = binary[subpacketsIndex..<binary.endIndex]
                var subpackets: [Packet] = []
                for _ in 0..<length {
                    let packetData = processData(String(processing!))
                    subpackets.append(packetData.packet)
                    processing = packetData.remainder
                }
                
                return (packet: Packet(version: versionNumber!, content: .operation(type), subpackets: subpackets), remainder: processing)
            default:
                fatalError("Uknown packet type")
            }
        }
    }
    
    public static func compute() {

        let data = load(file: "input_16")?.trimmingCharacters(in: .whitespacesAndNewlines)
        let packet = processData(data!.hexaToBinary)
        //let packet = processData(testData.hexaToBinary)
        print(packet.remainder ?? "nil")

        //print(packet)
        print(packet.packet.versionSum)
        print(packet.packet.result)
    }
    
}

extension String {
    typealias Byte = UInt8
    var hexaToBytes: [Byte] {
        var start = startIndex
        return stride(from: 0, to: count, by: 2).compactMap { _ in   // use flatMap for older Swift versions
            let end = index(after: start)
            defer { start = index(after: end) }
            return Byte(self[start...end], radix: 16)
        }
    }
    var hexaToBinary: String {
        return hexaToBytes.map {
            let binary = String($0, radix: 2)
            return repeatElement("0", count: 8-binary.count) + binary
        }.joined()
    }
}