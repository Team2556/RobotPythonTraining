
from math import e
from turtle import left
import phoenix5
from phoenix5 import Unmanaged 
import wpilib
import wpilib.simulation
from wpilib.simulation import (#DifferentialDrivetrainSim,
                               EncoderSim,
                               XboxControllerSim,
                                 AnalogGyroSim,
                                 
                               )
from wpilib import (AnalogGyro, SmartDashboard, Field2d)
import wpimath.controller
from wpimath.kinematics import (MecanumDriveWheelSpeeds,
                                MecanumDriveKinematics,
                                MecanumDriveOdometry,
                                MecanumDriveWheelPositions,
                                DifferentialDriveKinematics,
                                DifferentialDriveOdometry,
                                DifferentialDriveWheelSpeeds,
                                DifferentialDriveWheelPositions,
                                )
import wpimath
from wpimath.geometry import (Pose2d, Rotation2d, Translation2d)


from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics.drivetrains import MecanumDrivetrain
# from pyfrc.physics import motor_cfgs
import wpimath.kinematics
from wpimath.system.plant import DCMotor

from wpimath.system.plant import LinearSystemId

import rev
from constants import DriveConstant

class PhysicsEngine:
    '''
    start by simulating a sparkmax connected diff drive
    then change to mechanum drive
    '''
    def __init__(self, physics_controller: PhysicsInterface, robot: "MyRobot"): # type: ignore
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)
        self.physics_controller = physics_controller
        self.robot = robot
        
        self.sim_drivtrain = self.robot.robotDrive
        SmartDashboard.putData("imported drivetrain", self.sim_drivtrain)
        self.sim_created_drivtrain = wpimath.kinematics.MecanumDriveKinematics(Translation2d(.25,-.25),
                                                                               Translation2d(.25,.25),
                                                                               Translation2d(-.25,-.25),
                                                                                 Translation2d(-.25,.25))
        # self.sim_frontLeftMotor = self.sim_drivtrain.sim_frontLeftMotor
        self.sim_frontLeftMotor = self.sim_drivtrain.frontLeftMotor.getSimCollection()
        self.sim_frontRightMotor = self.sim_drivtrain.frontRightMotor.getSimCollection()
        self.sim_backLeftMotor = self.sim_drivtrain.backLeftMotor.getSimCollection()
        self.sim_backRightMotor = self.sim_drivtrain.backRightMotor.getSimCollection()

        

        # SmartDashboard.putData("sim created drivetrain", self.sim_created_drivtrain)



        '''plant_sim_2_2_2 = LinearSystemId.identifyDrivetrainSystem(
            1.98,  # V per rad/s
            0.2,  # V per rad/s^2
            1.5,  # V per m/s
            0.3,  # V per m/s^2
        )
        plant_sim_2_1_2 = LinearSystemId.DCMotorSystem(kV=2.0, kA=0.2)

        # generic_motor_sim = DCMotor( # CIM motor
        #     2.42,  # resistance
        #     2.0,  # voltage
        #     0.2,  # kv
        #     0.0,  # ka
        #     1.0  # gear ratio
        # )
        # DC_motor_param = dict( # CIM motor
        #     plant = plant_sim_2_1_2,
        #     gearbox = DCMotor.CIM(2) #generic_motor_sim,
        #     gearing = 1.0,  # gear ratio
        #     measurementStdDevs = [0,0]
        #     # 2.42,  # resistance
        #     # 2.0,  # voltage
        #     # 0.2,  # kv
        #     # 0.0,  # ka
        # )
        self.frontLeftMotor = robot.frontLeftMotor# rev.CANSparkMax(DriveConstant.kLeftMotor1Port, rev.CANSparkMax.MotorType.kBrushless) 
        # self.leftDrive = rev.CANSparkMax(DriveConstant.kLeftMotor2Port, rev.CANSparkMax.MotorType.kBrushless)
        self.frontRightMotor = robot.frontRightMotor #rev.CANSparkMax(DriveConstant.kRightMotor1Port, rev.CANSparkMax.MotorType.kBrushless)
        # self.rightDrive = rev.CANSparkMax(DriveConstant.kRightMotor2Port, rev.CANSparkMax.MotorType.kBrushless)
        
        #wpilib.simulation.DCMotorSim(**DC_motor_param) # .SimDeviceSim("SPARK MAX", 1)
        # self.frontRightMotor = wpilib.simulation.SimDeviceSim("SPARK MAX", 2)
        # self.backLeftMotor = wpilib.simulation.SimDeviceSim("SPARK MAX", 3)
        # self.backRightMotor = wpilib.simulation.SimDeviceSim("SPARK MAX", 4)


        self.drivetrain = DifferentialDrivetrainSim(
            plant=plant_sim_2_2_2 ,# ._controls._controls.system.LinearSystem_2_2_2,
            trackWidth=0.7112,  # track width in meters
            driveMotor=DCMotor.CIM(2),#generic_motor_sim,  # 2 CIM motors
            gearingRatio=7.29,  # gear ratio # 60.0,  # robot mass in kg
            wheelRadius=0.7112,  # wheel radius in meters
            # measurementStdDevs=[0.0, 0.0]
            )  # standard measurement noise'''
        
        
    def update_sim(self,now, tm_diff):
        Unmanaged.feedEnable(20 * 2)
        frontLeftMotor_volts = self.sim_frontLeftMotor.getMotorOutputLeadVoltage() 
        SmartDashboard.putNumber("frontLeftMotor_speed", frontLeftMotor_volts)
        frontRightMotor_volts = self.sim_frontRightMotor.getMotorOutputLeadVoltage()
        SmartDashboard.putNumber("frontRightMotor_speed", frontRightMotor_volts)
        backLeftMotor_volts = self.sim_backLeftMotor.getMotorOutputLeadVoltage()
        SmartDashboard.putNumber("backLeftMotor_speed", backLeftMotor_volts)
        backRightMotor_volts = self.sim_backRightMotor.getMotorOutputLeadVoltage()
        SmartDashboard.putNumber("backRightMotor_speed", backRightMotor_volts)
        
        # self.sim_created_drivtrain 
        # MecanumDriveWheelSpeeds(self.sim_created_drivtrain )
        pass
        '''encoder_fl = self.frontLeftMotor.getEncoder()
        encoder_fr = self.frontRightMotor.getEncoder()  
        # encoder_bl = self.backLeftMotor.getEncoder()
        # encoder_br = self.backRightMotor.getEncoder()

        self.drivetrain.setInputs(1,1)
        chasisSpeed_left = self.drivetrain.getLeftVelocity()
        chasisSpeed_right = self.drivetrain.getRightVelocity()

        # Create a simulated gyroscope
        self.gyro = AnalogGyroSim# wpilib.simulation.AnalogGyroSim(AnalogGyro)

        # Update the simulated gyroscope with the current heading
        self.gyro.setAngle(self.gyro(),angle=self.drivetrain.getHeading().degrees())

        # Convert wheel speeds to chassis speeds
        chassis_speeds = wpimath.kinematics.ChassisSpeeds.fromRobotRelativeSpeeds(
            vx=chasisSpeed_left, vy=chasisSpeed_right, omega=0, robot_heading=self.gyro.getAngle())
        
        # chasisSpeeds = 
        # .calculate(
        #     encoder_fl,
        #     # self.backLeftMotor.getSpeed(),
        #     encoder_fr,
        #     # self.backRightMotor.getSpeed(),
        #     tm_diff)
        pose = self.physics_controller.drive(speeds= chassis_speeds, tm_diff=tm_diff)#chasisSpeed_left,chasisSpeed_right,tm_diff=tm_diff)
                                                #  .vx,
                                                #     chasisSpeeds.vy,
                                                #     chasisSpeeds.omega,
                                                #     0.02
                                                # )'''
        ...