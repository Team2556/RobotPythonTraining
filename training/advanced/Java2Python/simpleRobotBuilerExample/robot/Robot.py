# RobotBuilder Version: 6.1
#
# This file was generated by RobotBuilder. It contains sections of
# code that are automatically generated and assigned by robotbuilder.
# These sections will be updated in the future when you export to
# Python from RobotBuilder. Do not put any code or make any change in
# the blocks indicating autogenerated code or it will be lost on an
# update. Deleting the comments indicating the section will prevent
# it from being updated in the future.

# ROBOTBUILDER TYPE: Robot.

import wpilib
from wpilib import TimedRobot
from wpilib2.command import Command, CommandScheduler

class Robot(TimedRobot):

    def __init__(self):
        super().__init__()
        self.m_autonomousCommand = None
        self.m_robotContainer = None

    def robotInit(self):
        # Instantiate our RobotContainer. This will perform all our button bindings, and put our
        # autonomous chooser on the dashboard.
        self.m_robotContainer = RobotContainer.getInstance()
        wpilib.HAL.report(wpilib.HAL.tResourceType.kResourceType_Framework, wpilib.HAL.tInstances.kFramework_RobotBuilder)
        self.enableLiveWindowInTest(True)

    def robotPeriodic(self):
        # Runs the Scheduler. This is responsible for polling buttons, adding newly-scheduled
        # commands, running already-scheduled commands, removing finished or interrupted commands,
        # and running subsystem periodic() methods. This must be called from the robot's periodic
        # block in order for anything in the Command-based framework to work.
        CommandScheduler.getInstance().run()

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        self.m_autonomousCommand = self.m_robotContainer.getAutonomousCommand()

        # schedule the autonomous command (example)
        if self.m_autonomousCommand is not None:
            self.m_autonomousCommand.schedule()

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        if self.m_autonomousCommand is not None:
            self.m_autonomousCommand.cancel()

    def teleopPeriodic(self):
        pass

    def testInit(self):
        # Cancels all running commands at the start of test mode.
        CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self):
        pass