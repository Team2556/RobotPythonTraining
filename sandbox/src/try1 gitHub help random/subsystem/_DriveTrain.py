import wpilib
import wpimath
import commands2
from id import PWM_channels#, DIO_channels, PCM_channels

# The drive train is a 6 wheel tank drive system(2 on left, 2 on right), 6 Talon SRX motor controllers
# The drive train is a subsystem
# The drive train is controlled by the driver
# The drive train has a default command to drive with tank drive

class DriveTrain(commands2.TrapezoidProfileSubsystem):
    def __init__(self):
        constraints = wpimath.trajectory.TrapezoidProfile.Constraints(maxVelocity=1, maxAcceleration=2)
        super().__init__(constraints=constraints)
        # got error acceptable argument wpimath._controls._controls.trajectory.TrapezoidProfile.State(position: float = 0, velocity: wpimath.units.units_per_second = 0)
        



        # Initialize any variables or resources here
        self.left_front_motor = wpilib.Talon(PWM_channels.LEFT_FRONT_MOTOR)
        self.left_rear_motor = wpilib.Talon(PWM_channels.LEFT_REAR_MOTOR)
        self.right_front_motor = wpilib.Talon(PWM_channels.RIGHT_FRONT_MOTOR)
        self.right_rear_motor = wpilib.Talon(PWM_channels.RIGHT_REAR_MOTOR)
        self.left_motors = wpilib.SpeedControllerGroup(self.left_front_motor, self.left_rear_motor)
        self.right_motors = wpilib.SpeedControllerGroup(self.right_front_motor, self.right_rear_motor)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motors, self.right_motors)

    def tankDrive(self, left_speed, right_speed):
        # Implement the logic to drive with tank drive here
        self.drive.tankDrive(left_speed, right_speed)

    def arcadeDrive(self, speed, rotation):
        # Implement the logic to drive with arcade drive here
        self.drive.arcadeDrive(speed, rotation)

    def stop(self):
        # Implement the logic to stop the drive train here
        self.drive.stopMotor()