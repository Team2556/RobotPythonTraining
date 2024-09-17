'''
Asked github copilot to generate a physics.py file for me. This file is used to simulate the robot in the pyfrc simulator.
Here's a detailed pseudocode plan:

Import necessary modules:

Import wpilib, wpilib.simulation, and robotpy.
Initialize the simulation components:

Define the __init__ method.
Initialize the motor controllers.
Initialize the drivetrain simulation.
Update the simulation:

Define the update_sim method.
Update motor voltages.
Simulate the drivetrain using the motor voltages.
Update the SmartDashboard with the motor voltages.
'''


from asyncio import constants
import pyfrc.mains
import pyfrc.physics.drivetrains
import pyfrc.physics.motor_cfgs
import pyfrc.util
import wpilib
from wpilib import SmartDashboard
from wpilib.simulation import (PWMSim, AnalogGyroSim,)
from wpilib.drive import MecanumDrive
import wpilib.simulation
from wpimath.kinematics import (MecanumDriveKinematics,
                                MecanumDriveKinematicsBase,
                                MecanumDriveOdometry,
                                MecanumDriveOdometryBase,
                                MecanumDriveWheelPositions,
                                MecanumDriveWheelSpeeds,)
from wpimath.geometry import (Pose2d, Rotation2d, Translation2d)
from wpimath.estimator import MecanumDrivePoseEstimator 
# from robotpy_ext.common_drivers import navx
from constants import (DriveConstant, OIConstant)
from phoenix6.unmanaged import feed_enable


