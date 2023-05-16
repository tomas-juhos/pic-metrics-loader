"""Timeframes enum class."""
from enum import Enum


class TimeFrame(str, Enum):
    """Possible timeframes for aggregates."""

    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
