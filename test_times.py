from times import compute_overlap_time, time_range
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), 
                ('2010-01-12 10:38:00', '2010-01-12 10:45:00')] 
    
    assert result == expected

def test_no_overlap():
    range1 = time_range("2022-01-01 10:00:00", "2022-01-01 11:00:00")
    range2 = time_range("2022-01-01 12:00:00", "2022-01-01 13:00:00")

    result = compute_overlap_time(range1, range2)
    expected = []

    assert result == expected

def test_multiple_intervals():
    range1 = time_range("2022-01-01 10:00:00", "2022-01-01 12:00:00", 3)
    range2 = time_range("2022-01-01 11:00:00", "2022-01-01 13:00:00", 3)

    result = compute_overlap_time(range1, range2)
    expected = [
    ('2022-01-01 11:00:00', '2022-01-01 11:20:00'),
    ('2022-01-01 11:20:00', '2022-01-01 11:40:00'),
    ('2022-01-01 11:40:00', '2022-01-01 12:00:00')
    ]

    assert result == expected

def test_touching_intervals():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 11:00:00")]
    range2 = [("2010-01-12 11:00:00", "2010-01-12 12:00:00")]
    result = compute_overlap_time(range1, range2)
    expected = [("2010-01-12 11:00:00","2010-01-12 11:00:00")]
    assert result == expected