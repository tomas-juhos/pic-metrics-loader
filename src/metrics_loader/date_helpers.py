"""Helper functions to deal with timeframes."""
from datetime import datetime
from typing import List
import logging

logger = logging.getLogger(__name__)


def generate_semesters(years: List[int]):
    intervals = []
    for year in years:
        intervals = intervals + [
            (datetime(year, 1, 1), datetime(year, 6, 30)),
            (datetime(year, 7, 1), datetime(year, 12, 31)),
        ]

    return intervals


def generate_years(years: List[int]):
    intervals = []
    for year in years:
        intervals.append((datetime(year, 1, 1), datetime(year, 12, 31)))

    return intervals
