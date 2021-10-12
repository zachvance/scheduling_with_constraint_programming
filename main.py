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

"""

from datetime import datetime, timedelta
from typing import Any, Union

import pandas as pd
from pandas import DataFrame, Series
from pandas.io.parsers import TextFileReader

from classes import Group, Job
from config import \
    PARSE_DATES  # No longer required using strptime and formatting.
from config import (ALLOWABLE_OVERLAP, FILE_TO_READ, OUTPUT_FILE,
                    TOTAL_VALUE_LIMIT)

# df: pd.DataFrame = pd.read_csv(FILE_TO_READ, parse_dates=PARSE_DATES)
df: pd.DataFrame = pd.read_csv(FILE_TO_READ)
overlap = timedelta(minutes=ALLOWABLE_OVERLAP)

# Create a list of Jobs with corresponding attributes from the data frame.
list_of_jobs = []

for x in df.index:
    job_id = "task_" + str(df["Task"].iloc[x])
    job = df["Job"].iloc[x]
    start_time = df["Start"].iloc[x]
    end_time = df["End"].iloc[x]
    value = df["Value"].iloc[x]
    priority = df["Priority"].iloc[x]
    list_of_jobs.append(Job(job_id, job, start_time, end_time, value, priority))

# --------

# Testing a comparative loop in list; proof of concept.
"""for x in list_of_jobs:
    if x.job == "13301":
        print(1)
    else:
        print(0)"""

# --------

# Testing a comparative loop; print matches of jobs if job start is
# later than job end and sum of job values is less than 13.
"""for x in list_of_jobs:
    for y in list_of_jobs:
        if x.start_time > (y.end_time - overlap) and x.value + y.value < 13:
            i = (y.job, y.end_time, x.job, x.start_time, round(x.value + y.value, 2))
            list_of_jobs.remove(y)
            print(i)"""

# Print leftover jobs:
"""for x in list_of_jobs:
    print(x.job)"""

# --------

# Continuation of loop; adding the matches to a group to then compare
# which match is the 'best' (whichever match has the least time gap
# between start and end)

"""for y in list_of_jobs:
    print(y.job, y.end_time)"""

"""future = datetime.timedelta(hours=13)
group = []
for x in list_of_jobs:
    for y in list_of_jobs:
        if x.start_time > (y.end_time - overlap) and (y.end_time - x.start_time)
         < future:
            z = [y, x]
            #list_of_jobs.remove(y)
            group.append(z)

# Print the number of minutes difference between start and end times of the pairs:
for pair in group:
    print(pair[0].job, pair[1].job, (pair[1].start_time - pair[0].end_time).seconds
     // 60)"""

# --------

# New attempt at solving:

jobs_over_x_hours = []
possible_matches = []
time_format = "%I:%M %p"

for job in list_of_jobs:
    if job.value > 8:
        list_of_jobs.remove(job)
        jobs_over_x_hours.append(job)

for x in list_of_jobs:
    for y in list_of_jobs:
        if x.end_time < y.start_time and x.value + y.value < TOTAL_VALUE_LIMIT:
            possible_matches.append([x, y])

dictionary_to_compare = {}
list_to_compare = []
for match in possible_matches:
    start_time = datetime.strptime(match[1].start_time, time_format)
    end_time = datetime.strptime(match[0].end_time, time_format)
    min_difference = start_time - (end_time - overlap)
    if min_difference.days < 0:
        min_difference = timedelta(
            days=0,
            seconds=min_difference.seconds,
            microseconds=min_difference.microseconds,
        )
    # print(match[0].job, match[1].job, min_difference)
    comparator = (match[0].job, match[1].job, min_difference)
    list_to_compare.append(comparator)

for x in list_to_compare:
    values = [x[1], x[2]]
    dictionary_to_compare.setdefault(x[0], []).append(values)

for key in dictionary_to_compare:
    for x in dictionary_to_compare[key]:
        print(key, x[1])
    # print(key, dictionary_to_compare[key])

for x in jobs_over_x_hours:
    print(x.job + " is leftover")