class PhysicsEngine:
    def __init__(self, physics_controller, robot: "MyRobot"): # type: ignore
        self.physics_controller = physics_controller
        self.robot = robot
        self.robotDrive = robot.robotDrive

        # Initialize motor controllers
        self.right_invert_YN = robot.robotDrive.right_invert_YN

        # TODO: try converting all motors to refer to the robot's motors
        self.frontLeftMotor = robot.robotDrive.frontLeftMotor.getSimCollection()
        self.frontRightMotor = robot.robotDrive.frontRightMotor.getSimCollection()
        # self.frontRightMotor.setInverted(self.right_invert_YN) sim colletion has no set inverted
        self.backLeftMotor = robot.robotDrive.backLeftMotor.getSimCollection()
        self.backRightMotor = robot.robotDrive.backRightMotor.getSimCollection()
        # self.backRightMotor.setInverted(self.right_invert_YN)

        # self.frontLeftMotor =wpilib.PWMVictorSPX(DriveConstant.kLeftMotor1Port)
        # self.frontRightMotor = wpilib.PWMVictorSPX(DriveConstant.kRightMotor1Port)
        # self.frontRightMotor.setInverted(self.right_invert_YN) 
        # self.backLeftMotor = wpilib.PWMVictorSPX(DriveConstant.kLeftMotor2Port)
        # self.backRightMotor = wpilib.PWMVictorSPX(DriveConstant.kRightMotor2Port)
        # self.backRightMotor.setInverted(self.right_invert_YN)

        # Initialize motor simulations
        # pyfrc.physics.drivetrains.MecanumDrivetrain
        # self.sim_frontLeftMotor = robot.robotDrive.frontLeftMotor.getSimCollection()
        # self.sim_frontLeftMotor =  PWMSim(DriveConstant.kLeftMotor1Port)
        # self.sim_frontRightMotor = PWMSim(DriveConstant.kRightMotor1Port)
        # self.sim_backLeftMotor = PWMSim(DriveConstant.kLeftMotor2Port)
        # self.sim_backRightMotor = PWMSim(DriveConstant.kRightMotor2Port)

        # Initialize the drivetrain
        # self.sim_frontRightMotor.setInverted(True)
        # self.sim_backRightMotor.setInverted(True)
        
        
        # self.drivetrain = MecanumDrive(frontLeftMotor=self.frontLeftMotor, 
        #                                rearLeftMotor=self.backLeftMotor,
        #                                frontRightMotor=self.frontRightMotor, 
        #                                rearRightMotor=self.backRightMotor)

        # Initialize the gyro
        # self.gyro = AnalogGyroSim()#navx.AHRS.create_spi()

        #initialize the Xbox conroller
        self.Drivercontroller = wpilib.XboxController(OIConstant.kDriver1ControllerPort)

    def update_sim(self, now, tm_diff):
        # Currently, the Python API for CTRE doesn't automatically detect the the
        # Sim driverstation status and enable the signals. So, for now, manually
        # feed the enable signal for double the set robot period.
        feed_enable(0.020 * 2)

        # self.frontRightMotor.setInverted(self.right_invert_YN )
        # self.backRightMotor.setInverted(self.right_invert_YN )
        # Update the SmartDashboard with the motor inversion status - hopefully allow change from SmartDashboard
        # SmartDashboard.putBoolean("Simmulated right inverstion?", self.right_invert_YN)
        # Update motor voltages
        # sim_frontLeftMotor_speed = self.sim_frontLeftMotor.getSpeed() #* 12
        # sim_frontRightMotor_speed = self.sim_frontRightMotor.getSpeed()# * 12
        # sim_backLeftMotor_speed = self.sim_backLeftMotor.getSpeed() #* 12
        # sim_backRightMotor_speed = self.sim_backRightMotor.getSpeed() #* 12
        # # Update the SmartDashboard with motor voltages
        # SmartDashboard.putNumber("frontLeftMotor_speed SIM", sim_frontLeftMotor_speed)
        # SmartDashboard.putNumber("frontRightMotor_speed SIM", sim_frontRightMotor_speed)
        # SmartDashboard.putNumber("backLeftMotor_speed SIM", sim_backLeftMotor_speed)
        # SmartDashboard.putNumber("backRightMotor_speed SIM", sim_backRightMotor_speed)

        # Update motor voltages
        frontLeftMotor_speed = self.frontLeftMotor.getMotorOutputLeadVoltage() /12 #assuming 12 volts for now
        SmartDashboard.putNumber("frontLeftMotor_SIM getmotorOutput Volts by 12Volts", frontLeftMotor_speed)
        frontRightMotor_speed = self.frontRightMotor.getMotorOutputLeadVoltage() / (12*(1-2*self.right_invert_YN))
        SmartDashboard.putNumber("frontRightMotor_SIM getmotorOutput Volts by 12Volts", frontRightMotor_speed)
        backLeftMotor_speed = self.backLeftMotor.getMotorOutputLeadVoltage() /12
        SmartDashboard.putNumber("backLeftMotor_SIM getmotorOutput Volts by 12Volts", backLeftMotor_speed)
        backRightMotor_speed = self.backRightMotor.getMotorOutputLeadVoltage() / (12*(1-2*self.right_invert_YN))
        SmartDashboard.putNumber("backRightMotor_SIM getmotorOutput Volts by 12Volts", backRightMotor_speed)

        '''
        frontRightMotor_speed = self.frontRightMotor.getSpeed()# * 12
        backLeftMotor_speed = self.backLeftMotor.getSpeed() #* 12
        backRightMotor_speed = self.backRightMotor.getSpeed() #* 12
        # Update the SmartDashboard with motor voltages
        SmartDashboard.putNumber("frontLeftMotor_speed", frontLeftMotor_speed)
        SmartDashboard.putNumber("frontRightMotor_speed", frontRightMotor_speed)
        SmartDashboard.putNumber("backLeftMotor_speed", backLeftMotor_speed)
        SmartDashboard.putNumber("backRightMotor_speed", backRightMotor_speed)
        '''
        # what is coming through the drivetrain?
        # Simulate the drivetrain
        # wheel_speeds =self.robotDrive.share_wheel_speeds
        '''
        self.drivetrain.driveCartesian(-self.Drivercontroller.getLeftY(),
                                       -self.Drivercontroller.getRightX(),
                                       -self.Drivercontroller.getRightY())  
        wheel_speeds = self.drivetrain.WheelSpeeds()
        print("wheel_speeds", wheel_speeds)
        frontLeftSpeed = wheel_speeds.frontLeft # self.drivetrain.WheelSpeeds().frontLeft

        print("frontLeftSpeed", frontLeftSpeed, '/n ---------------------------------------------- /n')
        SmartDashboard.putNumber("front left wheelspeed in update sim section", wheel_speeds.frontLeft)#wheel_speeds.frontLeft())
        SmartDashboard.putNumber("front Right wheelspeed in update sim section", wheel_speeds.frontRight)
        SmartDashboard.putNumber("back left wheelspeed in update sim section", wheel_speeds.rearLeft)
        SmartDashboard.putNumber("back right wheelspeed in update sim section", wheel_speeds.rearRight)
        #
        # subsystem used: self.robotDrive.driveCartesian(-joystick.getLeftY(), -joystick.getRightX(), -joystick.getLeftX(), Rotation2d(0))
        # Update the odometry based on the simulated wheel speeds
        # wheel_speeds_ifcantpullfromactualrobot = MecanumDriveWheelSpeeds(
        #     self.sim_frontLeftMotor.getSpeed(),
        #     self.sim_frontRightMotor.getSpeed(),
        #     self.sim_backLeftMotor.getSpeed(),
        #     self.sim_backRightMotor.getSpeed()
        # )


        '''
        wheel_speeds = MecanumDriveWheelSpeeds(
            frontLeftMotor_speed,
            frontRightMotor_speed,
            backLeftMotor_speed,
            backRightMotor_speed
        )


        # Create an odometry object
        drivtrain_kinematics = MecanumDriveKinematics(
                Translation2d(DriveConstant.kWheelBase / 2, DriveConstant.kTrackWidth / 2),
                Translation2d(DriveConstant.kWheelBase / 2, -DriveConstant.kTrackWidth / 2),
                Translation2d(-DriveConstant.kWheelBase / 2, DriveConstant.kTrackWidth / 2),
                Translation2d(-DriveConstant.kWheelBase / 2, -DriveConstant.kTrackWidth / 2)
            )
        chassis_speeds = drivtrain_kinematics.toChassisSpeeds(wheel_speeds)
        # Update the physics controller with the new state
        self.physics_controller.drive(chassis_speeds, tm_diff)

        '''
        # Update the simulation with the chassis speeds
        vx = chassis_speeds.vx
        SmartDashboard.putNumber("vx", vx)
        vy = chassis_speeds.vy
        SmartDashboard.putNumber("vy", vy)
        omega = chassis_speeds.omega
        SmartDashboard.putNumber("omega", omega)

        '''

