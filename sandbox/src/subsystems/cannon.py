

import wpilib
import commands2
from constants import CannonConstant

class Cannon(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        import commands.shooting
        self.Charge_Shoot = commands.shooting.Charge_Shoot
        
    