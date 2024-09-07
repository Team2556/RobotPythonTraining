from enum import IntEnum, unique, verify

@unique
class dummy_ID(IntEnum):
    A = 1
    B = 2
    C = 3

@unique
class PWM_channels(IntEnum):
    LEFT_FRONT_MOTOR = 1
    LEFT_REAR_MOTOR = 2
    RIGHT_FRONT_MOTOR = 3
    RIGHT_REAR_MOTOR = 4


@unique
class DIO_channels(IntEnum):
    LIMIT_SWITCH_DOWN = 5
    LIMIT_SWITCH_UP = 6

@unique
class PCM_channels(IntEnum):
    AIR_CANNON = 7
    CANNON_ACTUATOR = 8
    GEAR_SHIFTER = 9

@unique
class Solenoid_modules(IntEnum):
    GEAR_SHIFTER = 1
    FIRE = 2

@unique
class Gears(IntEnum):
    LOW_GEAR = 0
    HIGH_GEAR = 1