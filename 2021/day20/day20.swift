import Foundation

extension Collection {

    // Returns the element at the specified index if it is within bounds, otherwise nil.
    subscript (safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}

public class Task20 {
    
    static let testData = """
    ..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
    #..#.
    #....
    ##..#
    ..#..
    ..###
    """

    struct ImageData: CustomStringConvertible {
        let algorithm: [Bool]
        var image: [[Bool]]
        var repeated: Bool
        
        var description: String {
            return image.map { row in row.map { $0 ? "#" : "." }.joined() }.joined(separator: "\n") + "\nRepeated: \(repeated)\n"
        }
        
        func enhancePixel(data: [Bool]) -> Bool {
            guard let index = Int(data.map { $0 ? "1" : "0" }.joined(), radix: 2) else { fatalError("Cannot convert bit array to int") }
            return algorithm[index]
        }
        
        var onPixels: Int {
            return image.reduce(0, { (acc, row) in acc + row.filter({ $0 }).count })
        }
    }

    static func processData(_ data: String) -> ImageData {
        var lines = data.components(separatedBy: "\n")
        let algorithm = lines.removeFirst().map { $0 == "#" }
        lines.removeFirst()
        let image = lines.map { row in row.map { $0 == "#" } }
        return ImageData(algorithm: algorithm, image: image, repeated: false)
    }
    
    public static func compute(enhances: Int = 2) {
    
        let data = load(file: "input_20_alt")?.trimmingCharacters(in: .whitespacesAndNewlines)
        var imageData = processData(data!)
        //var imageData = processData(testData)
        for _ in 1...enhances {
            var enhancedImage = imageData.image
            for index in enhancedImage.indices {
                enhancedImage[index].insert(imageData.repeated, at: 0)
                enhancedImage[index].append(imageData.repeated)
            }
            let rowSize = enhancedImage.first!.count
            enhancedImage.insert(Array(repeating: imageData.repeated, count: rowSize), at: 0)
            enhancedImage.append(Array(repeating: imageData.repeated, count: rowSize))
            
            for x in enhancedImage.indices {
                for y in enhancedImage[x].indices {
                    let data = [
                        imageData.image[safe: x-2]?[safe: y-2] ?? imageData.repeated,
                        imageData.image[safe: x-2]?[safe: y-1] ?? imageData.repeated,
                        imageData.image[safe: x-2]?[safe: y] ?? imageData.repeated,
                        imageData.image[safe: x-1]?[safe: y-2] ?? imageData.repeated,
                        imageData.image[safe: x-1]?[safe: y-1] ?? imageData.repeated,
                        imageData.image[safe: x-1]?[safe: y] ?? imageData.repeated,
                        imageData.image[safe: x]?[safe: y-2] ?? imageData.repeated,
                        imageData.image[safe: x]?[safe: y-1] ?? imageData.repeated,
                        imageData.image[safe: x]?[safe: y] ?? imageData.repeated,
                    ]
                    enhancedImage[x][y] = imageData.enhancePixel(data: data)
                }
            }
            
            imageData.image = enhancedImage
            imageData.repeated = imageData.enhancePixel(data: Array(repeating: imageData.repeated, count: 9))
        }

        print(imageData.onPixels)
        
    }
    
}