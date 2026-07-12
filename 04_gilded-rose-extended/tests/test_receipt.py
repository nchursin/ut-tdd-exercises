from datetime import datetime, timedelta

from freezegun import freeze_time


@freeze_time("2026-07-11")
def test_return_deadline_is_16_days_for_saturday(saturday_receipt):
    # receipt = regular_receipt(datetime.now())
    assert saturday_receipt.return_deadline == (
        datetime.now() + timedelta(days=16))


@freeze_time("2026-07-12")
def test_return_deadline_is_15_days_for_sunday(sunday_receipt):
    assert sunday_receipt.return_deadline == (
        datetime.now() + timedelta(days=15))


@freeze_time("2026-07-13 10:00")
def test_return_deadline_is_14_days_for_weekday(monday_morning_receipt):
    assert monday_morning_receipt.return_deadline == (
        datetime.now() + timedelta(days=14))


@freeze_time("2026-07-13 18:00")
def test_return_deadline_is_15_days_for_weekday_after_1800(monday_evening_receipt):
    assert monday_evening_receipt.return_deadline == (
        datetime.now() + timedelta(days=15))


@freeze_time("2026-07-11")
def test_status_is_can_be_returned_on_purchase_day(monday_morning_receipt):
    assert monday_morning_receipt.status == "can_be_returned"


def test_status_is_can_not_be_returned_on_16th_day(expired_monday_morning_receipt):
    assert expired_monday_morning_receipt.status == "cannot_be_returned"


def test_status_is_archived_on_31st_day_after_expiration(archived_monday_morning_receipt):
    assert archived_monday_morning_receipt.status == "archived"
