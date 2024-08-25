# Import necessary modules from RobotPy
from commands2 import CommandBase

class AutonomousCommand(CommandBase):
    def __init__(self):
        super().__init__()
        # Add any subsystem requirements here
        # self.addRequirements([self.subsystem])

    def initialize(self):
        pass

    def execute(self):
        pass

    def end(self, interrupted: bool):
        pass

    def isFinished(self):
        return False

    def runsWhenDisabled(self):
        return False