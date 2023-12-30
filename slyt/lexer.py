from contextlib import suppress
from os import listdir
import os
from typing import Any, Generic, Callable, TypeVar, Generator

from slyt.state import State


################################################################################
# Types
################################################################################

class LexerType: ...


class Command(LexerType):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.func: Callable[[State, list[Argument[Any]]], State] = __import__(f"slyt.commands.{name}").func


T = TypeVar("T")
class Argument(Generic[T], LexerType):
    def __init__(self, value: T) -> None:
        self.type_ = T
        self.value: T = value



################################################################################
# Functions
################################################################################


def lexer(lines: list[str]) -> Generator[list[LexerType], Any, None]:
    for line in lines:
        # Removing comments
        if line.startswith("#"):
            continue
        with suppress(ValueError):
            line = line[:line.index("#")]

        yield [get_type(token) for token in line.split()]


def get_type(token: str) -> LexerType:
    if f"{token}.py" in listdir(f"slyt{os.path.sep}commands"):
        return Command(token)
    else:
        if token.isdigit():
            return Argument[int](int(token))
        else:
            return Argument[str](token)