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
from subsystems.drivetrain import DriveTrain


#region Helper functions

#endregion Helper functions
class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        CommandScheduler.getInstance().run()
        

        self.robotDrive = DriveTrain()

        self.driverController = commands2.button.CommandXboxController(
            OIConstant.kDriver1ControllerPort)
        # Configure the button bindings
        self.ConfigureButtonBindings()

        self.robotDrive.setDefaultCommand(commands2.cmd.run(lambda: self.robotDrive.driveWithJoystick(self.driverController)
                                                            , self.robotDrive))
        self.timer = wpilib.Timer()

        #region SmartDashboard init

        SmartDashboard.putData(CommandScheduler.getInstance())
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)
        #endregion SmartDashBoard init


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""
        # if self.autonomousCommand is not None:
        #     self.autonomousCommand.cancel()


    def teleopPeriodic(self):
        """This function is called periodically during teleoperated mode."""

    def testInit(self):
        """This function is called once each time the robot enters test mode."""
        commands2.CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self):
        """This function is called periodically during test mode."""

    def ConfigureButtonBindings(self):
        self.driverController.povLeft().onTrue(lambda: self.robotDrive.slowLeft(self.driverController))
        self.driverController.povRight().onTrue(lambda: self.robotDrive.slowRight(self.driverController))

        OnlyFrontLeft = commands2.SequentialCommandGroup(
            commands2.cmd.run(lambda: self.robotDrive.OnlyFrontLeft()).raceWith(
                commands2.WaitCommand(2.2)))
        self.driverController.x().onTrue(OnlyFrontLeft)


        OnlyFrontRight = (commands2.cmd.run(lambda: self.robotDrive.OnlyFrontRight())
                          .raceWith(commands2.WaitCommand(1.2))
                          .andThen(commands2.WaitCommand(0.5))
                          .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyFrontRight())
                          .raceWith(commands2.WaitCommand(1.2)))
                          )
        self.driverController.y().onTrue(OnlyFrontRight)

        OnlyBackLeft = (commands2.cmd.run(lambda: self.robotDrive.OnlyBackLeft())
                        .raceWith(commands2.WaitCommand(.7))
                        .andThen(commands2.WaitCommand(0.5))
                        .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyBackLeft())
                        .raceWith(commands2.WaitCommand(.7)))
                        .andThen(commands2.WaitCommand(0.5))
                        .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyBackLeft())
                        .raceWith(commands2.WaitCommand(.7)))
                        )
        self.driverController.a().onTrue(OnlyBackLeft)

        OnlyBackRight = (commands2.cmd.run(lambda: self.robotDrive.OnlyBackRight())
                         .raceWith(commands2.WaitCommand(.4))
                         .andThen(commands2.WaitCommand(0.35))
                         .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyBackRight())
                         .raceWith(commands2.WaitCommand(.4)))
                         .andThen(commands2.WaitCommand(0.35))
                         .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyBackRight())
                         .raceWith(commands2.WaitCommand(.4)))
                         .andThen(commands2.WaitCommand(0.35))
                         .andThen(commands2.cmd.run(lambda: self.robotDrive.OnlyBackRight())
                         .raceWith(commands2.WaitCommand(.4)))
                         )
        self.driverController.b().onTrue(OnlyBackRight)

        


        
