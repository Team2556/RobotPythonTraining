import wpilib.simulation
from wpilib.simulation import ( EncoderSim,
                               AnalogGyroSim,
                               PWMSim,
)

from wpilib import SmartDashboard, Field2d
import wpimath

from pyfrc.physics.core import PhysicsInterface
# from pyfrc.physics import motor_cfgs
from pyfrc.physics.drivetrains import MecanumDrivetrain



from pyfrc.physics.units import units

import constants

class PhysicsEngine:
    """
    Simulates a 4-wheel robot using Tank Drive joystick control
    """

    def __init__(self, physics_controller: PhysicsInterface, robot: "MyRobot"):
        """
        :param physics_controller: `pyfrc.physics.core.Physics` object
                                   to communicate simulation effects to
        :param robot: your robot object
        """
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)

        self.physics_controller = physics_controller
        self.robot = robot

        # Change these parameters to fit Reggie!
        bumper_width = 3.25 * units.inch

        # fmt: off
        self.drivetrain = MecanumDrivetrain(
            x_wheelbase=23.5 * units.inch, y_wheelbase=22.5 * units.inch,
            # wheel_diameter=6 * units.inch, wheel_width=2 * units.inch,
            # front_left_motor=constants.DriveConstant.kLeftMotor1Port,
            # rear_left_motor=constants.DriveConstant.kLeftMotor2Port,
            # front_right_motor=constants.DriveConstant.kRightMotor1Port,
            # rear_right_motor=constants.DriveConstant.kRightMotor2Port,
        )
        # fmt: on

        # fmt: off
        self.physics_controller = physics_controller#.add_model(self.drivetrain)
        # fmt: on

        self.frontLeftMotor = PWMSim(robot.drivetrain.frontLeftmotor.getChannel())
        self.backLeftMotor = PWMSim(robot.drivetrain.backLeftmotor.getChannel())
        self.frontRightMotor = PWMSim(robot.drivetrain.frontRightmotor.getChannel())
        self.backRightMotor = PWMSim(robot.drivetrain.backRightmotor.getChannel())
        #self.robot.drivetrain.drive.frontLeftmotor.getChannel())
        # self.gyro = AnalogGyroSim(wpilib.AnalogGyro(0))
        # self.gyro.setAngle(0)

        self.frontLeftEncoder = EncoderSim(wpilib.Encoder(0, 1))
        self.frontRightEncoder = EncoderSim(wpilib.Encoder(2, 3))
        self.backLeftEncoder = EncoderSim(wpilib.Encoder(4, 5))
        self.backRightEncoder = EncoderSim(wpilib.Encoder(6, 7))

        # self.physics_controller.add_device_gyro(self.gyro)
        # self.physics_controller.add_device_encoder(self.frontLeftEncoder)
        # self.physics_controller.add_device_encoder(self.frontRightEncoder)
        # self.physics_controller.add_device_encoder(self.backLeftEncoder)
        # self.physics_controller.add_device_encoder(self.backRightEncoder)

    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Update the simulation of the physics model
        """
        # self.drivetrain.wheelSpeeds = self.drivetrain.wheelSpeeds
        # Simulate the drivetrain
        lf_motor = self.frontLeftMotor.getSpeed()
        lr_motor = self.backLeftMotor.getSpeed()
        rf_motor = self.frontRightMotor.getSpeed()
        rr_motor = self.backRightMotor.getSpeed()
        chasisSpeeds = self.drivetrain.calculate(
            self.frontLeftMotor.getSpeed(),
            self.backLeftMotor.getSpeed(),
            self.frontRightMotor.getSpeed(),
            self.backRightMotor.getSpeed(),
        )

        # need to get the movement tmdiff
        
        SmartDashboard.putNumber("update SIM chasis speed vx", chasisSpeeds.vx)
        SmartDashboard.putNumber("update SIM chasis speed vy", chasisSpeeds.vy)
        SmartDashboard.putNumber("update SIM chasis speed omega", chasisSpeeds.omega)
        


        pose = self.physics_controller.drive( speeds = chasisSpeeds, tm_diff=.02)# .move_robot(transform)

        SmartDashboard.putNumber("Pose X", pose.X())
        SmartDashboard.putNumber("Pose Y", pose.Y())
        SmartDashboard.putNumber("Pose Rotation", pose.rotation().degrees())
        self.field.setRobotPose(pose)
        
