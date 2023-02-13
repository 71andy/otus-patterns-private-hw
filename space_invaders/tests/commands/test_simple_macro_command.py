import pytest
from unittest.mock import Mock

from space_invaders.engine.commands import SimpleMacroCommand
from space_invaders.engine.interfaces import Command


def test_simple_macro_command():
    command1 = Mock(Command)
    command2 = Mock(Command)

    SimpleMacroCommand([command1, command2]).execute()

    command1.execute.assert_called_once()
    command2.execute.assert_called_once()


def test_simple_macro_command_with_exception():
    command1 = Mock(Command)
    command2 = Mock(Command)

    exception = Exception
    command1.execute.side_effect = exception()

    with pytest.raises(exception):
        SimpleMacroCommand([command1, command2]).execute()

    command1.execute.assert_called_once()
    command2.execute.assert_not_called()
