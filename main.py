"""
=======================================================================
Scheduling with Constraint Programming
=======================================================================

A scheduler with configurable constraints. It takes a CSV as
input. An example CSV is included in the repository.

Guidelines for the algorithm:

- A given grouping of jobs should not have a value exceeding the
TOTAL_VALUE_LIMIT (in hours). Note this should take into account the
possibility of time overlaps, and in such situations values should be
calculated by the difference between start and end times rather than
using the value provided in the "Value" column from the input.

- Any pairing of jobs' start and end times may overlap by at most
the value of ALLOWABLE_OVERLAP (in minutes).

- The output file should be identical to the input file, with an added
"Group" column containing a value that matches between the grouped
jobs.

TODO:
    - Complete algorithm/get code working
    - Account for end times past midnight by adding +1 day to those
    instances (so they are sorted properly)
    - Convert times back to a more readable format, without the date
    before writing to output file and console

"""

import datetime
from typing import (
    Any,
    Union,
)

import pandas as pd
from pandas import (
    DataFrame,
    Series,
)
from pandas.io.parsers import TextFileReader

from classes import Job

from config import (
    ALLOWABLE_OVERLAP,
    FILE_TO_READ,
    TOTAL_VALUE_LIMIT,
    PARSE_DATES,
    OUTPUT_FILE,
)

df: pd.DataFrame = pd.read_csv(FILE_TO_READ, parse_dates=PARSE_DATES)

for x in df.index:
    task = "task_" + str(df["Task"].iloc[x])
    job = df["Job"].iloc[x]
    start_time = df["Start"].iloc[x]
    end_time = df["End"].iloc[x]
    value = df["Value"].iloc[x]
    priority = df["Priority"].iloc[x]
    task = Job(job, start_time, end_time, value, priority)
    print(task.job, task.start_time)

overlap = datetime.timedelta(minutes=ALLOWABLE_OVERLAP)


"""df_end_times = df.filter(items=["Task", "End", "Priority"])
df_start_times = df.filter(items=["Task", "Start", "End", "Val", "Job"])

def comparator(
    start_time: pd.DataFrame,
    end_times: pd.DataFrame = df_end_times,
) -> "int64":
    tasks = (end_times.loc[end_times["End"] < start_time]).sort_values(by="End").Task
    if tasks.empty:
        return float("nan")
    return tasks.iloc[-1]


df_start_times["Group"] = df_start_times["Start"].apply(comparator)
df_start_times.to_csv(OUTPUT_FILE, index=False)"""
