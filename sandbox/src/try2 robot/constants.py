#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

"""
A place for the constant values in the code that may be used in more than one place. 
This offers a convenient resources to teams who need to make both quick and universal
changes.
"""

import math
from enum import IntEnum, unique


class DriveConstants:
    kLeftMotor1Port = 0
    kLeftMotor2Port = 1
    kRightMotor1Port = 2
    kRightMotor2Port = 3

    kLeftEncoderPorts = (0, 1)
    kRightEncoderPorts = (2, 3)
    kLeftEncoderReversed = False
    kRightEncoderReversed = True

    kEncoderCPR = 1024
    kWheelDiameterInches = 6

    # Assumes the encoders are directly mounted on the wheel shafts
    kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR


class ShooterConstants:
    kEncoderPorts = (4, 5)
    kEncoderReversed = False
    kEncoderCPR = 1024
    kEncoderDistancePerPulse = 1 / kEncoderCPR

    kShooterMotorPort = 4
    kFeederMotorPort = 5

    kShooterFreeRPS = 5300
    kShooterTargetRPS = 4000
    kShooterToleranceRPS = 50

    # These are not real PID gains, and will have to be tuned for your specific robot.
    kP = 1
    kI = 0
    kD = 0

    # On a real robot the feedforward constants should be empirically determined; these are
    # reasonable guesses.
    kSVolts = 0.05

    # Should have value 12V at free speed...
    kVVoltSecondsPerRotation = 12.0 / kShooterFreeRPS

    kFeederSpeed = 0.5

    kFireSolenoidPort = 6


class CannonLiftConstants:
    kMotorPort = 7
    kEncoderPorts = (6, 7)
    kEncoderReversed = False
    kEncoderCPR = 1024
    kArmEncoderDistPerPulse = 360 / kEncoderCPR
    kArmPositionKey = "Cannon Position"
    kArmPKey = "CannonP"
    kArmMaxAngleDegrees = 60
    kArmMinAngleDegrees = -15

    kDefaultArmKp = 1
    kDefaultArmSetpointDegrees = 90


    kSVolts = 0.05
    kVVoltSecondsPerRotation = 12.0 / 1.0

    kLiftTargetRPS = 1
    kLiftToleranceRPS = 0.1

    kLimitSwitchTopPort = 8
    kLimitSwitchBottomPort = 9
    # CannonLiftConstants.kArmReduction,
            # wpilib.simulation.SingleJointedArmSim.estimateMOI(
            #     CannonLiftConstants.kArmLength, CannonLiftConstants.kArmMass
            # ),
            # CannonLiftConstants.kArmLength,
            # CannonLiftConstants.kMinAngleRads,
            # CannonLiftConstants.kMaxAngleRads,
    kArmReduction = 2/1
    kArmLength = 4
    kArmMass = 10
    kMinAngleRads = 15/180
    kMaxAngleRads = 45/180


class CannonConstants:
    kCannonMotorPort = 7
    kCannonChargeSolenoidPort = 9
    kEncoderPorts = (6, 7)
    kEncoderReversed = False
    kEncoderCPR = 1024

    kSVolts = 0.05
    kVVoltSecondsPerRotation = 12.0 / 1.0


    kCannonTargetRPS = 1
    kCannonToleranceRPS = 0.1

    kLimitSwitchTopPort = 8
    kLimitSwitchBottomPort = 9

@unique
class RobotArmStates(IntEnum):
    ARMING = 0
    ARMED = 1
    DISARMED = 2

class AutoConstants:
    kAutoTimeoutSeconds = 12
    kAutoShootTimeSeconds = 7
    kAutoChargeTimeSeconds = 3


class OIConstants:
    kDriverControllerPort = 0


