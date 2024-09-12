
#restart of robot
#create a mechanicum robot with:
# a cannon that is fired by a servo releasing pressure from a prep-tank
# the prep-tank is charged by a reserve tank
# the reserve tank is charged by a pump
# the robot is driven by an Xbox controller

#region imports
import subsystems.cannon
import subsystems.drivetrain
import subsystems.safeandarm
import wpilib
from wpilib import (SmartDashboard, 
                    # SendableChooser, 
                    # CameraServer, 
                    # DigitalInput, 
                    # DoubleSolenoid, 
                    # Joystick, 
                    # Servo, 
                    # Timer, 
                    # VictorSP,
                    # XboxController,
                    # Compressor,
                    # AnalogInput,
                    # Encoder,
                    Field2d,
                    
                    

                    )
import commands2
from commands2 import CommandScheduler
# from constants import ()
import typing
# import ntcore

import subsystems
import constants
# from commands.driving  import DriveByController





#endregion

#region robot class
class MyRobot(commands2.TimedCommandRobot):
    #region robotInit
    def robotInit(self) -> None:
        """
        This function is run when the robot is first started up and should be used for any
        initialization code.
        """
        self.autonomousCommand: typing.Optional[commands2.Command] = None

        #region subsystems init
        self.cannon = subsystems.cannon.Cannon()
        self.drivetrain = subsystems.drivetrain.Drivetrain()
        self.drive = self.drivetrain.drive
        self.safeandarm = subsystems.safeandarm.SafeAndArm()
    
        #endregion subsystem init


        #region Controller init
        self.driver1Controller = commands2.button.CommandXboxController(
            constants.OIConstants.kDriver1ControllerPort
        )

        #endregion controller init

        #region default commands

        self.drivetrain.setDefaultCommand(self.drivetrain.DriveByController(drivetrain= self.drivetrain, controller= self.driver1Controller))
        
        #endregion default commands

        #region SmartDashboard init

        SmartDashboard.putData(CommandScheduler.getInstance())
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)

        SmartDashboard.putData("Cannon", self.cannon)
        SmartDashboard.putData("Drivetrain", self.drivetrain)
        SmartDashboard.putData("SafeAndArm", self.safeandarm)

        #region Smart dashboard chooser for autonomous
        self.auto_chooser = wpilib.SendableChooser()
        self.auto_chooser.setDefaultOption("Charge and Shoot", self.cannon.Charge_Shoot)
        self.auto_chooser.addOption("Drive 1ft", self.drivetrain.auto_drive_1ft)
        SmartDashboard.putData(self.auto_chooser)
        # def get_auto_command():
        #     return self.auto_chooser.getSelected()
        #endregion



        #endregion SmartDashboard init


    #region disabled
    def disabledInit(self) -> None:
        """This function is called once each time the robot enters Disabled mode."""

    def disabledPeriodic(self) -> None:
        """This function is called periodically when disabled"""

    #endregion

    #region autonomous
    def autonomousInit(self) -> None:
        """This autonomous runs the autonomous command selected by your RobotContainer class."""
        self.auto_chooser.getSelected()
    
    def autonomousPeriodic(self) -> None:
        """This function is called periodically during autonomous"""
    
    #endregion

    #region teleop
    def teleopInit(self) -> None:
        """This function is called once each time the robot enters teleop mode."""
        
    def teleopPeriodic(self) -> None:
        """This function is called periodically during operator control"""
        
        

    #endregion

    #region test
    def testInit(self) -> None:
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self) -> None:
        """This function is called periodically during test mode."""

    #endregion

    #region Xbox controller bindings
    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands2.button.CommandGenericHID or one of its
        subclasses (commands2.button.CommandJoystick or command2.button.CommandXboxController).
        """

        # Configure your button bindings here

        # We can bind commands while retaining references to them in RobotContainer

        # Spin up the shooter when the 'A' button is pressed
        # self.driver1Controller.a().onTrue(self.armCannon)

        # Turn off the shooter when the 'B' button is pressed
        # self.driver1Controller.b().onTrue(self.abortArm)

        pass

        

    #endregion





