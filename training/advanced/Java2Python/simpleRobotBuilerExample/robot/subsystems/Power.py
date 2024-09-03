# RobotBuilder Version: 6.1
#
# This file was generated by RobotBuilder. It contains sections of
# code that are automatically generated and assigned by robotbuilder.
# These sections will be updated in the future when you export to
# Python from RobotBuilder. Do not put any code or make any change in
# the blocks indicating autogenerated code or it will be lost on an
# update. Deleting the comments indicating the section will prevent
# it from being updated in the future.

# ROBOTBUILDER TYPE: Subsystem.

import wpilib
from wpilib import PowerDistribution
from wpilib2.command import SubsystemBase

class Power(SubsystemBase):
    # Initialize your subsystem here
    def __init__(self):
        super().__init__()

        # Power Distribution
        self.powerDistribution = PowerDistribution()
        wpilib.LiveWindow.add(self.powerDistribution)

    def periodic(self):
        # This method will be called once per scheduler run
        pass

    def simulationPeriodic(self):
        # This method will be called once per scheduler run when in simulation
        pass

    # Put methods for controlling this subsystem here. Call these from Commands.