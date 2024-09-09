import wpilib
import wpimath.controller
import commands2
import commands2.cmd


# refer to limit switches for the cannon stop moving at the top and bottom

from wpimath.controller import PIDController
from wpimath.system.plant import DCMotor
from wpimath import units

from wpilib.simulation import BatterySim, EncoderSim, RoboRioSim, SingleJointedArmSim
from constants import CannonLiftConstants

class CannonLift:
    def __init__(self):
        # something like this goes in the physics.py file
        # self.arm = SingleJointedArmSim(constants.CannonConstants.kArmSimModel)
        # self.arm.setFriction(constants.CannonConstants.kArmFriction)
        # self.arm.setMass(constants.CannonConstants.kArmMass)
        # self.arm.setGearing(constants.CannonConstants.kArmGearing)
        # self.arm.setInertia(constants.CannonConstants.kArmInertia)
        # self.arm.setVoltage(0)
        # self.arm.setAngle(constants.CannonConstants.kArmStartingAngle)
        # self.arm.setVelocity(0)
        # self.arm.setAcceleration(0)
        # The P gain for the PID controller that drives this arm.

        self.armKp = CannonLiftConstants.kDefaultArmKp
        self.armSetpointDegrees = CannonLiftConstants.kDefaultArmSetpointDegrees

        # The arm gearbox represents a gearbox containing two Vex 775pro motors.
        self.armGearbox = DCMotor.vex775Pro(2)

        # Standard classes for controlling our arm
        self.controller = PIDController(self.armKp, 0, 0)
        self.encoder = wpilib.Encoder(
            CannonLiftConstants.kEncoderPorts[0], CannonLiftConstants.kEncoderPorts[1]
        )
        self.motor = wpilib.PWMSparkMax(CannonLiftConstants.kMotorPort)

        # Subsystem constructor.
        self.encoder.setDistancePerPulse(CannonLiftConstants.kArmEncoderDistPerPulse)

        # Set the Arm position setpoint and P constant to Preferences if the keys don't already exist
        wpilib.Preferences.initDouble(
            CannonLiftConstants.kArmPositionKey, self.armSetpointDegrees
        )
        wpilib.Preferences.initDouble(CannonLiftConstants.kArmPKey, self.armKp)



# create simple class for controlling the angle up and down of the cannon
# class CannonSubsystem(commands2.Subsystem):
#     def __init__(self) -> None:
#         super().__init__()
#         self.cannonMotor = wpilib.Talon(constants.CannonConstants.kCannonMotorPort)
#         self.cannonEncoder = wpilib.Encoder(
#             constants.CannonConstants.kEncoderPorts[0],
#             constants.CannonConstants.kEncoderPorts[1],
#             constants.CannonConstants.kEncoderReversed,
#         )
#         self.cannonFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(
#             constants.CannonConstants.kSVolts,
#             constants.CannonConstants.kVVoltSecondsPerRotation,
#         )
#         self.getController().setTolerance(
#             constants.CannonConstants.kCannonToleranceRPS
#         )
#         self.cannonEncoder.setDistancePerPulse(constants.CannonConstants.kEncoderCPR)
#         self.setSetpoint(constants.CannonConstants.kCannonTargetRPS)
#         self.limitSwitchTop = wpilib.DigitalInput(constants.CannonConstants.kLimitSwitchTopPort)
#         self.limitSwitchBottom = wpilib.DigitalInput(constants.CannonConstants.kLimitSwitchBottomPort)

#     def useOutput(self, output: float, setpoint: float):
#         self.cannonMotor.setVoltage(
#             output + self.cannonFeedForward.calculate(setpoint)
#         )
    
#     def getMeasurement(self) -> float:
#         return self.cannonEncoder.getRate()
    
#     def moveCannon(self, speed: float):
#         self.cannonMotor.set(speed)

    

