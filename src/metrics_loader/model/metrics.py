"""Metrics model."""

from datetime import datetime
from decimal import Decimal
import logging
from typing import Optional, Tuple

from metrics_loader.model.base import Modeling
from metrics_loader.model.base_data import BaseData

logger = logging.getLogger(__name__)


class Metrics(Modeling):
    """Metrics record object class."""

    datadate: datetime
    gvkey: int

    utilization_pct_delta: Optional[Decimal] = None
    bar_delta: Optional[int] = None
    age_delta: Optional[Decimal] = None
    tickets_delta: Optional[int] = None
    units_delta: Optional[Decimal] = None
    market_value_usd_delta: Optional[Decimal] = None
    loan_rate_avg_delta: Optional[Decimal] = None
    loan_rate_max_delta: Optional[Decimal] = None
    loan_rate_min_delta: Optional[Decimal] = None
    loan_rate_range_delta: Optional[Decimal] = None
    loan_rate_stdev_delta: Optional[Decimal] = None

    short_interest: Optional[Decimal] = None
    short_ratio: Optional[Decimal] = None

    market_cap: Optional[Decimal] = None
    shares_out: Optional[Decimal] = None
    rtn: Optional[Decimal] = None

    @classmethod
    def build_record(cls, prev_record: BaseData, record: BaseData) -> "Metrics":
        res = cls()

        res.datadate = record.datadate
        res.gvkey = record.gvkey

        res.utilization_pct_delta = (
            record.utilization_pct - prev_record.utilization_pct
            if record.utilization_pct and prev_record.utilization_pct
            else None
        )
        res.bar_delta = (
            record.bar - prev_record.bar if record.bar and prev_record.bar else None
        )
        res.age_delta = (
            record.age - prev_record.age if record.age and prev_record.age else None
        )
        res.tickets_delta = (
            record.tickets - prev_record.tickets
            if record.tickets and prev_record.tickets
            else None
        )
        res.units_delta = (
            record.units - prev_record.units
            if record.units and prev_record.units
            else None
        )
        res.market_value_usd_delta = (
            record.market_value_usd - prev_record.market_value_usd
            if record.market_value_usd and prev_record.market_value_usd
            else None
        )
        res.loan_rate_avg_delta = (
            record.loan_rate_avg - prev_record.loan_rate_avg
            if record.loan_rate_avg and prev_record.loan_rate_avg
            else None
        )
        res.loan_rate_max_delta = (
            record.loan_rate_max - prev_record.loan_rate_max
            if record.loan_rate_max and prev_record.loan_rate_max
            else None
        )
        res.loan_rate_min_delta = (
            record.loan_rate_min - prev_record.loan_rate_min
            if record.loan_rate_min and prev_record.loan_rate_min
            else None
        )
        res.loan_rate_range_delta = (
            record.loan_rate_range - prev_record.loan_rate_range
            if record.loan_rate_range and prev_record.loan_rate_range
            else None
        )
        res.loan_rate_stdev_delta = (
            record.loan_rate_stdev - prev_record.loan_rate_stdev
            if record.loan_rate_stdev and prev_record.loan_rate_stdev
            else None
        )

        res.short_interest = (
            record.units / record.shares_out
            if record.units and record.shares_out
            else None
        )
        res.short_ratio = (
            (record.market_value_usd / 1_000_000) / record.market_cap
            if record.market_value_usd and record.market_cap
            else None
        )

        res.market_cap = record.market_cap
        res.shares_out = record.shares_out
        res.rtn = record.rtn

        return res

    def as_tuple(self) -> Tuple:
        return (
            self.datadate,
            self.gvkey,
            self.utilization_pct_delta,
            self.bar_delta,
            self.age_delta,
            self.tickets_delta,
            self.units_delta,
            self.market_value_usd_delta,
            self.loan_rate_avg_delta,
            self.loan_rate_max_delta,
            self.loan_rate_min_delta,
            self.loan_rate_range_delta,
            self.loan_rate_stdev_delta,
            self.short_interest,
            self.short_ratio,
            self.market_cap,
            self.shares_out,
            self.rtn,
        )

    @property
    def is_empty(self) -> bool:
        if (
            self.utilization_pct_delta is None
            and self.bar_delta is None
            and self.age_delta is None
            and self.tickets_delta is None
            and self.units_delta is None
            and self.market_value_usd_delta is None
            and self.loan_rate_avg_delta is None
            and self.loan_rate_max_delta is None
            and self.loan_rate_min_delta is None
            and self.loan_rate_range_delta is None
            and self.loan_rate_stdev_delta is None
            and self.short_interest is not None
            and self.short_ratio is None
        ):
            return True
        else:
            return False
