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
from typing import Any, Union

import pandas as pd
from pandas import DataFrame, Series
from pandas.io.parsers import TextFileReader

from classes import Job
from config import (
    ALLOWABLE_OVERLAP,
    FILE_TO_READ,
    OUTPUT_FILE,
    PARSE_DATES,
    TOTAL_VALUE_LIMIT,
)

df: pd.DataFrame = pd.read_csv(FILE_TO_READ, parse_dates=PARSE_DATES)
overlap = datetime.timedelta(minutes=ALLOWABLE_OVERLAP)

# Create a list of Jobs with corresponding attributes from the data frame.
list_of_jobs = []
for x in df.index:
    id = "task_" + str(df["Task"].iloc[x])
    job = df["Job"].iloc[x]
    start_time = df["Start"].iloc[x]
    end_time = df["End"].iloc[x]
    value = df["Value"].iloc[x]
    priority = df["Priority"].iloc[x]
    list_of_jobs.append(Job(id, job, start_time, end_time, value, priority))

# Test calls
print(list_of_jobs)
print(list_of_jobs[0].job)

# Testing a comparative loop in list; proof of concept.
for x in list_of_jobs:
    if x.job == "13301":
        print(1)
    else:
        print(0)

# Testing a comparative loop; print matches of jobs if job start is later than job end.
for x in list_of_jobs:
    for y in list_of_jobs:
        if x.start_time > y.end_time:
            i = (y.job, y.end_time, x.job, x.start_time)
            print(i)