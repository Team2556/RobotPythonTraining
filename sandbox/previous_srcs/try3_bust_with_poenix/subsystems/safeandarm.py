
import wpilib
import commands2
from try3_bust_with_poenix.constants import ShooterConstant

class SafeAndArm(commands2.Subsystem):
    def __init__(self):
        self.safe = False
        self.arm = False
        #display the state of the safe and arm subsystem; do these need to be put in the periodic function?
        wpilib.SmartDashboard.putBoolean("Safe", self.safe)
        wpilib.SmartDashboard.putBoolean("Armed", self.arm)

    def set_safe(self):
        self.safe = True
        self.arm = False

    def set_arm(self):
        self.safe = False
        self.arm = True

    def is_safe(self):
        return self.safe

    def is_armed(self):
        return self.arm
    
    
    def initDefaultCommand(self):
        self.setDefaultCommand(commands2.RunCommand(self.periodic))

    def periodic(self):
        pass