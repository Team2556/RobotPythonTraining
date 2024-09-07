# Import the necessary libraries
import wpilib
import commands2
from commands2 import (button,
                       cmd,
                        Command,
                        CommandScheduler,
                        ConditionalCommand,
                        DeferredCommand,
                        FunctionalCommand,
                        IllegalCommandUse,
                        InstantCommand,
                        InterruptionBehavior,
                        NotifierCommand,
                        ParallelCommandGroup,
                        ParallelDeadlineGroup,
                        ParallelRaceGroup,
                        PIDCommand,
                        PIDSubsystem,
                        PrintCommand,
                        ProfiledPIDCommand,
                        ProfiledPIDSubsystem,
                        ProxyCommand,
                        RepeatCommand,
                        RunCommand,
                        ScheduleCommand,
                        SelectCommand,
                        SequentialCommandGroup,
                        StartEndCommand,
                        Subsystem,
                        SwerveControllerCommand,
                        TimedCommandRobot,
                        TrapezoidProfileCommand,
                        TrapezoidProfileSubsystem,
                        WaitCommand,
                        WaitUntilCommand,
                        WrapperCommand,
                        )
#Command, CommandGroup,
# from subsystem.DriveTrain import DriveTrain 
from subsystem.drivesubsystem import DriveSubsystem as DriveTrain
from subsystem.GearShifter import GearShifter
from subsystem.AirCannon import AirCannon
from subsystem.CannonActuator import CannonActuator
from command import  DriveWithJoystick, ShiftGear, ShootShirt, AimCannon
from oi import OI
from commands2 import CommandScheduler

import ntcore

# Create the robot class
class MyRobot(commands2.TimedCommandRobot): # wpilib.TimedRobot):
    """
    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you
    """
    def robotInit(self):
        # Create the subsystem instances
        self.drivetrain = DriveTrain
        self.gearshifter = GearShifter()
        self.aircannon = AirCannon()
        self.cannonactuator = CannonActuator()

        # Create the OI instance
        self.oi = OI.DriverController

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

        # Get the default instance of NetworkTables that was created automatically
        # when the robot program starts
        inst = ntcore.NetworkTableInstance.getDefault()
        # Get the table within that instance that contains the data. There can
        # be as many tables as you like and exist to make it easier to organize
        # your data. In this case, it's a table called datatable.
        table = inst.getTable("datatable")
        # Start publishing topics within that table that correspond to the X and Y values
        # for some operation in your program.
        # The topic names are actually "/datatable/x" and "/datatable/y".
        self.xPub = table.getDoubleTopic("x").publish()
        self.yPub = table.getDoubleTopic("y").publish()
        self.x = 0
        self.y = 0

    def autonomousInit(self):
        pass # for now
        # Start the autonomous command(s)
        # self.autonomousCommand = CommandGroup()
        # self.autonomousCommand.addSequential(Command())
        # self.autonomousCommand.schedule()

    def autonomousPeriodic(self):
        pass # for now
        # Run the scheduler for the autonomous command(s)
        # CommandScheduler.getInstance().run()

    def teleopInit(self):
        # Cancel any running autonomous command(s)
        if self.autonomousCommand is not None:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self):
        # Run the scheduler for the teleop command(s)
        CommandScheduler.getInstance().run()

        # Publish values that are constantly increasing.
        self.xPub.set(self.x)
        self.yPub.set(self.y)
        self.x += 0.05
        self.y += 1.0

    def testInit(self):
        # Start the test command(s)
        self.testCommand = Command()
        self.testCommand.schedule()

    def testPeriodic(self):
        # Run the scheduler for the test command(s)
        CommandScheduler.getInstance().run()

if __name__ == "__main__":
    pass # this is no longer used...wpilib.run(MyRobot), in a venv use robotpy instead
 