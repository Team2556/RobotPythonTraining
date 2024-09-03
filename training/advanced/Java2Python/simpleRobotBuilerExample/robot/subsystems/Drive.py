# RobotBuilder Version: 6.1
#
# This file was generated by RobotBuilder. It contains sections of
# code that are automatically generated and assigned by robotbuilder.
# These sections will be updated in the future when you export to
# Python from RobotBuilder. Do not put any code or make any change in
# the blocks indicating autogenerated code or it will be lost on an
# update. Deleting the comments indicating the section will prevent
# it from being updated in the future.

# ROBOTBUILDER TYPE: PIDSubsystem.

import wpilib
from wpilib import Encoder, NidecBrushless
from wpilib.drive import MecanumDrive
from wpilib.controller import PIDController
from wpilib2.command import PIDSubsystem

class Drive(PIDSubsystem):

    # Initialize your subsystem here
    def __init__(self):
        # PID Variables
        kP = 1.0
        kI = 0.0
        kD = 0.0
        kF = 0.0

        super().__init__(PIDController(kP, kI, kD))
        self.getController().setTolerance(0.2)

        # Encoder
        self.indexedEncoder1 = Encoder(0, 1, False)
        self.indexedEncoder1.setDistancePerPulse(1.0)
        self.indexedEncoder1.setIndexSource(2, Encoder.IndexingType.kResetOnRisingEdge)

        # Motors
        self.drive_motor_right_rear = NidecBrushless(2, 5)
        self.drive_motor_right_rear.setInverted(False)

        self.drive_motor_left_rear = NidecBrushless(3, 6)
        self.drive_motor_left_rear.setInverted(True)

        self.drive_motor_right = NidecBrushless(0, 3)
        self.drive_motor_right.setInverted(False)

        self.drive_motor_left = NidecBrushless(1, 4)
        self.drive_motor_left.setInverted(True)

        # Mecanum Drive
        self.mecanumDrive = MecanumDrive(self.drive_motor_left, self.drive_motor_left_rear,
                                         self.drive_motor_right, self.drive_motor_right_rear)
        self.mecanumDrive.setSafetyEnabled(True)
        self.mecanumDrive.setExpiration(0.1)
        self.mecanumDrive.setMaxOutput(1.0)

    def periodic(self):
        # This method will be called once per scheduler run
        super().periodic()

    def simulationPeriodic(self):
        # This method will be called once per scheduler run when in simulation
        pass

    def getMeasurement(self):
        return self.indexedEncoder1.getRate()

    def useOutput(self, output, setpoint):
        output += setpoint * kF
        self.drive_motor_right_rear.set(output)