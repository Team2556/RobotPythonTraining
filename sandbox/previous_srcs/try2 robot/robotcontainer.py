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

import subsystems.cannonsubsystem
SmartDashboard.putBoolean("Bridge Limit", False)
SmartDashboard.putNumber("Bridge Angle", 900)

import try3_bust_with_poenix.constants as constants
import subsystems.drivesubsystem
import subsystems.shootersubsystem

from try3_bust_with_poenix.constants import AutoConstants, RobotArmStates
import ntcore


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.

    """

    def __init__(self):

        #region Dashboard 
        self.robotDrive = subsystems.drivesubsystem.DriveSubsystem()
        SmartDashboard.putData(self.robotDrive)
        SmartDashboard.putData("drive type?", self.robotDrive.drive)
        self.charger = subsystems.shootersubsystem.CannonChargeSubsystem()
        SmartDashboard.putData(self.charger)
        self.shooter = subsystems.shootersubsystem.FireSubsystem()
        SmartDashboard.putData(self.shooter)
        self.lift = subsystems.cannonsubsystem.CannonLift()
        SmartDashboard.putData(self.lift)

        ## Smart Dashboard cannon representation
        self.sdCannonMech = wpilib.Mechanism2d(width=1,height=.1, backgroundColor= wpilib.Color8Bit(wpilib.Color.kAliceBlue))
        self.sdCannonRoot = self.sdCannonMech.getRoot(name="Cannon", x=.5, y=0.1)
        self.sdCannonBarrel = self.sdCannonRoot.appendLigament(name="Barrel", length=2, angle=15, color=wpilib.Color8Bit(wpilib.Color.kBlueViolet))

        SmartDashboard.putData("Cannon", self.sdCannonMech)
        #endregion

        
        # self.ArmState = RobotArmStates.DISARMED

    
        #region prep-tank 

        self.armCannon = commands2.cmd.sequence(
            # commands2.cmd.runOnce(self.charger.enable, self.charger), # are there safety checks could put in
            commands2.cmd.runOnce(self.charger.charge, self.charger),
            commands2.cmd.waitSeconds(constants.AutoConstants.kAutoChargeTimeSeconds),
            commands2.cmd.runOnce(self.charger.seal, self.charger),
            commands2.cmd.runOnce(lambda: setattr(self,'ArmState',RobotArmStates.ARMED), self.charger),
            # self.sd.putString("gameData", f'Cannon Armed: {self.ArmState=}'),
            # commands2.cmd.runOnce(self.arm.disable, self.charger),
        )

        # A routine to interrupt arming and abort the arming process
        self.abortArm = commands2.cmd.sequence(
            commands2.cmd.runOnce(self.charger.seal, self.charger),
            commands2.cmd.runOnce(lambda: setattr(self, 'ArmState', RobotArmStates.DISARMED), self.charger),
            ) #
        #endregion

        #region Autonomous

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

        #Smart dashboard chooser for autonomous
        self.auto_chooser = wpilib.SendableChooser()
        self.auto_chooser.setDefaultOption("Charge and Shoot", self.Charge_Shoot)
        self.auto_chooser.addOption("Drive 1ft", self.auto_drive_1ft)
        SmartDashboard.putData(self.auto_chooser)
        #endregion

        #region Cannon Lift

        # command for moving the cannon via the lifter
        self.cannon_lift_up = commands2.cmd.runOnce(self.lift.setMotorSpeed(.25), self.lift)
        SmartDashboard.putData("Cannon Lift Up", self.cannon_lift_up)
        self.cannon_lift_down = commands2.cmd.runOnce(self.lift.setMotorSpeed(-.25), self.lift)
        SmartDashboard.putData("Cannon Lift Down", self.cannon_lift_down)
        
        def get_auto_command():
            return self.auto_chooser.getSelected()
        
        # the sim starts off moving the robot, so we need to stop it (or get rid of the default comand or add gate check if in teleop)
        self.robotDrive.driveCartesian(0,0,0)

        #endregion


        
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

        #region xbox Controller

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
                lambda: self.robotDrive.driveCartesian(
                    xSpeed=-self.driverController.getLeftY(),
                    ySpeed=self.driverController.getLeftX(),
                    zRotation=self.driverController.getLeftTriggerAxis()
                # lambda: self.robotDrive.arcadeDrive(
                #     -self.driverController.getLeftY(),
                #     self.driverController.getLeftX(),
                ),
                self.robotDrive,
            ).andThen(self.robotDrive.getAverageEncoderDistance() ) # TODO: fix avg encoder for mechanum
        )
        self.lift.setDefaultCommand(
            commands2.cmd.runOnce(
                lambda: self.lift.setMotorSpeed(-.10),
                self.lift
            ).andThen(self.lift.encoder.getDistance()).andThen(self.lift.encoder.getDistance())
        )
        #endregion

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

        self.driverController.povUp().onTrue( self.cannon_lift_up)
        self.driverController.povDown().onTrue(self.cannon_lift_down)
        #lambda: self.sdCannonBarrel.setAngle(self.driverController.getRightX().get()*90))

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
        #endregion

    def getAutonomousCommand(self) -> commands2.Command:
        """
        Use this to pass the autonomous command to the main :class:`.Robot` class.

        :returns: the command to run in autonomous
        """
        return self.auto_chooser.getSelected()
        
    