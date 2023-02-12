import pytest
from unittest.mock import Mock

from space_invaders.engine import exceptions
from space_invaders.engine.commands import CheckFuel
from space_invaders.engine.interfaces import FuelChecker


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption'),
    [
        (10, 1),
        (10, -1),
        (10, 10),
    ],
)
def test_check_fuel_enough(fuel_level, fuel_consumption):

    mock = Mock(FuelChecker)
    mock.fuel_level = fuel_level
    mock.fuel_consumption = fuel_consumption

    try:
        CheckFuel(mock).execute()
    except Exception as exc:
        pytest.fail(f'CheckFuel raised an exception {type(exc).__name__}')


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption', 'expected_exception'),
    [
        (1, 10, exceptions.NegativeFuelLevelError),
        (0, 1, exceptions.NegativeFuelLevelError),
    ],
)
def test_burn_fuel_not_enough(fuel_level, fuel_consumption, expected_exception):
    mock = Mock(FuelChecker)
    mock.fuel_level = fuel_level
    mock.fuel_consumption = fuel_consumption

    with pytest.raises(expected_exception):
        CheckFuel(mock).execute()
