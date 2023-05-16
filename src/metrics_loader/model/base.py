"""Abstract model."""

from abc import ABC, abstractmethod
from typing import Tuple


class Modeling(ABC):
    """Modeling abstract class."""

    @classmethod
    @abstractmethod
    def build_record(cls, prev_record, record) -> "Modeling":
        """Transforms record into record object.

        Args:
            prev_record: previous record.
            record: record to be record object.

        Returns:
            Record object for the given entity.
        """

    @abstractmethod
    def as_tuple(self) -> Tuple:
        """Returns object values as a tuple.

        Returns:
            Record object attributes as a tuple.
        """
