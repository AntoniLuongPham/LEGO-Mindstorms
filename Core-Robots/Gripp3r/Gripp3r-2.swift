let leftWheelPort: OutputPort = .c
let rightWheelPort: OutputPort = .b

func startForward(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power)
}

func forward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: power,
        brakeAtEnd: brake)
}

func startBackward(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power)
}

func backward(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: -power,
        brakeAtEnd: brake)
}

func startLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: -power)
}

func left(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: -power,
        brakeAtEnd: brake)
}

func startRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: power)
}

func right(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: power,
        brakeAtEnd: brake)
}

func startForwardLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: 0)
}

func forwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: power, rightPower: 0,
        brakeAtEnd: brake)
}

func startForwardRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: power)
}

func forwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: power,
        brakeAtEnd: brake)
}

func startBackwardLeft(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: 0)
}

func backwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: -power, rightPower: 0,
        brakeAtEnd: brake)
}

func startBackwardRight(power: Float = 100) {
    ev3.move(
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: -power)
}

func backwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    ev3.move(
        forRotations: nRotations,
        leftPort: leftWheelPort, rightPort: rightWheelPort,
        leftPower: 0, rightPower: -power,
        brakeAtEnd: brake)
}

ev3.motorOn(forSeconds: 1, on: .a, withPower: -50)
forward(nRotations: 3, power: 75, brake: true)
ev3.playSound(file: .snap, atVolume: 100, withStyle: .playOnce)
ev3.motorOn(forSeconds: 1, on: .a, withPower: 50)
right(nRotations: 2.5, power: 75, brake: true)
forward(nRotations: 3, power: 75, brake: true)
ev3.motorOn(on: .a, withPower: -50)
ev3.playSound(file: .snap, atVolume: 100, withStyle: .playOnce)