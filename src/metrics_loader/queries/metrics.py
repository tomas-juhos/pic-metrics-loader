"""Metrics queries."""

from .base import BaseQueries


class Queries(BaseQueries):
    """Metrics queries class."""

    UPSERT = (
        "INSERT INTO {timeframe}_metrics ("
        "       datadate, "
        "       gvkey, "
        "       utilization_pct_delta,"
        "       bar_delta, "
        "       age_delta, "
        "       tickets_delta, "
        "       units_delta, "
        "       market_value_usd_delta, "
        "       loan_rate_avg_delta, "
        "       loan_rate_max_delta, "
        "       loan_rate_min_delta, "
        "       loan_rate_range_delta, "
        "       loan_rate_stdev_delta, "
        "       short_interest, "
        "       short_ratio, "
        "       market_cap, "
        "       shares_out, "
        "       volume, "
        "       rtn, "
        "       winsorized_5_rtn"
        ") VALUES %s "
        "ON CONFLICT (datadate, gvkey) DO "
        "UPDATE SET "
        "       datadate=EXCLUDED.datadate, "
        "       gvkey=EXCLUDED.gvkey, "
        "       utilization_pct_delta=EXCLUDED.utilization_pct_delta, "
        "       bar_delta=EXCLUDED.bar_delta, "
        "       age_delta=EXCLUDED.age_delta, "
        "       tickets_delta=EXCLUDED.tickets_delta, "
        "       units_delta=EXCLUDED.units_delta, "
        "       market_value_usd_delta=EXCLUDED.market_value_usd_delta, "
        "       loan_rate_avg_delta=EXCLUDED.loan_rate_avg_delta, "
        "       loan_rate_max_delta=EXCLUDED.loan_rate_max_delta, "
        "       loan_rate_min_delta=EXCLUDED.loan_rate_min_delta, "
        "       loan_rate_range_delta=EXCLUDED.loan_rate_range_delta, "
        "       loan_rate_stdev_delta=EXCLUDED.loan_rate_stdev_delta, "
        "       short_interest=EXCLUDED.short_interest, "
        "       short_ratio=EXCLUDED.short_ratio, "
        "       market_cap=EXCLUDED.market_cap, "
        "       shares_out=EXCLUDED.shares_out, "
        "       volume=EXCLUDED.volume, "
        "       rtn=EXCLUDED.rtn, "
        "       winsorized_5_rtn=EXCLUDED.winsorized_5_rtn; "
    )
