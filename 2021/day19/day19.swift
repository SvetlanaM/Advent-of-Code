import Foundation
import Accelerate
import simd

public class Task19 {
    
    static let testData = """
    --- scanner 0 ---
    404,-588,-901
    528,-643,409
    -838,591,734
    390,-675,-793
    -537,-823,-458
    -485,-357,347
    -345,-311,381
    -661,-816,-575
    -876,649,763
    -618,-824,-621
    553,345,-567
    474,580,667
    -447,-329,318
    -584,868,-557
    544,-627,-890
    564,392,-477
    455,729,728
    -892,524,684
    -689,845,-530
    423,-701,434
    7,-33,-71
    630,319,-379
    443,580,662
    -789,900,-551
    459,-707,401
    --- scanner 1 ---
    686,422,578
    605,423,415
    515,917,-361
    -336,658,858
    95,138,22
    -476,619,847
    -340,-569,-846
    567,-361,727
    -460,603,-452
    669,-402,600
    729,430,532
    -500,-761,534
    -322,571,750
    -466,-666,-811
    -429,-592,574
    -355,545,-477
    703,-491,-529
    -328,-685,520
    413,935,-424
    -391,539,-444
    586,-435,557
    -364,-763,-893
    807,-499,-711
    755,-354,-619
    553,889,-390
    --- scanner 2 ---
    649,640,665
    682,-795,504
    -784,533,-524
    -644,584,-595
    -588,-843,648
    -30,6,44
    -674,560,763
    500,723,-460
    609,671,-379
    -555,-800,653
    -675,-892,-343
    697,-426,-610
    578,704,681
    493,664,-388
    -671,-858,530
    -667,343,800
    571,-461,-707
    -138,-166,112
    -889,563,-600
    646,-828,498
    640,759,510
    -630,509,768
    -681,-892,-333
    673,-379,-804
    -742,-814,-386
    577,-820,562
    --- scanner 3 ---
    -589,542,597
    605,-692,669
    -500,565,-823
    -660,373,557
    -458,-679,-417
    -488,449,543
    -626,468,-788
    338,-750,-386
    528,-832,-391
    562,-778,733
    -938,-730,414
    543,643,-506
    -524,371,-870
    407,773,750
    -104,29,83
    378,-903,-323
    -778,-728,485
    426,699,580
    -438,-605,-362
    -469,-447,-387
    509,732,623
    647,635,-688
    -868,-804,481
    614,-800,639
    595,780,-596
    --- scanner 4 ---
    727,592,562
    -293,-554,779
    441,611,-461
    -714,465,-776
    -743,427,-804
    -660,-479,-426
    832,-632,460
    927,-485,-438
    408,393,-506
    466,436,-512
    110,16,151
    -258,-428,682
    -393,719,612
    -211,-452,876
    808,-476,-593
    -575,615,604
    -485,667,467
    -680,325,-822
    -627,-443,-432
    872,-547,-609
    833,512,582
    807,604,487
    839,-516,451
    891,-625,532
    -652,-548,-490
    30,-46,-14
    """

    enum Axis: String {
        case x = "x"
        case y = "y"
        case z = "z"
    }

    //struct Beacon: CustomStringConvertible {
    //    let x: Int32
    //    let y: Int32
    //    let z: Int32
    //    var matrix: SIMD3<Float> {
    //        return simd_float3(x: Float(x), y: Float(y), z: Float(z))
    //    }
    //
    //    var description: String {
    //        return "\(String(format:"%4d", x)) \(String(format:"%4d", y)) \(String(format:"%4d", z))"
    //    }
    //
    //    func multiply(by: simd_float3x3) -> Beacon {
    //        let multiplied = by * matrix
    //        return Beacon(x: Int32(multiplied.x), y: Int32(multiplied.y), z: Int32(multiplied.z))
    //    }
    //
    //}
    typealias RelativeOffset = (translation: SIMD3<Float>, orientation: simd_float3x3)

