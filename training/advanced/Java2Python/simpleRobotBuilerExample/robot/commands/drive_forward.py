# Import necessary modules from RobotPy
from commands2 import CommandBase
from wpilib import SmartDashboard

# Import the Drive subsystem
from subsystems.drive import Drive

class DriveForward(CommandBase):
    def __init__(self, drive: Drive, setpoint: float = 0):
        super().__init__()
        self.drive = drive
        self.setpoint = setpoint
        self.addRequirements([self.drive])

    def initialize(self):
        self.drive.enable()
        self.drive.setSetpoint(self.setpoint)

    def execute(self):
        pass

    def isFinished(self):
        return self.drive.getController().atSetpoint()

    def end(self, interrupted: bool):
        pass