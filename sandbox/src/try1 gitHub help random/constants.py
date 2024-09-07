#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

"""
The constants module is a convenience place for teams to hold robot-wide
numerical or boolean constants. Don't use this for any other purpose!
"""
import wpilib
import math
from id import PWM_channels, DIO_channels, PCM_channels,Solenoid_modules,Gears



class DriveConstants:
    # The PWM IDs for the drivetrain motor controllers.
    kLeftMotor1Port = PWM_channels.LEFT_FRONT_MOTOR
    kLeftMotor2Port = PWM_channels.LEFT_REAR_MOTOR
    kRightMotor1Port = PWM_channels.RIGHT_FRONT_MOTOR
    kRightMotor2Port = PWM_channels.RIGHT_REAR_MOTOR

    # Encoders and their respective motor controllers.
    kLeftEncoderPorts = (0, 1) #TODO: change these to the correct ports, or can bus id for spark max
    kRightEncoderPorts = (2, 3)
    kLeftEncoderReversed = False
    kRightEncoderReversed = True

    # Encoder counts per revolution/rotation.
    kEncoderCPR = 1024
    kWheelDiameterInches = 6

    # Assumes the encoders are directly mounted on the wheel shafts
    kEncoderDistancePerPulse = (kWheelDiameterInches * math.pi) / kEncoderCPR
    kGearSifterModule = wpilib.PneumaticsModuleType.REVPH


class ArmConstants:
    # NOTE: Please do NOT use these values on your robot.
    kMotorPort = PCM_channels.CANNON_ACTUATOR

    kP = 1
    kSVolts = 1
    kGVolts = 1
    kVVoltSecondPerRad = 0.5
    kAVoltSecondSquaredPerRad = 0.1

    kMaxVelocityRadPerSecond = 3
    kMaxAccelerationRadPerSecSquared = 10

    kEncoderPorts = (4, 5) #TODO: change these to the correct ports, or can bus id for spark max
    kEncoderPPR = 256
    kEncoderDistancePerPulse = 2.0 * math.pi / kEncoderPPR

    # The offset of the arm from the horizontal in its neutral position,
    # measured from the horizontal
    kArmOffsetRads = 0.5

    kFireControlModule = wpilib.PneumaticsModuleType.REVPH


class AutoConstants:
    kAutoTimeoutSeconds = 12
    kAutoShootTimeSeconds = 7


class OIConstants:
    kDriverControllerPort = 0
