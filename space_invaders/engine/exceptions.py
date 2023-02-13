class EGetPositionError(Exception):
    """Не определено значение координат"""


class EGetVelocityError(Exception):
    """Не определено значение скорости"""


class NegativeAngularVelocityError(Exception):
    """Исключение при получении отрицательного значения угловой скорости"""


class NegativeFuelLevelError(Exception):
    """Отрицательный уровень топлива."""


class NegativeLinearVelocityError(Exception):
    """Исключение при получении отрицательного значения линейной скорости"""
