
from operator import invert
import phoenix6
import wpilib
import wpilib.drive
import commands2
from try3_bust_with_poenix.constants import DriveConstant
import commands.driving as drivingCommandsPassThrough
import math


from wpilib import (SmartDashboard, 
                    SendableChooser, 
                    CameraServer, 
                    DigitalInput, 
                    DoubleSolenoid, 
                    Joystick, 
                    Servo, 
                    Timer, 
                    VictorSP,
                    XboxController,
                    Compressor,
                    AnalogInput,
                    Encoder,
                    Field2d,
                    ADXRS450_Gyro,
                    Talon,
                    # TalonFX,

                    )
from phoenix6 import controls, configs, hardware, signals


# from phoenix6 import TalonFX
from wpilib.simulation import (EncoderSim,
                                 ADXRS450_GyroSim
                                 )



class Drivetrain(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        #region motors
        # now types are organized cleanly by module
        self.frontLeftmotor = hardware.TalonFX(DriveConstant.kLeftMotor1Port)
        # self.frontLeftmotor_SIM = self.frontLeftmotor.getSimState()
        talonfx_frontLeft_configurator = self.frontLeftmotor.configurator
        self.frontLeftmotor_control = controls.DutyCycleOut(output=0.2, enable_foc=False)
        # self.frontLeftmotor_control.w with_motor_output(.3)
        self.frontLeftmotor.set_control(self.frontLeftmotor_control)
        SmartDashboard.putNumber("front left motor output value -- in drivetrain init", self.frontLeftmotor.get_duty_cycle().value)
        
        self.frontLeftmotor.set_control(self.frontLeftmotor_control)
        self.backLeftmotor = hardware.TalonFX(DriveConstant.kLeftMotor2Port)
        self.backLeftmotor_control = controls.DutyCycleOut(output=0.2)
        self.backLeftmotor.set_control(self.backLeftmotor_control)
        phoenix6.hardware.talon_fx.TalonFX
        
        #setup a motor configuration with inversion to apply to left
        motor_invert_configs = configs.MotorOutputConfigs()
        motor_invert_configs.inverted = signals.InvertedValue.COUNTER_CLOCKWISE_POSITIVE# .CLOCKWISE_POSITIVE
        
        self.frontRightmotor = hardware.TalonFX(DriveConstant.kRightMotor1Port)
        talonfx_frontRight_configurator = self.frontRightmotor.configurator
        talonfx_frontRight_configurator.apply(motor_invert_configs)
        self.frontRightmotor_control = controls.DutyCycleOut(output=0)

        self.backRightmotor = hardware.TalonFX(DriveConstant.kRightMotor2Port)
        talonfx_backRight_configurator = self.backRightmotor.configurator
        talonfx_backRight_configurator.apply(motor_invert_configs)
        self.backRightmotor_control = controls.DutyCycleOut(output=0)
        # signals.    (self.backRightmotor, talonfx_inverted)


        TheWB_p6_mecanum = self.TheWB_p6_mecanum
        self.drive = TheWB_p6_mecanum(self)#self.frontLeftmotor, self.backLeftmotor, self.frontRightmotor, self.backRightmotor)
        #wpilib.drive.MecanumDrive(self.frontLeftmotor , self.backLeftmotor, self.frontRightmotor, self.backRightmotor)
        self.drive.Deadband = DriveConstant.kDeadband
        self.drive.MaxOutput = DriveConstant.kMaxOutput
        # self.driveCartesian = self.drive.TheWB_driveCartesian
        
        #endregion

        #region encoders
        self.frontLeftEncoder = Encoder(DriveConstant.kFrontLeftEncoderPorts[0], 
                                               DriveConstant.kFrontLeftEncoderPorts[1])
        self.frontLeftEncoder.setDistancePerPulse(DriveConstant.kEncoderDistancePerPulse)
        self.frontLeftEncoder.setSamplesToAverage(7)
        #simulation version of the encoder
        self.sim_frontLeftEncoder = EncoderSim(self.frontLeftEncoder)
                                            

        self.frontRightEncoder = Encoder(DriveConstant.kFrontRightEncoderPorts[0],
                                                DriveConstant.kFrontRightEncoderPorts[1])
        
        self.frontRightEncoder.setDistancePerPulse(DriveConstant.kEncoderDistancePerPulse)
        self.frontRightEncoder.setSamplesToAverage(7)
        self.sim_frontRightEncoder = EncoderSim(self.frontRightEncoder)

        self.backLeftEncoder = Encoder(DriveConstant.kBackLeftEncoderPorts[0],
                                              DriveConstant.kBackLeftEncoderPorts[1])
        self.backLeftEncoder.setDistancePerPulse(DriveConstant.kEncoderDistancePerPulse)
        self.backLeftEncoder.setSamplesToAverage(7)
        self.sim_backLeftEncoder = EncoderSim(self.backLeftEncoder)

        self.backRightEncoder = Encoder(DriveConstant.kBackRightEncoderPorts[0],
                                               DriveConstant.kBackRightEncoderPorts[1])
        self.backRightEncoder.setDistancePerPulse(DriveConstant.kEncoderDistancePerPulse)
        self.backRightEncoder.setSamplesToAverage(7)
        self.sim_backRightEncoder = EncoderSim(self.backRightEncoder)

        #endregion

        #region gyro
        self.gyro = ADXRS450_Gyro()
        self.sim_gyro = ADXRS450_GyroSim(self.gyro)
        #endregion

        #region drive methods

        self.auto_drive_1ft = drivingCommandsPassThrough.auto_drive_1ft
        self.DriveByController = drivingCommandsPassThrough.DriveByController

        #endregion

    def periodic(self):
        #region dashboard
        # change to use the pheonix6 stuff... ugh ... SmartDashboard.putData("front left motor", self.frontLeftmotor)
        # SmartDashboard.putNumber("front left Motor - data get", self.frontLeftmotor.get())
        # SmartDashboard.putNumber("Back Left Motor - data", self.backLeftmotor.get())
        # SmartDashboard.putNumber("Front Right Motor - data", self.frontRightmotor.get())
        # SmartDashboard.putNumber("Back Right Motor - data", self.backRightmotor.get())

        # SmartDashboard.putNumber("Front Left Encoder", self.frontLeftEncoder.getDistance())
        # SmartDashboard.putNumber("Front Right Encoder", self.frontRightEncoder.getDistance())
        # SmartDashboard.putNumber("Back Left Encoder", self.backLeftEncoder.getDistance())
        # SmartDashboard.putNumber("Back Right Encoder", self.backRightEncoder.getDistance())

        SmartDashboard.putNumber("Gyro", self.gyro.getAngle())
        SmartDashboard.putNumber("front left motor output Voltage", self.frontLeftmotor.get_motor_voltage().value)

        #endregion

    def resetEncoders(self):
        self.frontLeftEncoder.reset()
        self.frontRightEncoder.reset()
        self.backLeftEncoder.reset()
        self.backRightEncoder.reset()
    
    def getAverageEncoderDistance(self):
        avgEncoderDistance = (self.frontLeftEncoder.getDistance() + self.frontRightEncoder.getDistance() + self.backLeftEncoder.getDistance() + self.backRightEncoder.getDistance()) / 4.0
        return avgEncoderDistance
    
    class TheWB_p6_mecanum:
        def __init__(self, robot_to_pull_motors_from):
            self.frontLeftmotor = robot_to_pull_motors_from.frontLeftmotor
            self.backLeftmotor = robot_to_pull_motors_from.backLeftmotor
            self.frontRightmotor = robot_to_pull_motors_from.frontRightmotor
            self.backRightmotor = robot_to_pull_motors_from.backRightmotor
            self.frontLeftmotor_control = robot_to_pull_motors_from.frontLeftmotor_control
            self.backLeftmotor_control = robot_to_pull_motors_from.backLeftmotor_control
            self.frontRightmotor_control = robot_to_pull_motors_from.frontRightmotor_control
            self.backRightmotor_control = robot_to_pull_motors_from.backRightmotor_control
            self.Deadband = 0.1
            self.MaxOutput = .995
            

            
        def TheWB_driveCartesian(self, xSpeed, ySpeed, zRotation): #, gyroAngle = 0.0):
            '''
            xSpeed: The speed that the robot should drive in its X direction. [-1.0..1.0]
            ySpeed: The speed that the robot should drive in its Y direction. [-1.0..1.0]
            zRotation: The rate of rotation for the robot that is independent of the translation. [-1.0..1.0]
            '''
            #create coding for the mecanum drive kinematics
            base_theta = math.atan2(xSpeed, ySpeed) - math.pi / 4.0
            r = math.hypot(xSpeed, ySpeed)
            cos = math.cos(base_theta)
            sin = math.sin(base_theta)
            max_trig = max(abs(cos), abs(sin))
            leftFront = r * cos/max_trig + zRotation
            rightFront = r * sin/max_trig - zRotation
            leftRear = r * sin/max_trig + zRotation
            rightRear = r * cos/max_trig - zRotation

            # Limit the toal power to the motors to self.MaxOutput

            maxMagnitude = max(max(abs(leftFront), abs(rightFront)), max(abs(leftRear), abs(rightRear)))
            if maxMagnitude > self.MaxOutput:
                leftFront /= maxMagnitude/self.MaxOutput
                rightFront /= maxMagnitude/self.MaxOutput
                leftRear /= maxMagnitude/self.MaxOutput
                rightRear /= maxMagnitude/self.MaxOutput
            SmartDashboard.putNumber("leftFront in TheWB_drivecartesian", leftFront)
            SmartDashboard.putNumber("rightFront in TheWB_drivecartesian", rightFront)
            SmartDashboard.putNumber("leftRear in TheWB_drivecartesian", leftRear)
            SmartDashboard.putNumber("rightRear in TheWB_drivecartesian", rightRear)

            # TODO: should this just set motor speeds instead of return something
            # self.frontLeftmotor.set_control( self.frontLeftmotor_control.with_output(leftFront))
            # self.frontRightmotor.set_control( self.frontRightmotor_control.with_output(rightFront))
            # self.backLeftmotor.set_control( self.backLeftmotor_control.with_output(leftRear))   
            # self.backRightmotor.set_control( self.backRightmotor_control.with_output(rightRear))    


            return (leftFront, rightFront, leftRear, rightRear)


  