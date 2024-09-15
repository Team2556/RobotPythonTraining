

import wpilib
import commands2
from try3_bust_with_poenix.constants import CannonConstant

class Cannon(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        import commands.shooting
        self.Charge_Shoot = commands.shooting.Charge_Shoot
        
    