import wpilib
import wpimath.controller
import commands2
import commands2.cmd

import constants

# refer to limit switches for the cannon stop moving at the top and bottom


# create simple class for controlling the angle up and down of the cannon
class CannonSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.cannonMotor = wpilib.PWMSparkMax(constants.CannonConstants.kCannonMotorPort)
        self.cannonEncoder = wpilib.Encoder(
            constants.CannonConstants.kEncoderPorts[0],
            constants.CannonConstants.kEncoderPorts[1],
            constants.CannonConstants.kEncoderReversed,
        )
        self.cannonFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(
            constants.CannonConstants.kSVolts,
            constants.CannonConstants.kVVoltSecondsPerRotation,
        )
        self.getController().setTolerance(
            constants.CannonConstants.kCannonToleranceRPS
        )
        self.cannonEncoder.setDistancePerPulse(constants.CannonConstants.kEncoderCPR)
        self.setSetpoint(constants.CannonConstants.kCannonTargetRPS)
        self.limitSwitchTop = wpilib.DigitalInput(constants.CannonConstants.kLimitSwitchTopPort)
        self.limitSwitchBottom = wpilib.DigitalInput(constants.CannonConstants.kLimitSwitchBottomPort)

    def useOutput(self, output: float, setpoint: float):
        self.cannonMotor.setVoltage(
            output + self.cannonFeedForward.calculate(setpoint)
        )
    
    def getMeasurement(self) -> float:
        return self.cannonEncoder.getRate()
    
    def moveCannon(self, speed: float):
        self.cannonMotor.set(speed)

    

