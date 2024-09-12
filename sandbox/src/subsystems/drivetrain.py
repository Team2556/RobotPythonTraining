
import wpilib
import wpilib.drive
import commands2
from constants import DriveConstant
import commands.driving as drivingCommandsPassThrough


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
                    Talon

                    )

from wpilib.simulation import (EncoderSim,
                                 ADXRS450_GyroSim
                                 )

class Drivetrain(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        #region motors

        self.frontLeftmotor = Talon(DriveConstant.kLeftMotor1Port)
        self.backLeftmotor = Talon(DriveConstant.kLeftMotor2Port)
        self.frontRightmotor = Talon(DriveConstant.kRightMotor1Port)
        self.frontRightmotor.setInverted(True)
        self.backRightmotor = Talon(DriveConstant.kRightMotor2Port)
        self.backRightmotor.setInverted(True)

        self.drive = wpilib.drive.MecanumDrive(self.frontLeftmotor, self.backLeftmotor, self.frontRightmotor, self.backRightmotor)
        self.drive.setDeadband(DriveConstant.kDeadband)
        self.drive.setMaxOutput(DriveConstant.kMaxOutput)
        
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
        SmartDashboard.putData("front left motor", self.frontLeftmotor)
        SmartDashboard.putNumber("front left Motor - data get", self.frontLeftmotor.get())
        SmartDashboard.putNumber("Back Left Motor - data", self.backLeftmotor.get())
        SmartDashboard.putNumber("Front Right Motor - data", self.frontRightmotor.get())
        SmartDashboard.putNumber("Back Right Motor - data", self.backRightmotor.get())

        SmartDashboard.putNumber("Front Left Encoder", self.frontLeftEncoder.getDistance())
        SmartDashboard.putNumber("Front Right Encoder", self.frontRightEncoder.getDistance())
        SmartDashboard.putNumber("Back Left Encoder", self.backLeftEncoder.getDistance())
        SmartDashboard.putNumber("Back Right Encoder", self.backRightEncoder.getDistance())
        SmartDashboard.putNumber("Gyro", self.gyro.getAngle())
        #endregion

    def resetEncoders(self):
        self.frontLeftEncoder.reset()
        self.frontRightEncoder.reset()
        self.backLeftEncoder.reset()
        self.backRightEncoder.reset()
    
    def getAverageEncoderDistance(self):
        avgEncoderDistance = (self.frontLeftEncoder.getDistance() + self.frontRightEncoder.getDistance() + self.backLeftEncoder.getDistance() + self.backRightEncoder.getDistance()) / 4.0
        return avgEncoderDistance
    



  