import wpilib
# import wpimath.controller
import commands2
import commands2.cmd
import commands2.button
from commands2 import Command
from commands2 import CommandScheduler
from commands2 import ConditionalCommand
from commands2 import DeferredCommand
from commands2 import FunctionalCommand
from constants import ArmConstants

from id import PWM_channels, DIO_channels, PCM_channels,Solenoid_modules,Gears 


class AirCannon(commands2.Subsystem):
    def __init__(self):
        super().__init__()

        self.aircannon = wpilib.Solenoid(module=Solenoid_modules.FIRE,
                                         moduleType= wpilib.PneumaticsModuleType.REVPH,#ArmConstants.kFireControlModule,
                                         channel=PCM_channels.AIR_CANNON)
        self.aircannon.set(False)
        # initalize the pneumatic system
        self.compressor = wpilib.Compressor(moduleType= wpilib.PneumaticsModuleType.REVPH)#ArmConstants.kFireControlModule)
        # wpilib._wpilib.Compressor(moduleType: wpilib._wpilib.PneumaticsModuleType)


    # create pneumatic charging and firing capabilities
    # this goes into the air cannon, we assume that the air cannon is a solenoid, and there is only one tank
    # TODO: extent to multiple tanks
    def pump(self):
        self.compressor.start().setClosedLoopControl(True).setPressureSwitchValue(120).setCompressorCurrent(0.0)

    def fire(self):
        # fire if the compressor has a tank pressure of 120 psi
        if self.compressor.getPressureSwitchValue() == 120:
            self.aircannon.set(True)
        else:
            self.aircannon.set(False)
    
    def stop(self):
        self.compressor.stop().setClosedLoopControl(False).setPressureSwitchValue(0).setCompressorCurrent(0.0)
        self.aircannon.set(False)




    #this goes into the cannonactuator


