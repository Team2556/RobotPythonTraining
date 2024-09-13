
from turtle import left
from wpilib import (XboxController,
                    SmartDashboard,
)
from commands2 import Command

import typing
if typing.TYPE_CHECKING:
    from subsystems.drivetrain import Drivetrain
Drivetrain_type = typing.TypeVar("Drivetrain", bound="Drivetrain")


class DriveByController(Command):
    def __init__(self, drivetrain: Drivetrain_type, controller: XboxController):
        super().__init__()
        self.drivetrain = drivetrain
        self.controller = controller
        self.addRequirements(drivetrain)        

    def execute(self):
        
        (leftFront,
        rightFront,
        leftRear,
        rightRear)= self.drivetrain.drive.TheWB_driveCartesian( 
            xSpeed= -self.controller.getLeftY(),
            ySpeed =self.controller.getLeftTriggerAxis(),
            zRotation=self.controller.getLeftX(),
            )
        SmartDashboard.putNumber("leftFront out of TheWB_drivecartesian -- from driving", leftFront)
        self.drivetrain.frontLeftmotor_control.with_output(leftFront)
        SmartDashboard.putNumber("front left motor controler -- in driving", self.drivetrain.frontLeftmotor_control.__getattribute__("output"))
        self.drivetrain.frontLeftmotor.set_control( self.drivetrain.frontLeftmotor_control.with_output(leftFront))
        SmartDashboard.putNumber("front left motor output value -- ing driving", self.drivetrain.frontLeftmotor.get_duty_cycle().value)
        self.drivetrain.frontRightmotor.set_control( self.drivetrain.frontRightmotor_control.with_output(rightFront))
        self.drivetrain.backLeftmotor.set_control( self.drivetrain.backLeftmotor_control.with_output(leftRear))   
        self.drivetrain.backRightmotor.set_control( self.drivetrain.backRightmotor_control.with_output(rightRear)) 

        self.drivetrain.frontLeftEncoder.getDistance()
        SmartDashboard.putNumber("front left encoder distance", self.drivetrain.frontLeftEncoder.getDistance())
        self.drivetrain.frontRightEncoder.getDistance()
        self.drivetrain.backLeftEncoder.getDistance()
        self.drivetrain.backRightEncoder.getDistance()

        # setup the simulation's encoder
        self.drivetrain.sim_frontLeftEncoder.setDistance(self.drivetrain.frontLeftEncoder.getDistance())
        SmartDashboard.putNumber("SIM-front left encoder distance", self.drivetrain.sim_frontLeftEncoder.getDistance())
        self.drivetrain.sim_frontRightEncoder.setDistance(self.drivetrain.frontRightEncoder.getDistance())
        self.drivetrain.sim_backLeftEncoder.setDistance(self.drivetrain.backLeftEncoder.getDistance())
        self.drivetrain.sim_backRightEncoder.setDistance(self.drivetrain.backRightEncoder.getDistance())

    def isFinished(self):
        return False

    def end(self):
        self.drivetrain.drive.TheWB_driveCartesian(0, 0, 0)

def auto_drive_1ft():
    ...
