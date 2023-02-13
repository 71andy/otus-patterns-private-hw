from space_invaders.engine.interfaces import Command


class SimpleMacroCommand(Command):
    """Простая макрокоманда (при выбросе исключения выполнение последовательность останавливается)

    Args:
        commands: список команд, объединенных в макрокоманду.
    """

    def __init__(self, command_list: list[Command]):
        self._command_list = command_list

    def execute(self) -> None:
        """Выполнить последовательность команд, пока не список команд не закончится или не возникнет
        исключение в одной из команд"""
        for command in self._command_list:
            command.execute()
