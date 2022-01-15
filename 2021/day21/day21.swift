import Foundation

public class Task21 {
    
    enum PlayerType: CustomStringConvertible {
        case first
        case second
        
        var description: String {
            switch self {
            case .first:
                return "First"
            case .second:
                return "Second"
            }
        }
    }
    
    class Player: CustomStringConvertible {
        var type: PlayerType
        private var currentPosition: Int
        var points: Int = 0
        var position: Int {
            return currentPosition + 1
        }
        
        init(type: PlayerType, position: Int) {
            self.type = type
            self.currentPosition = position - 1
        }
        
        func move(amount: Int) {
            self.currentPosition += amount
            self.currentPosition %= 10
            points += position
        }
        
        func backtrack(amount: Int) {
            points -= position
            self.currentPosition -= amount
            if self.currentPosition < 0 {
                self.currentPosition += 10
            }
        }
        
        var description: String {
            return "Position: \(position), current points: \(points)"
        }
    }

    class Die: CustomStringConvertible {
        private var currentValue = 0
        var rolls = 0
        var value: Int {
            return currentValue + 1
        }
        
        func throwNext() {
            currentValue += 1
            currentValue %= 100
            rolls += 1
        }
        
        var description: String {
            return "Total rolls: \(rolls), last value: \(value)"
        }
    }
    
    static func processData(_ data: String) -> [PlayerType: Player] {
        var lines = data.components(separatedBy: "\n")
        let firstPlayer = (lines.removeFirst().split(separator: ":").last?.trimmingCharacters(in: .whitespacesAndNewlines)).flatMap({ Int($0) }).flatMap({ Player(type: .first, position: $0) })
        let secondPlayer = (lines.removeFirst().split(separator: ":").last?.trimmingCharacters(in: .whitespacesAndNewlines)).flatMap({ Int($0) }).flatMap({ Player(type: .second, position: $0) })
        guard let firstPlayer = firstPlayer, let secondPlayer = secondPlayer else { fatalError("Error parsing players") }
        return [.first: firstPlayer, .second: secondPlayer]
    }
    
    public static func computeTraining() {
        let data = load(file: "input_21_alt")?.trimmingCharacters(in: .whitespacesAndNewlines)
        //let players = (first: Player(position: 4), second: Player(position: 8))
        let players = processData(data!)
        let winningPoints = 1000
        let die = Die()
        var currentPlayer = players[.first]!

        while players[.first]!.points < winningPoints && players[.second]!.points < winningPoints {
            var roll = 0
            for _ in 1...3 {
                roll += die.value
                die.throwNext()
            }
            currentPlayer.move(amount: roll)
            
            currentPlayer = currentPlayer.type == .first ? players[.second]! : players[.first]!
        }


        print(players)
        print(die)
        let result = currentPlayer.points * die.rolls
        print("Result: \(result)")
    }
    
    public static func computeDirac() {
        let data = load(file: "input_21")?.trimmingCharacters(in: .whitespacesAndNewlines)
        //let players = [PlayerType.first: Player(type: PlayerType.first, position: 4), PlayerType.second: Player(type: PlayerType.second, position: 8)]
        let players = processData(data!)
        let winningPoints = 21
        var wins = [PlayerType.first: 0, PlayerType.second: 0]
        
        let multiverseMap = [
            3: 1,
            4: 3,
            5: 6,
            6: 7,
            7: 6,
            8: 3,
            9: 1
        ]

        func nextThrow(currentPlayer: PlayerType, multiverses: Int = 1) {
            for amount in 3...9 {
                players[currentPlayer]!.move(amount: amount)
                let multiverseSplits = multiverses * multiverseMap[amount]!
                if players[currentPlayer]!.points < winningPoints {
                    nextThrow(currentPlayer: currentPlayer == .first ? .second : .first, multiverses: multiverseSplits)
                } else {
                    //print(players[currentPlayer]!)
                    wins[currentPlayer]! += multiverseSplits
                }
                players[currentPlayer]!.backtrack(amount: amount)
            }
        }

        nextThrow(currentPlayer: .first)

        print(players)
        print(wins)
        let result = wins.values.max()!
        print("Result: \(result)")
    }
    
    
}