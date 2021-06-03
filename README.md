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