    class Scanner: CustomStringConvertible {
        let name: String
        var beacons: [SIMD3<Float>]
        let beaconVariants: [[SIMD3<Float>]]
        var relativePosition: RelativeOffset?
        
        init(data: String) {
            var beaconData = data.split(separator: "\n")
            name = beaconData.removeFirst().trimmingCharacters(in: CharacterSet(charactersIn: "- "))
            let beacons: [SIMD3<Float>] = beaconData.map { beaconData in
                let coords = beaconData.split(separator: ",")
                guard coords.count == 3 else { fatalError("Incorrect number of beacon coords") }
                
                return simd_float3(x: Float(coords[0])!, y: Float(coords[1])!, z: Float(coords[2])!)
            }
            self.beacons = beacons
            
            beaconVariants = rotationMatrices.map { rotation in
                beacons.map { $0 * rotation }
            }
            
        }
        
        func translate() {
            if let relativePosition = relativePosition {
                for (key, beacon) in beacons.enumerated() {
                    beacons[key] = relativePosition.translation + (relativePosition.orientation * beacon)
                }
            }
        }
        
        var description: String {
            return name + "\n" + beacons.map { "\(String(format:"%4.0f", $0.x)) \(String(format:"%4.0f", $0.y)) \(String(format:"%4.0f", $0.z))" }.joined(separator: "\n") + "\n"
        }
    }

    static func generateRotationMatrix(angle: Float, axis: Axis) -> simd_float3x3 {
        let rows: [SIMD3<Float>]
        switch axis {
        case .x:
            rows = [
                simd_float3(1, 0,                   0),
                simd_float3(0, round(cos(angle)),   round(-sin(angle))),
                simd_float3(0, round(sin(angle)),   round(cos(angle)))
            ]
        case .y:
            rows = [
                simd_float3(round(cos(angle)),  0,  round(sin(angle))),
                simd_float3(0,                  1,  0),
                simd_float3(round(-sin(angle)), 0,  round(cos(angle)))
            ]
        case .z:
            rows = [
                simd_float3(round(cos(angle)),  round(-sin(angle)), 0),
                simd_float3(round(sin(angle)),  round(cos(angle)),  0),
                simd_float3(0,                  0,                  1)
            ]
        }
        
        return float3x3(rows: rows)
    }

    static func printMatrix(_ matrix: simd_float3x3) {
        print("\(String(format:"%2.0f", matrix[0][0])) \(String(format:"%2.0f", matrix[0][1])) \(String(format:"%2.0f", matrix[0][2]))")
        print("\(String(format:"%2.0f", matrix[1][0])) \(String(format:"%2.0f", matrix[1][1])) \(String(format:"%2.0f", matrix[1][2]))")
        print("\(String(format:"%2.0f", matrix[2][0])) \(String(format:"%2.0f", matrix[2][1])) \(String(format:"%2.0f", matrix[2][2]))")
        print()
    }

    static func processData(_ data: String) -> [Scanner] {
        let scannerData = data.components(separatedBy: "\n\n")
        return scannerData.map { Scanner(data: $0) }
    }

    static let angles = (
        Float(Measurement(value: 0, unit: UnitAngle.degrees).converted(to: .radians).value),
        Float(Measurement(value: 90, unit: UnitAngle.degrees).converted(to: .radians).value),
        Float(Measurement(value: 180, unit: UnitAngle.degrees).converted(to: .radians).value),
        Float(Measurement(value: 270, unit: UnitAngle.degrees).converted(to: .radians).value)
    )

    static let baseRotations = [
        generateRotationMatrix(angle: angles.0, axis: .x),
        generateRotationMatrix(angle: angles.1, axis: .x),
        generateRotationMatrix(angle: angles.2, axis: .x),
        generateRotationMatrix(angle: angles.3, axis: .x),
        generateRotationMatrix(angle: angles.1, axis: .y),
        generateRotationMatrix(angle: angles.3, axis: .y)
    ]

