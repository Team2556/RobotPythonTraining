#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

#
# See the notes for the other physics sample
#

import wpilib.simulation
from wpilib.simulation import ( EncoderSim,
                               AnalogGyroSim,
                               PWMSim,
                            #    DifferentialDrivetrainSim
                            #    DIOEncoderSim,
                            #    ADXRS450_GyroSim, PDPData,
                            #    PneumaticsSim,
                            #    RoboRIOData, SimDeviceData, SimDeviceSim,
                            #    SolenoidSim,
                            #    TalonFXSim, TalonSRXSim, VictorSPXSim,
                            #    AnalogInputSim, AnalogOutputSim,
                            #    DigitalInputSim, DigitalOutputSim, 
                            #    DutyCycleEncoderSim, PowerDistributionSim, RelaySim, UltrasonicSim, AccelerometerSim, GyroBase,
                            #    ADXL345_I2C, ADXL362
                               )
from wpilib import SmartDashboard, Field2d
import wpimath

from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics import motor_cfgs, tankmodel
from pyfrc.physics.units import units
from wpilib import RobotController
import wpimath.system
import wpimath.system.plant

import constants

import typing

if typing.TYPE_CHECKING:
    from robot import MyRobot
    from robotcontainer import RobotContainer

# there has to be a beter way to do this
from subsystems.cannonsubsystem import CannonLift

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
        self.robotCont = robot.container

        # Motors
        self.leftMotors = PWMSim(self.robotCont.robotDrive.leftMotorLeader.getChannel())
        # self.leftMotors = wpilib.simulation.PWMSim(2)
        self.rightMotors = PWMSim(self.robotCont.robotDrive.rightMotorLeader.getChannel())
        # self.rightMotors = wpilib.simulation.PWMSim(4)

        # Encoders
        self.leftEncoder = EncoderSim.createForChannel(constants.DriveConstants.kLeftEncoderPorts[0] ) #.getChannel())
        self.rightEncoder = EncoderSim.createForChannel(constants.DriveConstants.kRightEncoderPorts[0]) #.getChannel())

        # Gyro
        # self.gyro = wpilib.simulation.AnalogGyroSim(robot.gyro)

        # Change these parameters to fit your robot!
        bumper_width = 3.25 * units.inch

        # fmt: off
        self.drivetrain = tankmodel.TankModel.theory(
            motor_cfgs.MOTOR_CFG_CIM,           # motor configuration
            110 * units.lbs,                    # robot mass
            10.71,                              # drivetrain gear ratio
            2,                                  # motors per side
            22 * units.inch,                    # robot wheelbase
            23 * units.inch + bumper_width * 2, # robot width
            32 * units.inch + bumper_width * 2, # robot length
            6 * units.inch,                     # wheel diameter
        )
        # fmt: on

        # Cannon Lift to aim
        # The arm gearbox represents a gearbox containing two Vex 775pro motors.
        CannonLiftConstants = constants.CannonLiftConstants
        self.armGearbox = wpimath.system.plant.DCMotor.vex775Pro(2)
        # Simulation classes help us simulate what's going on, including gravity.
        # This arm sim represents an arm that can travel from -75 degrees (rotated down front)
        # to 255 degrees (rotated down in the back).
        self.armSim = wpilib.simulation.SingleJointedArmSim(
            self.armGearbox,
            CannonLiftConstants.kArmReduction,
            wpilib.simulation.SingleJointedArmSim.estimateMOI(
                CannonLiftConstants.kArmLength, CannonLiftConstants.kArmMass
            ),
            CannonLiftConstants.kArmLength,
            CannonLiftConstants.kMinAngleRads,
            CannonLiftConstants.kMaxAngleRads,
            True,
            # Add noise with a std-dev of 1 tick
            CannonLiftConstants.kArmEncoderDistPerPulse,
        )


    def update_sim(self, now: float, tm_diff: float) -> None:
        """
        Called when the simulation parameters for the program need to be
        updated.

        :param now: The current time as a float
        :param tm_diff: The amount of time that has passed since the last
                        time that this function was called
        """

        # Simulate the drivetrain (only front motors used because read should be in sync)
        leftMotorSpeed = self.leftMotors.getSpeed()
        SmartDashboard.putNumber("Sim- Left Motor Speed", leftMotorSpeed)
        rightMotorSpeed = self.rightMotors.getSpeed()
        SmartDashboard.putNumber("Sim- Right Motor Speed", rightMotorSpeed)

        transform = self.drivetrain.calculate(leftMotorSpeed, rightMotorSpeed, tm_diff)


        pose = self.physics_controller.move_robot(transform)
        self.field.setRobotPose(pose) #should display on glass
        SmartDashboard.putNumberArray("Sim- Pose", [pose.x, pose.y, pose.rotation().degrees()])
        # SmartDashboard.putNumberArray("Sim- Position", [pose.x, pose.y])
        SmartDashboard.putNumber("Sim- Position X", pose.x)
        SmartDashboard.putNumber("Sim- Position Y", pose.y)

        # self.physics_controller.move_robot(transform)

        # compute encoder
        l_encoder = self.drivetrain.l_position / constants.DriveConstants.kEncoderDistancePerPulse #ENCODER_TICKS_PER_FT
        r_encoder = self.drivetrain.r_position / constants.DriveConstants.kEncoderDistancePerPulse #ENCODER_TICKS_PER_FT
        self.leftEncoder.setDistance(l_encoder)
        self.rightEncoder.setDistance(r_encoder)
        SmartDashboard.putNumber("Sim- Left Encoder", l_encoder)
        SmartDashboard.putNumber("Sim- Right Encoder", r_encoder)

        # Simulate the cannon lift
        self.encoderSim = wpilib.simulation.EncoderSim( self.robotCont.lift.encoder )
        #CannonLift.encoder() )
        self.motorSim = wpilib.simulation.PWMSim(constants.CannonLiftConstants.kMotorPort)
        # something like this goes in the physics.py file
        # self.arm = SingleJointedArmSim(constants.CannonConstants.kArmSimModel)
        # self.arm.setFriction(constants.CannonConstants.kArmFriction)
        # self.arm.setMass(constants.CannonConstants.kArmMass)
        # self.arm.setGearing(constants.CannonConstants.kArmGearing)
        # self.arm.setInertia(constants.CannonConstants.kArmInertia)
        # self.arm.setVoltage(0)
        # self.arm.setAngle(constants.CannonConstants.kArmStartingAngle)
        # self.arm.setVelocity(0)
        # self.arm.setAcceleration(0)
        # The P gain for the PID controller that drives this arm.


        # Update the gyro simulation
        # -> FRC gyros are positive clockwise, but the returned pose is positive
        #    counter-clockwise
        # self.gyro.setAngle(-pose.rotation().degrees())
