#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import wpilib
import commands2
import commands2.cmd
import commands2.button
from wpilib import SmartDashboard, Field2d
SmartDashboard.putBoolean("Bridge Limit", False)
SmartDashboard.putNumber("Bridge Angle", 900)

import constants
import subsystems.drivesubsystem
import subsystems.shootersubsystem

from constants import AutoConstants, RobotArmStates
import ntcore


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.

    """

    def __init__(self):
        self.robotDrive = subsystems.drivesubsystem.DriveSubsystem()
        SmartDashboard.putData(self.robotDrive)
        self.charger = subsystems.shootersubsystem.CannonChargeSubsystem()
        SmartDashboard.putData(self.charger)
        self.shooter = subsystems.shootersubsystem.FireSubsystem()
        SmartDashboard.putData(self.shooter)
        

        #self.sd = ntcore.NetworkTableInstance.getDefault().getTable("SmartDashboard")
        self.ArmState = RobotArmStates.DISARMED


        # self.spinUpShooter = commands2.cmd.runOnce(self.shooter.enable, self.shooter)
        # self.stopShooter = commands2.cmd.runOnce(self.shooter.disable, self.shooter)

        # A routine that recharges to prep-tank 
        self.armCannon = commands2.cmd.sequence(
            # commands2.cmd.runOnce(self.charger.enable, self.charger), # are there safety checks could put in
            commands2.cmd.runOnce(self.charger.charge, self.charger),
            commands2.cmd.waitSeconds(constants.AutoConstants.kAutoChargeTimeSeconds),
            commands2.cmd.runOnce(self.charger.seal, self.charger),
            commands2.cmd.runOnce(lambda: setattr(self,'ArmState',RobotArmStates.ARMED), self.charger),
            # self.sd.putString("gameData", f'Cannon Armed: {self.ArmState=}'),
            # commands2.cmd.runOnce(self.arm.disable, self.charger),
        )
        # SmartDashboard.putData("Arm Cannon", self.armCannon)

        # A routine to interrupt arming and abort the arming process
        self.abortArm = commands2.cmd.sequence(
            commands2.cmd.runOnce(self.charger.seal, self.charger),
            commands2.cmd.runOnce(lambda: setattr(self, 'ArmState', RobotArmStates.DISARMED), self.charger),
            ) #
        # SmartDashboard.putData("Abort Arm", self.abortArm)  

        # An autonomous routine charges and shoots cannon
        self.Charge_Shoot = commands2.cmd.sequence(
            commands2.cmd.runOnce(self.charger.charge, self.charger),
            commands2.cmd.waitSeconds(constants.AutoConstants.kAutoChargeTimeSeconds),
            commands2.cmd.runOnce(self.shooter.fire, self.shooter),
            commands2.cmd.waitSeconds(constants.AutoConstants.kAutoShootTimeSeconds),
            commands2.cmd.runOnce(self.shooter.finish_fire, self.shooter),
            commands2.cmd.runOnce(lambda: setattr(self, 'ArmState',RobotArmStates.DISARMED), self.charger),
        )
        SmartDashboard.putData("Charge and Shoot", self.Charge_Shoot)

         # An Autonomuous command to drive forward
        self.auto_drive_1ft = commands2.cmd.runOnce(self.robotDrive.driveDistance(1.0), self.robotDrive)
        SmartDashboard.putData("Drive 1ft", self.auto_drive_1ft)

        self.auto_chooser = wpilib.SendableChooser()
        self.auto_chooser.setDefaultOption("Charge and Shoot", self.Charge_Shoot)
        self.auto_chooser.addOption("Drive 1ft", self.auto_drive_1ft)
        SmartDashboard.putData(self.auto_chooser)
        def get_auto_command():
            return self.auto_chooser.getSelected()
        
        #     # Start the command by spinning up the shooter...
        #     commands2.cmd.runOnce(self.shooter.enable, self.shooter),
        #     # Wait until the shooter is at speed before feeding the frisbees
        #     commands2.cmd.waitUntil(lambda: self.shooter.getController().atSetpoint()),
        #     # Start running the feeder
        #     commands2.cmd.runOnce(self.shooter.runFeeder, self.shooter),
        #     # Shoot for the specified time
        #     commands2.cmd.waitSeconds(constants.AutoConstants.kAutoShootTimeSeconds)
        #     # Add a timeout (will end the command if, for instance, the shooter
        #     # never gets up to speed)
        #     .withTimeout(constants.AutoConstants.kAutoTimeoutSeconds)
        #     # When the command ends, turn off the shooter and the feeder
        #     .andThen(
        #         commands2.cmd.runOnce(
        #             lambda: self.shooter.disable, self.shooter
        #         ).andThen(
        #             commands2.cmd.runOnce(lambda: self.shooter.stopFeeder, self.shooter)
        #         )
        #     ),
        # )

        self.driverController = commands2.button.CommandXboxController(
            constants.OIConstants.kDriverControllerPort
        )

        # Configure the button bindings
        self.configureButtonBindings()

        # Configure default commands
        # Set the default drive command to split-stick arcade drive
        self.robotDrive.setDefaultCommand(
            # A split-stick arcade command, with forward/backward controlled by the left
            # hand, and turning controlled by the right.
            commands2.cmd.run(
                lambda: self.robotDrive.arcadeDrive(
                    -self.driverController.getLeftY(),
                    -self.driverController.getLeftX(),
                ),
                self.robotDrive,
            ).andThen(self.robotDrive.getAverageEncoderDistance() )
        )

    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can be created via the button
        factories on commands2.button.CommandGenericHID or one of its
        subclasses (commands2.button.CommandJoystick or command2.button.CommandXboxController).
        """

        # Configure your button bindings here

        # We can bind commands while retaining references to them in RobotContainer

        # Spin up the shooter when the 'A' button is pressed
        self.driverController.a().onTrue(self.armCannon)

        # Turn off the shooter when the 'B' button is pressed
        self.driverController.b().onTrue(self.abortArm)

        # We can also write them as temporary variables outside the bindings

        # Shoots if the prep-tank is finished charging
        shoot = commands2.cmd.sequence((self.shooter.fire, self.shooter),
                                   commands2.cmd.waitSeconds(.07),
                                   commands2.cmd.runOnce(self.shooter.finish_fire, self.shooter),
                                   commands2.cmd.runOnce(lambda: setattr(self, 'ArmState', RobotArmStates.DISARMED), self.charger),
                                #    runOnce(lambda: setattr(self, 'ArmState', RobotArmStates.DISARMED), self.charger)
                                   )
        
        #     # Do nothing
        #     commands2.cmd.none(),
        #     # Determine which of the above to do based on whether the shooter has reached the
        #     # desired speed
        #     lambda: self.shooter.getController().atSetpoint(),
        # )

        # stopFeeder = commands2.cmd.runOnce(self.shooter.stopFeeder, self.shooter)

        # Shoot when the 'X' button is pressed
        self.driverController.x().onTrue(shoot)#.onFalse(charge)

        # We can also define commands inline at the binding!

        # While holding the shoulder button, drive at half speed
        # self.driverController.rightBumper().onTrue(
        #     commands2.cmd.runOnce(
        #         lambda: self.robotDrive.setMaxOutput(0.5), self.robotDrive
        #     )
        # ).onFalse(
        #     commands2.cmd.runOnce(
        #         lambda: self.robotDrive.setMaxOutput(1), self.robotDrive
        #     )
        # )

    def getAutonomousCommand(self) -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot` class.

        :returns: the command to run in autonomous
        """
        return self.auto_chooser.getSelected()
        
    