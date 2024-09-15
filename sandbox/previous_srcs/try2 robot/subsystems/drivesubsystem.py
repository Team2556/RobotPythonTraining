#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
from wpimath.geometry import Rotation2d, Rotation3d, Translation2d, Translation3d
import commands2
from wpilib import SmartDashboard

import try3_bust_with_poenix.constants as constants

class DriveSubsystem(commands2.Subsystem ):
    def __init__(self) -> None:
        """Creates a new DriveSubsystem"""
        super().__init__()

        # The motors on the left side of the drive.
        # self.leftMotorLeader = wpilib.Talon(constants.DriveConstants.kLeftMotor1Port)
        # self.leftMotors = wpilib.MotorControllerGroup(
        #     self.leftMotorLeader, 
        #     wpilib.Talon(constants.DriveConstants.kLeftMotor2Port),
        # )
        
        

        # # The motors on the right side of the drive.
        # self.rightMotorLeader = wpilib.Talon(constants.DriveConstants.kRightMotor1Port)
        # self.rightMotors = wpilib.MotorControllerGroup(
        #     self.rightMotorLeader ,
        #     wpilib.Talon(constants.DriveConstants.kRightMotor2Port),
        # )
        self.frontLeftmotor = wpilib.Talon(constants.DriveConstants.kLeftMotor1Port)
        self.backLeftmotor = wpilib.Talon(constants.DriveConstants.kLeftMotor2Port)
        self.frontRightmotor = wpilib.Talon(constants.DriveConstants.kRightMotor1Port)
        self.backRightmotor = wpilib.Talon(constants.DriveConstants.kRightMotor2Port)


        # The robot's drive
        self.drive = wpilib.drive.MecanumDrive(self.frontLeftmotor, self.backLeftmotor, self.frontRightmotor, self.backRightmotor)
        # self.drive = wpilib.drive.DifferentialDrive(self.leftMotors, self.rightMotors)

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
        # self.rightMotors.setInverted(True)
        # TODO: is this needed for mechanum drive? looks yes
        self.frontRightmotor.setInverted(True)
        self.backRightmotor.setInverted(True)

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

    # TODO: fix the fwd and rot variable names
    def driveCartesian(self, xSpeed: float, ySpeed: float, zRotation: float):
        """
        Drives the robot using cartesian controls.

        :param xSpeed: the speed that the robot should drive in the X direction. [-1.0..1.0]

        :param ySpeed: the speed that the robot should drive in the Y direction. This input is
                          inverted to match the forward == -1.0 that joysticks produce. [-1.0..1.0]

        :param zRotation: the rate of rotation for the robot that is independent of translation. [-1.0..1.0]
        """
        SmartDashboard.putString("Drive Status", f'Arcade Mode, {xSpeed=}, {ySpeed=}')
        self.drive.driveCartesian(xSpeed=xSpeed,ySpeed=ySpeed,zRotation=zRotation) #.arcadeDrive(fwd, rot)
    
    def driveDistance(self, distance: float):
        
        avg_speed = 0.5 #ft/s
        SmartDashboard.putString("Drive Status", f'Driving {distance/avg_speed=} seconds')
        self.drive.drivePolar(magnitude=1, angle=Rotation2d(0),zRotation=0.0)
        
        SmartDashboard.putString("Drive Status", f'Just Drove {distance=} ?feet?')
        # if self.getAverageEncoderDistance() >= distance:
        #     self.drive.arcadeDrive(0, 0)
        #     return True
        # return False



