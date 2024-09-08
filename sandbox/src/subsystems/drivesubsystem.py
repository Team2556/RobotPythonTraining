#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import commands2
from wpilib import SmartDashboard

import constants


class DriveSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        """Creates a new DriveSubsystem"""
        super().__init__()

        # The motors on the left side of the drive.
        self.leftMotorLeader = wpilib.Talon(constants.DriveConstants.kLeftMotor1Port)
        self.leftMotors = wpilib.MotorControllerGroup(
            self.leftMotorLeader, 
            wpilib.Talon(constants.DriveConstants.kLeftMotor2Port),
        )
        
        

        # The motors on the right side of the drive.
        self.rightMotorLeader = wpilib.Talon(constants.DriveConstants.kRightMotor1Port)
        self.rightMotors = wpilib.MotorControllerGroup(
            self.rightMotorLeader ,
            wpilib.Talon(constants.DriveConstants.kRightMotor2Port),
        )

        # The robot's drive
        self.drive = wpilib.drive.DifferentialDrive(self.leftMotors, self.rightMotors)

        # The left-side drive encoder
        self.leftEncoder = wpilib.Encoder(
            constants.DriveConstants.kLeftEncoderPorts[0],
            constants.DriveConstants.kLeftEncoderPorts[1],
            constants.DriveConstants.kLeftEncoderReversed,
        )

        # The right-side drive encoder
        self.rightEncoder = wpilib.Encoder(
            constants.DriveConstants.kRightEncoderPorts[0],
            constants.DriveConstants.kRightEncoderPorts[1],
            constants.DriveConstants.kRightEncoderReversed,
        )

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        self.rightMotors.setInverted(True)

        # Sets the distance per pulse for the encoders
        self.leftEncoder.setDistancePerPulse(
            constants.DriveConstants.kEncoderDistancePerPulse
        )
        self.rightEncoder.setDistancePerPulse(
            constants.DriveConstants.kEncoderDistancePerPulse
        )
        SmartDashboard.putString("Drive Status", f'Drive System Initialized')


    def resetEncoders(self):
        """Resets the drive encoders to currently read a position of 0."""
        self.leftEncoder.reset()
        self.rightEncoder.reset()

    def getAverageEncoderDistance(self):
        """
        Gets the average distance of the two encoders.

        :returns: the average of the two encoder readings
        """
        avgEncoderDistance = (self.leftEncoder.getDistance() + self.rightEncoder.getDistance()) / 2.0
        SmartDashboard.putString("Drive Status", f'I have moved about {avgEncoderDistance} meters')
        SmartDashboard.putNumber("Drive Distance", avgEncoderDistance)
        return avgEncoderDistance

    def getLeftEncoder(self) -> wpilib.Encoder:
        """
        Gets the left drive encoder.

        :returns: the left drive encoder
        """
        SmartDashboard.putNumber("Left Encoder", self.leftEncoder.getDistance())
        return self.leftEncoder

    def getRightEncoder(self) -> wpilib.Encoder:
        """
        Gets the right drive encoder.

        :returns: the right drive encoder
        """
        SmartDashboard.putNumber("Right Encoder", self.rightEncoder.getDistance())
        return self.rightEncoder

    def setMaxOutput(self, maxOutput: float):
        """
        Sets the max output of the drive. Useful for scaling the drive to drive more slowly.

        :param maxOutput: the maximum output to which the drive will be constrained
        """
        self.drive.setMaxOutput(maxOutput)

    def arcadeDrive(self, fwd: float, rot: float):
        """
        Drives the robot using arcade controls.

        :param fwd: the commanded forward movement
        :param rot: the commanded rotation
        """
        SmartDashboard.putString("Drive Status", f'Arcade Mode, {fwd=}, {rot=}')
        self.drive.arcadeDrive(fwd, rot)
    
    def driveDistance(self, distance: float):
        SmartDashboard.putString("Drive Status", f'Driving {distance=} ?feet?')
        self.arcadeDrive(fwd=distance, rot=0)
        SmartDashboard.putString("Drive Status", f'Just Drove {distance=} ?feet?')
        # if self.getAverageEncoderDistance() >= distance:
        #     self.drive.arcadeDrive(0, 0)
        #     return True
        # return False