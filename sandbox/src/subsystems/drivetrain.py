import commands2

import wpilib
from wpilib import SmartDashboard
import wpilib.drive
import wpimath
from wpimath.geometry import Rotation2d
import phoenix5

from constants import DriveConstant

class DriveTrain(commands2.Subsystem):
    def __init__(self) -> None:
        """Creates a new DriveSubsystem"""
        super().__init__()

        # The motors on the left side of the drive.
        
        self.frontLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor1Port)
        # self.sim_frontLeftMotor = self.frontLeftMotor.getSimCollection()#phoenix5.TalonSRXSimCollection()
        SmartDashboard.putData("frontLeftMotor", self.frontLeftMotor)
        self.frontRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor1Port)
        SmartDashboard.putData("frontRightMotor", self.frontRightMotor)
        self.backLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor2Port)
        SmartDashboard.putData("backLeftMotor", self.backLeftMotor)
        self.backRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor2Port)
        SmartDashboard.putData("backRightMotor", self.backRightMotor)

        self.robotDrive = wpilib.drive.MecanumDrive(self.frontLeftMotor, 
                                                    self.frontRightMotor, 
                                                    self.backLeftMotor, 
                                                    self.backRightMotor)     
        self.robotDrive.setDeadband(0.1)
        self.robotDrive.setMaxOutput(0.60)
        self.robotDrive.setExpiration(.1)
        # self.frontLeftMotor.configPeakOutputForward(.6)
        # self.frontLeftMotor.configPeakOutputReverse(-.6)
        # self.frontRightMotor.configPeakOutputForward(.6)
        # self.frontRightMotor.configPeakOutputReverse(-.6)
        # self.backLeftMotor.configPeakOutputForward(.6)
        # self.backLeftMotor.configPeakOutputReverse(-.6)
        # self.backRightMotor.configPeakOutputForward(.6)
        # self.backRightMotor.configPeakOutputReverse(-.6)   

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        
        # TODO: is it juet sim or do these not need to be inverted?
        # self.frontRightMotor.setInverted(True)
        # self.backRightMotor.setInverted(True)


    def driveWithJoystick(self, joystick: wpilib.Joystick):
        """Drives the robot using the joystick"""
        self.robotDrive.driveCartesian(-joystick.getLeftY(), -joystick.getLeftTriggerAxis(), -joystick.getLeftX(), Rotation2d(0))
    def slowLeft(self,joystick: wpilib.Joystick) -> None:
        self.robotDrive.driveCartesian(0, 0, -.22, Rotation2d(0))
    def slowRight(self,joystick: wpilib.Joystick) -> None:
        self.robotDrive.driveCartesian(0, 0, .22, Rotation2d(0))
    def OnlyFrontLeft(self) -> None:
        self.frontLeftMotor.set(0.51)
    def OnlyFrontRight(self) -> None:
        self.frontRightMotor.set(0.52)
    def OnlyBackLeft(self) -> None:
        self.backLeftMotor.set(0.53)
    def OnlyBackRight(self) -> None:
        self.backRightMotor.set(0.54)
