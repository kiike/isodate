"""
Tests to parse an ISO datetime string into a datetime object.
"""
import pickle

import isodate


def test_pickle_datetime():
    """
    Parse an ISO datetime string and compare it to the expected value.
    """
    dti = isodate.parse_datetime("2012-10-26T09:33+00:00")
    for proto in range(0, pickle.HIGHEST_PROTOCOL + 1):
        pikl = pickle.dumps(dti, proto)
        assert dti == pickle.loads(pikl), f"pickle proto {proto} failed"


def test_pickle_duration():
    """
    Pickle / unpickle duration objects.
    """
    from isodate.duration import Duration

    dur = Duration()
    failed = []
    for proto in range(0, pickle.HIGHEST_PROTOCOL + 1):
        try:
            pikl = pickle.dumps(dur, proto)
            if dur != pickle.loads(pikl):
                raise Exception("not equal")
        except Exception as e:
            failed.append(f"pickle proto {proto} failed ({repr(e)})")
    assert len(failed) == 0, f"pickle protos failed: {failed}"


def test_pickle_utc():
    """
    isodate.UTC objects remain the same after pickling.
    """
    assert isodate.UTC is pickle.loads(pickle.dumps(isodate.UTC))
