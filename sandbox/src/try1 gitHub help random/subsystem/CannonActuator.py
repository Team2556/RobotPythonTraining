
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import wpimath.controller
import wpimath.trajectory

import constants


class CannonActuator(commands2.ProfiledPIDSubsystem):
    """A robot arm subsystem that moves with a motion profile."""

    # Create a new ArmSubsystem
    def __init__(self) -> None:
        super().__init__(
            wpimath.controller.ProfiledPIDController(
                constants.ArmConstants.kP,
                0,
                0,
                wpimath.trajectory.TrapezoidProfile.Constraints(
                    constants.ArmConstants.kMaxVelocityRadPerSecond,
                    constants.ArmConstants.kMaxAccelerationRadPerSecSquared,
                ),
            ),
            0,
        )

        self.motor = wpilib.PWMSparkMax(constants.ArmConstants.kMotorPort)
        self.encoder = wpilib.Encoder(
            constants.ArmConstants.kEncoderPorts[0],
            constants.ArmConstants.kEncoderPorts[1],
        )
        self.feedforward = wpimath.controller.ArmFeedforward(
            constants.ArmConstants.kSVolts,
            constants.ArmConstants.kGVolts,
            constants.ArmConstants.kVVoltSecondPerRad,
            constants.ArmConstants.kAVoltSecondSquaredPerRad,
        )

        self.encoder.setDistancePerPulse(
            constants.ArmConstants.kEncoderDistancePerPulse
        )

        # Start arm at rest in neutral position
        self.setGoal(constants.ArmConstants.kArmOffsetRads)

    # TODO: look into using the gravity feedforward options
    def useOutput(
        self, output: float, setpoint: wpimath.trajectory.TrapezoidProfile.State
    ) -> None:
        # Calculate the feedforward from the setpoint
        feedforward = self.feedforward.calculate(setpoint.position, setpoint.velocity)

        # Add the feedforward to the PID output to get the motor output
        self.motor.setVoltage(output + feedforward)

    def getMeasurement(self) -> float:
        return self.encoder.getDistance() + constants.ArmConstants.kArmOffsetRads






# import wpilib
# import wpimath.controller
# import commands2
# import commands2.cmd
# import commands2.button


# from id import PWM_channels, DIO_channels, PCM_channels,Solenoid_modules,Gears

# # aim up or down with the cannon regardless of its firing state

# # rework this to be a trapazoidal profile subsystem with tallon srx motor controllers; well this is like an arm extended and actuated by a motor
# # the cannon actuator is a subsystem that is controlled by the driver




# class CannonActuator(commands2.Subsystem):
#     def __init__(self):
#         super().__init__()

#         self.cannonactuator = wpilib.Solenoid(module=Solenoid_modules., channel=id.CANNON_ACTUATOR)
#         self.cannonactuator.set(False)
#         # initalize the pneumatic system
#         self.compressor = wpilib.Compressor()
#         #initalize a limit switch to stop the cannon from going too far up and one for down
#         self.limitSwitchUp = wpilib.DigitalInput(channel=id.LIMIT_SWITCH_UP)
#         self.limitSwitchDown = wpilib.DigitalInput(channel=id.LIMIT_SWITCH_DOWN)

#     # need to define the periodc function... maybe check on xbox right joystick up and down for cannon actuator
#     def periodic(self):
#         pass





#     # create pneumatic charging and firing capabilities
#     # this goes into the air cannon, we assume that the air cannon is a solenoid, and there is only one tank
#     def extend(self):
#         self.cannonactuator.setSolonoidCurrent(id.CANNON_UP_SOL).setClosedLoopControl(True).conditionWhenPressed(self.limitSwitchUp.get()).setSolonoidCurrent(0.0)
#         # if the limit switch is pressed, stop the cannon from going up
#         # if self.limitSwitchUp.get() == True:
#         #     self.cannonactuator.set(False)
#         # else:
#         #     self.cannonactuator.set(True)

#     def retract(self):
#         self.cannonactuator.setSolonoidCurrent(id.CANNON_DOWN_SOL).setClosedLoopControl(True).conditionWhenPressed(self.limitSwitchDown.get()).setSolonoidCurrent(0.0)  

#     def isFullyExtended(self):
#         return self.limitSwitchUp.get() == True
#     def isFullyRetracted(self):
#         return self.limitSwitchDown.get() == True