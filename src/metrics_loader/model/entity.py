"""Entity file."""

from enum import Enum


class Entity(str, Enum):
    """Entities."""

    METRICS = "metrics"

    def __repr__(self) -> str:
        return str(self.value)
