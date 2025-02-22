# ISO 8601 date/time parser

[![PyPI version](https://img.shields.io/pypi/v/isodate2.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/isodate2)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/isodate2.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/isodate2)
[![PyPI downloads](https://img.shields.io/pypi/dm/isodate2.svg)](https://pypistats.org/packages/isodate2)
[![GitHub Actions status](https://github.com/isodate/isodate/actions/workflows/test.yml/badge.svg)](https://github.com/isodate/isodate/actions)
[![Codecov](https://codecov.io/gh/isodate/isodate/branch/main/graph/badge.svg?token=Ck33cyrNid)](https://codecov.io/gh/isodate/isodate)
[![Licence](https://img.shields.io/pypi/l/isodate2.svg)](https://pypi.org/project/isodate2/)

## isodate2 is a fork of isodate

This module implements ISO 8601 date, time and duration parsing.
The implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non-existent, and not as an allowed
option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not
intended by this module to support 2 digit years. (while it may still
be valid as ISO date, because it is not explicitly forbidden.)
Another example is, when no time zone information is given for a time,
then it should be interpreted as local time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types, like
*date*, *time*, *datetime* and *timedelta*, it is not possible to convert
all possible ISO 8601 dates/times. For instance, dates before 0001-01-01 are
not allowed by the Python *date* and *datetime* classes. Additionally
fractional seconds are limited to microseconds. That means if the parser finds
for instance nanoseconds it will round it to microseconds.

## Documentation

There are five parsing methods available.

* `parse_time`:
     parses an ISO 8601 time string into a *time* object
* `parse_date`:
     parses an ISO 8601 date string into a *date* object
* `parse_datetime`:
     parses an ISO 8601 date-time string into a *datetime* object
* `parse_duration`:
     parses an ISO 8601 duration string into a *timedelta* or *Duration*
     object.
* `parse_tzinfo`:
     parses the time zone info part of an ISO 8601 string into a
     *tzinfo* object.

As ISO 8601 allows to define durations in years and months, and *timedelta*
does not handle years and months, this module provides a *Duration* class,
which can be used almost like a *timedelta* object (with some limitations).
However, a *Duration* object can be converted into a *timedelta* object.

There are also ISO formatting methods for all supported data types. Each
*xxx_isoformat* method accepts a format parameter. The default format is
always the ISO 8601 expanded format. This is the same format used by
*datetime.isoformat*:

* `time_isoformat`:
    Intended to create ISO time strings with default format
    *hh:mm:ssZ*.
* `date_isoformat`:
    Intended to create ISO date strings with default format
    *yyyy-mm-dd*.
* `datetime_isoformat`:
    Intended to create ISO date-time strings with default format
    *yyyy-mm-ddThh:mm:ssZ*.
* `duration_isoformat`:
    Intended to create ISO duration strings with default format
    *PnnYnnMnnDTnnHnnMnnS*.
* `tz_isoformat`:
    Intended to create ISO time zone strings with default format
    *hh:mm*.
* `strftime`:
    A re-implementation mostly compatible with Python's *strftime*, but
    supports only those format strings, which can also be used for dates
    prior 1900. This method also understands how to format *datetime* and
    *Duration* instances.

## Installation

```sh
python -m pip install isodate2
```

## Limitations

* The parser accepts several date/time representation which should be invalid
  according to ISO 8601 standard.

1. for date and time together, this parser accepts a mixture of basic and extended format.
   e.g. the date could be in basic format, while the time is accepted in extended format.
   It also allows short dates and times in date-time strings.
2. For incomplete dates, the first day is chosen. e.g. 19th century results in a date of
   1901-01-01.
3. negative *Duration* and *timedelta* value are not fully supported yet.

## Further information

The doc strings and unit tests should provide rather detailed information about
the methods and their limitations.

The source release provides a *setup.py* script,
which can be used to run the unit tests included.

Source code is available at https://github.com/isodate/isodate.

## See also

[isoduration](https://github.com/bolsote/isoduration) is a well-maintained library which
aims to improve upon isodate:

> The state of the art of ISO 8601 duration handling in Python is more or less limited
> to what's offered by [`isodate`](https://pypi.org/project/isodate/). What we are
> trying to achieve here is to address the shortcomings of `isodate` (as described in
> their own [_Limitations_](https://github.com/gweis/isodate/#limitations) section), and
> a few of our own annoyances with their interface, such as the lack of uniformity in
> their handling of types, and the use of regular expressions for parsing.
