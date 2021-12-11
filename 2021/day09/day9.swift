let data = load(file: "input")?.trimmingCharacters(in: .whitespacesAndNewlines)
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