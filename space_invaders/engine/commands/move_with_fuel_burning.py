from space_invaders.engine.commands.burn_fuel import BurnFuel
from space_invaders.engine.commands.change_straight_line_position import Move
from space_invaders.engine.commands.check_fuel import CheckFuel
from space_invaders.engine.commands.simple_macro_command import SimpleMacroCommand


class MoveWithFuelBurning(SimpleMacroCommand):
    """Макрокоманда движения по прямой с расходом топлива"""

    commands_sequence = (CheckFuel, Move, BurnFuel)

    def __init__(self, obj):
        super().__init__([command(obj) for command in self.commands_sequence])
