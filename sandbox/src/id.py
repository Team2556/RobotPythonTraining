from enum import Enum, IntEnum, verify, UNIQUE

@verify(UNIQUE)
class vroom(IntEnum):
    speed = 10

vroom.speed
print(vroom.speed)
