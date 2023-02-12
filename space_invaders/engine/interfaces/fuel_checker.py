from abc import ABC, abstractmethod


class FuelChecker(ABC):
    """Объект, позволяющий проверять, достаточно ли текущего уровня топлива для совершения движения."""

    @property
    @abstractmethod
    def fuel_level(self) -> int:
        """Уровень топлива."""

    @property
    @abstractmethod
    def fuel_consumption(self) -> int:
        """Расход топлива."""
