let leftWheelPort: OutputPort = .b
let rightWheelPort: OutputPort = .c

let leftRightBC = (leftWheelPort == .b)

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
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power)
    }
}

func left(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power,
            brakeAtEnd: brake)
    }
}

func startRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power)
    }
}

func right(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: -power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: power,
            brakeAtEnd: brake)
    }
}

func startForwardLeft(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0)
    }
}

func forwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0,
            brakeAtEnd: brake)
    }
}

func startForwardRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power)
    }
}

func forwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: power, rightPower: 0,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: power,
            brakeAtEnd: brake)
    }
}

func startBackwardLeft(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0)
    }
}

func backwardLeft(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0,
            brakeAtEnd: brake)
    }
}

func startBackwardRight(power: Float = 100) {
    if leftRightBC {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0)
    } else {
        ev3.move(
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power)
    }
}

func backwardRight(nRotations: Float = 1, power: Float = 100, brake: Bool = false) {
    if leftRightBC {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: -power, rightPower: 0,
            brakeAtEnd: brake)
    } else {
        ev3.move(
            forRotations: nRotations,
            leftPort: leftWheelPort, rightPort: rightWheelPort,
            leftPower: 0, rightPower: -power,
            brakeAtEnd: brake)
    }
}


// test drive
startForward()
startBackward()
startLeft()
startRight()
startForwardLeft()
startBackwardLeft()
startForwardRight()
startBackwardRight()
 
forward()
backward()
left()
right()
forwardLeft()
backwardLeft()
forwardRight()
backwardRight()
