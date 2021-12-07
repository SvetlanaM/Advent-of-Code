import Foundation

public class Task5 {
    
    public static func compute() {
        let data = load(file: "input_5_alt")
        let ventArray = data?.split(separator: "\n").map { String($0) } ?? []


        var resultMap: [String: Int] = [:]
        ventArray.forEach { vent in
            let coords = vent.components(separatedBy: " -> ")
            
            guard coords.count == 2 else { return }
            
            let start = coords[0].split(separator: ",")
            let end = coords[1].split(separator: ",")
            
            let startX = Int(start[0])!
            let startY = Int(start[1])!
            
            let endX = Int(end[0])!
            let endY = Int(end[1])!
            
            //guard startX == endX || startY == endY else { return }
            
            let diffX = startX == endX ? 0 : startX < endX ? 1 : -1
            let diffY = startY == endY ? 0 : startY < endY ? 1 : -1
                
            var position = (x: startX, y: startY)
            while (position.x != endX || position.y != endY) {
                let key = "\(position.x),\(position.y)"
                resultMap[key] = (resultMap[key] ?? 0) + 1
                
                position.x += diffX
                position.y += diffY
            }
            let key = "\(position.x),\(position.y)"
            resultMap[key] = (resultMap[key] ?? 0) + 1
        }

        let result = resultMap.filter { $0.value > 1 }
        print(result.count)

    }
    
}