"""Metrics loader."""

import logging
from sys import stdout
import os
from typing import Dict, List

from metrics_loader.date_helpers import generate_years
import metrics_loader.model as model
from metrics_loader.model.entity import Entity
from metrics_loader.persistence import source, target
import metrics_loader.queries as queries
from metrics_loader.timeframe import TimeFrame

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)s [%(filename)s:%(lineno)d]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=stdout,
)

logger = logging.getLogger(__name__)


class Loader:
    """Loader class for cap iq returns."""

    YEARS = [
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
    ]

    _entities = {
        "metrics": Entity.METRICS,
    }

    _timeframes = {
        "monthly": TimeFrame.monthly,
        "weekly": TimeFrame.weekly,
        "daily": TimeFrame.daily,
    }

    _queries = {
        Entity.METRICS: queries.MetricsQueries,
    }

    def __init__(self) -> None:
        self.source = source.Source(os.environ.get("SOURCE"))
        self.target = target.Target(os.environ.get("TARGET"))

    def run(self) -> None:
        """Persists records to the metrics tables."""
        entity = self._entities["metrics"]
        for timeframe in self._timeframes.values():
            logger.info(f"Starting process for {timeframe}_metrics...")
            history: Dict[int, List[model.BaseData]] = {}

            # CHANGE HERE TO RUN BY YEAR INSTEAD OF SEMESTER
            date_ranges = generate_years(self.YEARS)

            last_date_persisted = self.target.fetch_last_date_persisted(timeframe)
            if last_date_persisted:
                date_ranges = [dr for dr in date_ranges if dr[1] >= last_date_persisted]

            n = len(date_ranges)
            i = 0
            for date_range in date_ranges:
                logger.info(f"Persisted {i}/{n} {timeframe}.")
                logger.debug("Fetching records...")

                raw_records = self.source.get_records(
                    timeframe=timeframe, date_range=date_range
                )

                if raw_records:
                    curated_records = [
                        model.BaseData.build_record(r) for r in raw_records
                    ]
                    logger.debug("Building history per gvkey...")

                    for record in curated_records:
                        if record.gvkey not in history.keys():
                            history[record.gvkey] = [record]
                        else:
                            history[record.gvkey].append(record)

                    for key in history.keys():
                        history[key].sort(key=lambda x: x.datadate)

                    # PROCESS WOULD BE IMPLEMENTED HERE
                    logger.debug("Curating records...")
                    records = []
                    for key in history.keys():
                        key_records = history[key]
                        for j in range(0, len(key_records) - 1):
                            metrics_record = model.Metrics.build_record(
                                prev_record=key_records[j], record=key_records[j + 1]
                            )
                            if not metrics_record.is_empty:
                                records.append(metrics_record.as_tuple())

                    logger.debug("Persisting records...")

                    records_slices = self.list_slicer(records, 100_000)
                    for records_slice in records_slices:
                        upsert_query = self._queries[entity].UPSERT.format(
                            timeframe=timeframe.value
                        )
                        self.target.execute(upsert_query, records_slice)

                    self.target.commit_transaction()

                    # SAVING LAST PERSISTED RECORD TO CALC CHANGE TO FIRST OF NEXT BATCH
                    for key in history.keys():
                        history[key] = [history[key][-1]]

                i += 1
            logger.info(f"Persisted {i}/{n} {timeframe}.")
        logger.info("Process finished. Terminating...")

    @staticmethod
    def list_slicer(lst: List, slice_len: int) -> List[List]:
        """Slice list into list of lists.

        Args:
            lst: list to slice.
            slice_len: size of each slice.

        Returns:
            Sliced list.
        """
        res = []
        i = 0
        while i + slice_len < len(lst):
            res.append(lst[i : i + slice_len])  # noqa
            i = i + slice_len
        res.append(lst[i:])
        return res


loader = Loader()
loader.run()
