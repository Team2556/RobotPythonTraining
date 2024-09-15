#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
from wpilib import (SmartDashboard, Field2d)
import wpilib.drive
import rev
# from pyfrc.physics.drivetrains import MecanumDrivetrain
import commands2
from commands2 import CommandScheduler
import wpimath
from wpimath.geometry import Translation2d, Rotation2d
from constants import (DriveConstant,
                       OIConstant,
                       )
import phoenix5
import math
# import ctre



#region Helper functions
def rotate_45_degrees(x, y):
        radians = math.radians(45)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x_new = x * cos_angle - y * sin_angle
        y_new = x * sin_angle + y * cos_angle
        return x_new, y_new
#endregion Helper functions
class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.frontLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor1Port)
        self.backLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor2Port)
        self.frontRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor1Port)
        self.backRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor2Port)
        # self.frontLeftMotor = 
        #rev.CANSparkMax(DriveConstant.kLeftMotor1Port, rev.CANSparkMax.MotorType.kBrushless)
        # self.leftDrive = rev.CANSparkMax(DriveConstant.kLeftMotor2Port, rev.CANSparkMax.MotorType.kBrushless)
        # self.frontRightMotor = rev.CANSparkMax(DriveConstant.kRightMotor1Port, rev.CANSparkMax.MotorType.kBrushless)
        # self.rightDrive = rev.CANSparkMax(DriveConstant.kRightMotor2Port, rev.CANSparkMax.MotorType.kBrushless)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        self.frontRightMotor.setInverted(True)
        self.backRightMotor.setInverted(True)

        self.robotDrive = wpilib.drive.MecanumDrive(self.frontLeftMotor, self.frontRightMotor, self.backLeftMotor, self.backRightMotor)
        # .DifferentialDrive(
        #     self.frontLeftMotor, self.frontRightMotor
        # )
        self.controller = wpilib.XboxController(OIConstant.kDriver1ControllerPort)
        self.timer = wpilib.Timer()

        #region SmartDashboard init

        SmartDashboard.putData(CommandScheduler.getInstance())
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)
        #endregion SmartDashBoard init


        # Initialize the Pigeon IMU
        # self.pigeon = ctre.sensors.    WPI_PigeonIMU(DriveConstant.kPigeonPort)
        # self.pigeon.setFusedHeading(0.0)  # Reset the heading to zero

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.robotDrive.driveCartesian(0.5, 0, 0)
        else:
            self.robotDrive.stopMotor()  # Stop robot

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""


    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""
        self.robotDrive .driveCartesian(
            *(-self.controller.getLeftY(), self.controller.getRightX()), #rotate_45_degrees
            self.controller.getLeftX(), Rotation2d(0) )
            
  

    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wpilib.run(MyRobot)