    static let derivedRotations = [
        baseRotations[0] * generateRotationMatrix(angle: angles.1, axis: .z),
        baseRotations[0] * generateRotationMatrix(angle: angles.2, axis: .z),
        baseRotations[0] * generateRotationMatrix(angle: angles.3, axis: .z),
        baseRotations[1] * generateRotationMatrix(angle: angles.1, axis: .y),
        baseRotations[1] * generateRotationMatrix(angle: angles.2, axis: .y),
        baseRotations[1] * generateRotationMatrix(angle: angles.3, axis: .y),
        baseRotations[2] * generateRotationMatrix(angle: angles.1, axis: .z),
        baseRotations[2] * generateRotationMatrix(angle: angles.2, axis: .z),
        baseRotations[2] * generateRotationMatrix(angle: angles.3, axis: .z),
        baseRotations[3] * generateRotationMatrix(angle: angles.1, axis: .y),
        baseRotations[3] * generateRotationMatrix(angle: angles.2, axis: .y),
        baseRotations[3] * generateRotationMatrix(angle: angles.3, axis: .y),
        baseRotations[4] * generateRotationMatrix(angle: angles.1, axis: .x),
        baseRotations[4] * generateRotationMatrix(angle: angles.2, axis: .x),
        baseRotations[4] * generateRotationMatrix(angle: angles.3, axis: .x),
        baseRotations[5] * generateRotationMatrix(angle: angles.1, axis: .x),
        baseRotations[5] * generateRotationMatrix(angle: angles.2, axis: .x),
        baseRotations[5] * generateRotationMatrix(angle: angles.3, axis: .x)
    ]

    static let rotationMatrices = baseRotations + derivedRotations

    static func findOverlap(first: Scanner, other: Scanner) {
        var matches: [SIMD3<Float>: Int] = [:]

        for (index, variantBeacons) in first.beaconVariants.enumerated() {
            matches.removeAll()
            for variantBeacon in variantBeacons {
                for beacon in other.beacons {
                    let diff = variantBeacon - beacon
                    matches[diff] = (matches[diff] ?? 0) + 1
                }
            }
            let relations = matches.filter { $0.value >= 12 }.map { (translation: $0.key, orientation: rotationMatrices[index]) }
            if let relation = relations.first {
                if relations.count > 1 { print("Found more than one overlap, check possible error") }
                if let firstRelation = first.relativePosition {
                    let orientationToFirst = firstRelation.orientation * relation.orientation
                    other.relativePosition = (translation: firstRelation.translation + orientationToFirst * relation.translation,
                                              orientation: orientationToFirst)
                } else {
                    other.relativePosition = (translation: relation.orientation * relation.translation,
                                              orientation: relation.orientation)
                }
            }
            matches.removeAll()
        }
    }
    
    static func dist(first: Scanner, second: Scanner) -> Float {
        let posFirst = first.relativePosition?.translation ?? simd_float3(0, 0, 0)
        let posSecond = second.relativePosition?.translation ?? simd_float3(0, 0, 0)
        return abs(posFirst.x - posSecond.x) + abs(posFirst.y - posSecond.y) + abs(posFirst.z - posSecond.z)
    }
    
    public static func compute() {
        let data = load(file: "input_19")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var scanners = processData(data!)
        //var scanners = processData(testData)
        var processed: [Scanner] = [scanners.removeFirst()]

        while !scanners.isEmpty {
            let other = scanners.removeFirst()
            for origin in processed {
                findOverlap(first: origin, other: other)
                if other.relativePosition != nil {
                    processed.append(other)
                    break
                }
            }
            if other.relativePosition == nil {
                scanners.append(other)
            }
        }

        processed.forEach {
            $0.translate()
        }

        let allBeacons = processed.reduce([], { $0 + $1.beacons })
        let uniqueBeacons = Array(Set(allBeacons))
        
        print("Total beacon count: \(uniqueBeacons.count)")
        
        var distances: [Float] = []
        while let scanner = processed.popLast() {
            distances += processed.map { dist(first: scanner, second: $0) }
        }
        let maxDistance = distances.max()
        
        print("Maximum distance between two scanners is \(maxDistance!)")

    }
    
}