"""Contains State and Component utilities"""
from typing import Callable, List
from abc import ABC, abstractmethod


class State(ABC):
    """State ABC for states"""

    @abstractmethod
    def handle(self):
        """Abstract method for handling state trnsition"""


StateList = List[Callable]


class Component(ABC):
    """Component ABC for stateful components"""
    def __init__(self, states: StateList) -> None:
        self._states = states
        self._current_state = None

    def set_state(self, new_state: State) -> None:
        """Set state of component"""
        self._current_state = new_state
        self._current_state.handle()