'''
 def drive(self, speeds: ChassisSpeeds, tm_diff: float) -> Pose2d:
        """Call this from your :func:`PhysicsEngine.update_sim` function.
        Will update the robot's position on the simulation field.

        You can either calculate the chassis speeds yourself, or you
        can use the predefined functions in :mod:`pyfrc.physics.drivetrains`.

        The outputs of the `drivetrains.*` functions should be passed
        to this function.

        :param speeds:   Represents current speed/angle of robot travel
        :param tm_diff:  Amount of time speed was traveled (this is the
                         same value that was passed to update_sim)

        :return: current robot pose

        .. versionchanged:: 2020.1.0
           Input parameter is ChassisSpeeds object
        """    



        odometry = MecanumDriveOdometry(
            drivtrain_kinematics,
            Rotation2d(0),
            drivtrain_kinematics.getFrontLeft WheelPosition(),
        )

        # Update the odometry with the current wheel speeds and gyro angle
        odometry.update(Rotation2d(0), wheel_speeds)

        # Get the new pose of the robot
        new_pose = odometry.getPose()
        SmartDashboard.putData("Odometry", new_pose)

        # Update the physics controller with the new state
        self.physics_controller.move_robot(new_pose, tm_diff)
        
        # MecanumDriveOdometryBase.getPose(
        #     MecanumDriveOdometryBase(
        #         MecanumDriveKinematicsBase(self.drivetrain. ),
        #         Rotation2d(0),
        #         Pose2d(Translation2d(0,0), Rotation2d(0))
        #     ),
        # )
        # Update the physics controller with the new state
        # self.physics_controller.move_robot(self.drivetrain, tm_diff)'''