CREATE TABLE daily_metrics
(
    datadate                                  TIMESTAMP,
    gvkey                                     INTEGER,

    utilization_pct_delta                     DECIMAL(14,8),
    bar_delta                                 DECIMAL(14,8),
    age_delta                                 DECIMAL(18,7),
    tickets_delta                             DECIMAL(18,2),
    units_delta                               DECIMAL(18,4),
    market_value_usd_delta                    DECIMAL(18,2),
    loan_rate_avg_delta                       DECIMAL(18,9),
    loan_rate_max_delta                       DECIMAL(18,9),
    loan_rate_min_delta                       DECIMAL(18,9),
    loan_rate_range_delta                     DECIMAL(18,9),
    loan_rate_stdev_delta                     DECIMAL(18,9),

    short_interest                            DECIMAL(18,8),
    short_ratio                               DECIMAL(14,8),

    market_cap                                DECIMAL(30,15),
    shares_out                                DECIMAL(30,4),
    volume                                    DECIMAL(30,15),
    rtn                                       DECIMAL(25,15),
    winsorized_5_rtn                          DECIMAL(25,15),

    PRIMARY KEY (gvkey, datadate)
);