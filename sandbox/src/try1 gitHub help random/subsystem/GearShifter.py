import wpilib
import commands2
from id import PWM_channels, DIO_channels, PCM_channels,Solenoid_modules,Gears
from  try3_bust_with_poenix.constants import DriveConstants
# the gear shifter is a pneumatic switch that changes the gear ratio of the robot drivetrain
# it is a subsystem that is controlled by the driver
# the gear shifter has two states, high and low
# the gear shifter is controlled by a solenoid
# the gear shifter is a subsystem
# the gear shifter has a default command to go to low gear
# the gear shifter has a command to go to high gear



class GearShifter(commands2.Subsystem):
	# super().__init__()
	def __init__(self):
		# Initialize any variables or resources here
		self.selected_gear = Gears.LOW_GEAR # Default gear is low, use 0 in  so False is low gear
		self.gear_shifter = wpilib.Solenoid(module=Solenoid_modules.GEAR_SHIFTER,
									   moduleType=DriveConstants.kGearSifterModule,
									   channel=PCM_channels.GEAR_SHIFTER)
		self.gear_shifter.set(on = (self.selected_gear==Gears.HIGH_GEAR))
		
		
		

	def high_gear(self):
		# Implement the logic to shift to high gear here
		self.selected_gear = id.HIGH_GEAR
		self.gear_shifter.set(on = (self.selected_gear==Gears.HIGH_GEAR))

	def low_gear(self):
		# Implement the logic to shift to low gear here
		self.selected_gear = id.LOW_GEAR
		self.gear_shifter.set(on = (self.selected_gear==Gears.HIGH_GEAR))
