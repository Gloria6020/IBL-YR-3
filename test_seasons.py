from datetime import date, timedelta
from seasons import age_in_minutes

def test_age_in_minutes():
    # Test with a birthdate in the past
    birthdate = date(1990, 1, 1)
    assert age_in_minutes(birthdate) == "1,576,800 minutes"

    # Test with a birthdate that is today
    today = date.today()
    assert age_in_minutes(today) == "0 minutes"

    # Test with a future birthdate
    future_birthdate = date.today() + timedelta(days=365)
    assert age_in_minutes(future_birthdate) == "0 minutes"

