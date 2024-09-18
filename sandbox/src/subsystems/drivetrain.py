import commands2
# from commands2 import Subsystem, CommandScheduler

import wpilib
from wpilib import SmartDashboard
import wpilib.drive
# import wpimath
from wpimath.geometry import Rotation2d

import phoenix5

from constants import DriveConstant

import typing

class DriveTrain(commands2.Subsystem):
    def __init__(self) -> None:
        """Creates a new DriveSubsystem"""
        super().__init__()
        # Register the subsystem with the CommandScheduler
        # CommandScheduler.getInstance().registerSubsystem(self) when calling it in robot it registers it

        self.right_invert_YN = True

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how the robot's
        # gearbox is constructed, you might have to invert the left side instead.    
        self.frontLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor1Port)
        SmartDashboard.putData("frontLeftMotor -from drivetrain", self.frontLeftMotor)
        self.frontRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor1Port)
        # self.frontRightMotor.getSimCollection().getMotorOutputLeadVoltage()
        self.frontRightMotor.setInverted(self.right_invert_YN)
        SmartDashboard.putData("frontRightMotor -from drivetrain", self.frontRightMotor)
        self.backLeftMotor = phoenix5.WPI_TalonSRX(DriveConstant.kLeftMotor2Port)
        SmartDashboard.putData("backLeftMotor -from drivetrain", self.backLeftMotor)
        self.backRightMotor = phoenix5.WPI_TalonSRX(DriveConstant.kRightMotor2Port)
        self.backRightMotor.setInverted(self.right_invert_YN)
        SmartDashboard.putData("backRightMotor -from drivetrain", self.backRightMotor)
        ''' not using encoder yet
        # Set up encoders for each motor
        self.frontLeftEncoder = self.frontLeftMotor.getSensorCollection().getQuadraturePosition
        SmartDashboard.putNumber("frontLeftEncoder -from drivetrain", self.frontLeftEncoder())
        self.frontRightEncoder = self.frontRightMotor.getSensorCollection().getQuadraturePosition
        self.backLeftEncoder = self.backLeftMotor.getSensorCollection().getQuadraturePosition
        self.backRightEncoder = self.backRightMotor.getSensorCollection().getQuadraturePosition

        # Reset encoders to zero
        self.frontLeftMotor.getSensorCollection().setQuadraturePosition(0, 10)
        self.frontRightMotor.getSensorCollection().setQuadraturePosition(0, 10)
        self.backLeftMotor.getSensorCollection().setQuadraturePosition(0, 10)
        self.backRightMotor.getSensorCollection().setQuadraturePosition(0, 10)
        '''
        if DriveConstant.kIsMecanum:
            self.robotDrive = wpilib.drive.MecanumDrive(frontLeftMotor= self.frontLeftMotor, 
                                                        frontRightMotor=self.frontRightMotor, 
                                                        rearLeftMotor=self.backLeftMotor, 
                                                        rearRightMotor=self.backRightMotor)
        else:
            self.backLeftMotor.follow(self.frontLeftMotor)
            self.backRightMotor.follow(self.frontRightMotor)
            self.robotDrive = wpilib.drive.DifferentialDrive(self.frontLeftMotor, self.frontRightMotor)
        
        
        self.robotDrive.setMaxOutput(0.60)
        '''rest are defaults so far:
        self.robotDrive.setDeadband(0.02)
        self.robotDrive.setExpiration(.05)'''


    def periodic(self) -> None:
        """This method will be called once per scheduler run"""
        # Add code here that needs to run periodically
        # SmartDashboard.putNumber("frontLeftMotor -from drivetrain getmotoroutputpercent", self.frontLeftMotor.getMotorOutputPercent())
        # SmartDashboard.putNumber("frontRightMotor -from drivetrain getmotoroutputpercent", self.frontRightMotor.getMotorOutputPercent())
        # SmartDashboard.putNumber("backLeftMotor -from drivetrain getmotoroutputpercent", self.backLeftMotor.getMotorOutputPercent())
        # SmartDashboard.putNumber("backRightMotor -from drivetrain getmotoroutputpercent", self.backRightMotor.getMotorOutputPercent())

        # SmartDashboard.putData("robotDrive -from drivetrain periodic", self.robotDrive)  


    def driveWithJoystick(self, joystick: wpilib.Joystick):
        """Drives the robot using the joystick"""
        if isinstance(self.robotDrive, wpilib.drive.MecanumDrive):
            self.robotDrive.driveCartesian(joystick.getLeftX(), joystick.getRightX(),-joystick.getLeftY(),  Rotation2d(0))
        elif isinstance(self.robotDrive, wpilib.drive.DifferentialDrive):
            self.robotDrive.arcadeDrive(joystick.getLeftY(), -joystick.getLeftX())
    def slowLeft(self,joystick: wpilib.Joystick) -> None:
        self.robotDrive.driveCartesian(0, 0, -.22, Rotation2d(0))
    def slowRight(self,joystick: wpilib.Joystick) -> None:
        self.robotDrive.driveCartesian(0, 0, .22, Rotation2d(0))
    # flight Checklist commands
    def OnlyFrontLeft(self) -> None:
        self.frontLeftMotor.set(0.51)
    def OnlyFrontRight(self) -> None:
        self.frontRightMotor.set(0.52)
    def OnlyBackLeft(self) -> None:
        self.backLeftMotor.set(0.53)
    def OnlyBackRight(self) -> None:
        self.backRightMotor.set(0.54)
