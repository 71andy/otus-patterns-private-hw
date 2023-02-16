import pytest

from space_invaders.engine import exceptions
from space_invaders.engine.commands import MoveWithFuelBurning
from space_invaders.engine.interfaces import FuelBurner, FuelChecker, MoveController
from space_invaders.tests.utils import build_mock_object


class MoveControllerWithFuelBurning(FuelBurner, FuelChecker, MoveController):
    pass


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption', 'expected_fuel_level', 'position', 'velocity', 'expected_position'),
    [
        (10, 1, 9, (12, 5), (-7, 3), (5, 8)),
        (10, 10, 0, (3, 5), (7, -7), (10, -2)),
    ],
)
def test_burn_fuel_positive(
    fuel_level,
    fuel_consumption,
    expected_fuel_level,
    position,
    velocity,
    expected_position,
):
    mock = build_mock_object(
        MoveControllerWithFuelBurning,
        fuel_level=fuel_level,
        fuel_consumption=fuel_consumption,
        position=position,
        velocity=velocity,
    )
    MoveWithFuelBurning(mock).execute()

    assert mock.fuel_level == expected_fuel_level
    assert mock.position == expected_position


@pytest.mark.parametrize(
    ('fuel_level', 'fuel_consumption', 'expected_exception', 'position', 'velocity', 'expected_position'),
    [
        (1, 10, exceptions.NegativeFuelLevelError, (0, 0), (1, 0), (0, 0)),
        (0, 1, exceptions.NegativeFuelLevelError, (0, 0), (1, 0), (0, 0)),
    ],
)
def test_burn_fuel_negative(
    fuel_level,
    fuel_consumption,
    expected_exception,
    position,
    velocity,
    expected_position,
):
    mock = build_mock_object(
        MoveControllerWithFuelBurning,
        fuel_level=fuel_level,
        fuel_consumption=fuel_consumption,
        position=position,
        velocity=velocity,
    )
    with pytest.raises(expected_exception):
        MoveWithFuelBurning(mock).execute()
    assert mock.position == expected_position
