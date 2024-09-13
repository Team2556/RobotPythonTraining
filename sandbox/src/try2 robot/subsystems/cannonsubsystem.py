import wpilib
import wpimath.controller
from wpilib import SmartDashboard
import commands2
import commands2.cmd


# refer to limit switches for the cannon stop moving at the top and bottom

from wpimath.controller import PIDController
from wpimath.system.plant import DCMotor
from wpimath import units

from wpilib.simulation import BatterySim, EncoderSim, RoboRioSim, SingleJointedArmSim
from try3_bust_with_poenix.constants import CannonLiftConstants

class CannonLift(commands2.Subsystem):
    def __init__(self):
        

        self.armKp = CannonLiftConstants.kDefaultArmKp
        self.armSetpointDegrees = CannonLiftConstants.kDefaultArmSetpointDegrees

        # The arm gearbox represents a gearbox containing two Vex 775pro motors.
        self.armGearbox = DCMotor.vex775Pro(2)

        # Standard classes for controlling our arm
        self.controller = PIDController(self.armKp, 0, 0)
        self.encoder = wpilib.Encoder(
            CannonLiftConstants.kEncoderPorts[0], CannonLiftConstants.kEncoderPorts[1]
        )
        
        self.encoder.setDistancePerPulse(CannonLiftConstants.kArmEncoderDistPerPulse)  # in degrees
        self.encoder.reset()
        # TODO: create a homing routine
        self.encoderSim = EncoderSim(self.encoder)
        self.motor = wpilib.PWMSparkMax(CannonLiftConstants.kMotorPort)

        

        # Set the Arm position setpoint and P constant to Preferences if the keys don't already exist
        wpilib.Preferences.initDouble(
            CannonLiftConstants.kArmPositionKey, self.armSetpointDegrees
        )
        wpilib.Preferences.initDouble(CannonLiftConstants.kArmPKey, self.armKp)

        self.limitSwitchTop = wpilib.DigitalInput(CannonLiftConstants.kLimitSwitchTopPort) # configure H/W normally open
        SmartDashboard.putBoolean("Limit Switch Top disengaged", self.limitSwitchTop.get())
        self.limitSwitchBottom = wpilib.DigitalInput(CannonLiftConstants.kLimitSwitchBottomPort) # configure H/W normally open
        SmartDashboard.putBoolean("Limit Switch Bottom disengaged", self.limitSwitchBottom.get())
        
        SmartDashboard.putString("Cannon Lift Status", f'Cannon Lift Initialized')

    def setMotorSpeed(self, speed: float):
        # safety gate for normally open limit switches
        ANGLE= self.encoder.getDistance()
        SmartDashboard.putNumber("Cannon Lift Angle", ANGLE)
        if ((ANGLE) > CannonLiftConstants.kArmMaxAngleDegrees or 
                ANGLE < CannonLiftConstants.kArmMinAngleDegrees):
            SmartDashboard.putString("Cannon Lift Status", f'Cannon Lift beyond encoder limits at {ANGLE} degrees')
            self.motor.set(0)
        elif (AtTOP:=not(self.limitSwitchTop.get()) ) or ( AtBottom:=not(self.limitSwitchBottom.get())):
            self.motor.set(0)
            SmartDashboard.putString("Cannon Lift Status", f'Cannon Lift at limit switch {AtTOP=} {AtBottom=}')
        elif speed== 0:
            self.motor.set(speed)
            SmartDashboard.putString("Cannon Lift Status", f'Cannon Lift instructed to be still')
        else:
            self.motor.set(speed)
            
            SmartDashboard.putString("Cannon Lift Status", f'Cannon Lift Moving at {speed} speed')
    



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

    

