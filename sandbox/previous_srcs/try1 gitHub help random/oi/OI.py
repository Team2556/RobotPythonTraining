
import wpilib
from wpilib import SmartDashboard

def init():
    """
    This function is called when the robot is first started up and should be used for any initialization code.
    """

    # Set up the SmartDashboard
    SmartDashboard.putNumber("Shooter Speed", 0.0)
    SmartDashboard.putNumber("Shooter Angle", 0.0)
    
    SmartDashboard.putNumber("Shooter Acceleration", 0.0)


def DriverController():
    return wpilib.XboxController(0)
   