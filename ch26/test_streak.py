from streak import longest_streak


def test_empty_log():
    assert longest_streak([]) == 0


def test_gap_breaks_streak():
    assert longest_streak([1, 2, 3, 5, 6]) == 3


def test_same_day_counts_once():
    assert longest_streak([1, 1, 2, 2, 3]) == 3
