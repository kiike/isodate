##############################################################################
# Copyright 2009, Gerhard Weis
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#  * Neither the name of the authors nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT
##############################################################################
"""
Import all essential functions and constants to re-export them here for easy
access.

This module contains also various pre-defined ISO 8601 format strings.
"""
from isodate.duration import Duration
from isodate.isodates import date_isoformat, parse_date
from isodate.isodatetime import datetime_isoformat, parse_datetime
from isodate.isoduration import duration_isoformat, parse_duration
from isodate.isoerror import ISO8601Error
from isodate.isostrf import (
    D_ALT_BAS,
    D_ALT_BAS_ORD,
    D_ALT_EXT,
    D_ALT_EXT_ORD,
    D_DEFAULT,
    D_WEEK,
    DATE_BAS_COMPLETE,
    DATE_BAS_MONTH,
    DATE_BAS_ORD_COMPLETE,
    DATE_BAS_WEEK,
    DATE_BAS_WEEK_COMPLETE,
    DATE_CENTURY,
    DATE_EXT_COMPLETE,
    DATE_EXT_MONTH,
    DATE_EXT_ORD_COMPLETE,
    DATE_EXT_WEEK,
    DATE_EXT_WEEK_COMPLETE,
    DATE_YEAR,
    DT_BAS_COMPLETE,
    DT_BAS_ORD_COMPLETE,
    DT_BAS_WEEK_COMPLETE,
    DT_EXT_COMPLETE,
    DT_EXT_ORD_COMPLETE,
    DT_EXT_WEEK_COMPLETE,
    TIME_BAS_COMPLETE,
    TIME_BAS_MINUTE,
    TIME_EXT_COMPLETE,
    TIME_EXT_MINUTE,
    TIME_HOUR,
    TZ_BAS,
    TZ_EXT,
    TZ_HOUR,
    strftime,
)
from isodate.isotime import parse_time, time_isoformat
from isodate.isotzinfo import parse_tzinfo, tz_isoformat
from isodate.tzinfo import LOCAL, UTC, FixedOffset

__all__ = [
    "parse_date",
    "date_isoformat",
    "parse_time",
    "time_isoformat",
    "parse_datetime",
    "datetime_isoformat",
    "parse_duration",
    "duration_isoformat",
    "ISO8601Error",
    "parse_tzinfo",
    "tz_isoformat",
    "UTC",
    "FixedOffset",
    "LOCAL",
    "Duration",
    "strftime",
    "DATE_BAS_COMPLETE",
    "DATE_BAS_ORD_COMPLETE",
    "DATE_BAS_WEEK",
    "DATE_BAS_WEEK_COMPLETE",
    "DATE_CENTURY",
    "DATE_EXT_COMPLETE",
    "DATE_EXT_ORD_COMPLETE",
    "DATE_EXT_WEEK",
    "DATE_EXT_WEEK_COMPLETE",
    "DATE_YEAR",
    "DATE_BAS_MONTH",
    "DATE_EXT_MONTH",
    "TIME_BAS_COMPLETE",
    "TIME_BAS_MINUTE",
    "TIME_EXT_COMPLETE",
    "TIME_EXT_MINUTE",
    "TIME_HOUR",
    "TZ_BAS",
    "TZ_EXT",
    "TZ_HOUR",
    "DT_BAS_COMPLETE",
    "DT_EXT_COMPLETE",
    "DT_BAS_ORD_COMPLETE",
    "DT_EXT_ORD_COMPLETE",
    "DT_BAS_WEEK_COMPLETE",
    "DT_EXT_WEEK_COMPLETE",
    "D_DEFAULT",
    "D_WEEK",
    "D_ALT_EXT",
    "D_ALT_BAS",
    "D_ALT_BAS_ORD",
    "D_ALT_EXT_ORD",
]

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # <Python 3.7 and lower
    import importlib_metadata

# Append "2" for isodate2
__version__ = importlib_metadata.version(__name__ + "2")
