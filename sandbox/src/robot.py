import wpilib
import robotpy
# from commands import  Scheduler, DriveWithJoystick, ShiftGear, ShootShirt, AimCannon
#Command, CommandGroup,
from oi import OI
from subsystems import DriveTrain, GearShifter, AirCannon, CannonActuator
import numpy as np
# Import the necessary libraries

# Create the robot class
class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Create the subsystem instances
        self.drivetrain = DriveTrain()
        self.gearshifter = GearShifter()
        self.aircannon = AirCannon()
        self.cannonactuator = CannonActuator()

        # Create the OI instance
        self.oi = OI()

        # Create the commands
        self.driveWithJoystick = DriveWithJoystick(self.drivetrain, self.oi)
        self.shiftGear = ShiftGear(self.gearshifter, self.oi)
        self.shootShirt = ShootShirt(self.aircannon, self.oi)
        self.aimCannon = AimCannon(self.cannonactuator, self.oi)

        # Set the default command for the subsystems
        self.drivetrain.setDefaultCommand(self.driveWithJoystick)
        self.gearshifter.setDefaultCommand(self.shiftGear)
        self.aircannon.setDefaultCommand(self.shootShirt)
        self.cannonactuator.setDefaultCommand(self.aimCannon)

    def autonomousInit(self):
        # Start the autonomous command(s)
        self.autonomousCommand = CommandGroup()
        self.autonomousCommand.addSequential(Command())
        self.autonomousCommand.start()

    def autonomousPeriodic(self):
        # Run the scheduler for the autonomous command(s)
        Scheduler.getInstance().run()

    def teleopInit(self):
        # Cancel any running autonomous command(s)
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self):
        # Run the scheduler for the teleop command(s)
        Scheduler.getInstance().run()

    def testInit(self):
        # Start the test command(s)
        self.testCommand = Command()
        self.testCommand.start()

    def testPeriodic(self):
        # Run the scheduler for the test command(s)
        Scheduler.getInstance().run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
