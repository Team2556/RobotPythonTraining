#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
# import wpimath.controller
import commands2
import commands2.cmd
from wpilib import SmartDashboard

import try3_bust_with_poenix.constants as constants


# Robot will have a cannon connected to a large pneumatic cylinder, called prep-tank
# Cannon prep-tank will be charged by pressurized air in the reservoir
# Charging will be achieved by opening a solenoid that will allow the air to flow into the prep-tank from the reservoir
class CannonChargeSubsystem(commands2.Subsystem): # Pneumatics controller
    def __init__(self) -> None:
        super().__init__()
        self.cannonChargeSolenoid = wpilib.Solenoid(moduleType= wpilib.PneumaticsModuleType.REVPH,
                                                    channel=constants.CannonConstants.kCannonChargeSolenoidPort)
        self.cannonChargeSolenoid.set(False)  
        SmartDashboard.putString("Cannon Status", f'Cannon Initialized')


    def charge(self): # Charge the cannon, safety gates handled in the command
        self.cannonChargeSolenoid.set(True)
        SmartDashboard.putString("Cannon Status", f'Cannon Charging prep-tank')
        SmartDashboard.putString("Safe&Arm Status", f'Firing System Armed')

    def seal(self):
        self.cannonChargeSolenoid.set(False)
        SmartDashboard.putString("Cannon Status", f'Cannon pre-tank Sealed')


# class ShooterSubsystem(commands2.PIDSubsystem):
#     def __init__(self) -> None:
#         super().__init__(
#             wpimath.controller.PIDController(
#                 constants.ShooterConstants.kP,
#                 constants.ShooterConstants.kI,
#                 constants.ShooterConstants.kD,
#             )
#         )

#         self.shooterMotor = wpilib.PWMSparkMax(
#             constants.ShooterConstants.kShooterMotorPort
#         )
#         self.feederMotor = wpilib.PWMSparkMax(
#             constants.ShooterConstants.kFeederMotorPort
#         )
#         self.shooterEncoder = wpilib.Encoder(
#             constants.ShooterConstants.kEncoderPorts[0],
#             constants.ShooterConstants.kEncoderPorts[1],
#             constants.ShooterConstants.kEncoderReversed,
#         )
#         self.shooterFeedForward = wpimath.controller.SimpleMotorFeedforwardMeters(
#             constants.ShooterConstants.kSVolts,
#             constants.ShooterConstants.kVVoltSecondsPerRotation,
#         )
#         self.getController().setTolerance(
#             constants.ShooterConstants.kShooterToleranceRPS
#         )
#         self.shooterEncoder.setDistancePerPulse(constants.ShooterConstants.kEncoderCPR)
#         self.setSetpoint(constants.ShooterConstants.kShooterTargetRPS)

#     def useOutput(self, output: float, setpoint: float):
#         self.shooterMotor.setVoltage(
#             output + self.shooterFeedForward.calculate(setpoint)
#         )

#     def getMeasurement(self) -> float:
#         return self.shooterEncoder.getRate()

#     def runFeeder(self):
#         self.feederMotor.set(constants.ShooterConstants.kFeederSpeed)

#     def stopFeeder(self):
#         self.feederMotor.set(0)

# The firing will be achieved by a solenoid that will release the pressurized air from the prep-tank
class FireSubsystem(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.fireSolenoid = wpilib.Solenoid(moduleType= wpilib.PneumaticsModuleType.REVPH,
                                            channel=constants.ShooterConstants.kFireSolenoidPort)
        # self.retractSolenoid = wpilib.Solenoid(constants.FireConstants.kRetractSolenoidPort)
        self.fireSolenoid.set(False)
        # self.retractSolenoid.set(True)
        SmartDashboard.putString("Safe&Arm Status", f'Firing System Initialized')

    def fire(self):
        self.fireSolenoid.set(True)
        # self.retractSolenoid.set(False)
        SmartDashboard.putString("Safe&Arm Status", f'Firing System Engaged')

    def finish_fire(self):
        self.fireSolenoid.set(False)
        # self.retractSolenoid.set(True)
        SmartDashboard.putString("Safe&Arm Status", f'Firing System Finished')
        SmartDashboard.putString("Cannon Status", f'Cannon pre-tank Discharged (at least should be)')

