from space_invaders.engine import exceptions
from space_invaders.engine.interfaces import Command, FuelChecker


class CheckFuel(Command):
    """Проверить достаточно ли текущего уровня топлива для перемещения.

    Args:
        obj: Объект, для которого выполняется проверка текущего уровня топлива.
    """

    def __init__(self, obj: FuelChecker):
        self.obj = obj

    def execute(self) -> None:
        """Выполнить действие.

        Raises:
            NegativeFuelLevelError: Попытка сжигания топлива приведет к отрицательному уровню топлива.
        """
        if self.obj.fuel_level - self.obj.fuel_consumption < 0:
            raise exceptions.NegativeFuelLevelError
