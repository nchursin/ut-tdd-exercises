from datetime import datetime, timedelta

from freezegun import freeze_time


@freeze_time("2026-07-11")
def test_return_deadline_is_16_days_for_saturday(regular_receipt):
    receipt = regular_receipt(datetime.now())
    assert receipt.return_deadline == (datetime.now() + timedelta(days=16))


@freeze_time("2026-07-12")
def test_return_deadline_is_15_days_for_sunday(regular_receipt):
    receipt = regular_receipt(datetime.now())
    assert receipt.return_deadline == (datetime.now() + timedelta(days=15))


@freeze_time("2026-07-13 10:00")
def test_return_deadline_is_14_days_for_weekday(regular_receipt):
    receipt = regular_receipt(datetime.now())
    assert receipt.return_deadline == (datetime.now() + timedelta(days=14))


@freeze_time("2026-07-13 18:00")
def test_return_deadline_is_15_days_for_weekday_after_1800(regular_receipt):
    receipt = regular_receipt(datetime.now())
    assert receipt.return_deadline == (datetime.now() + timedelta(days=15))


@freeze_time("2026-07-11")
def test_status_is_can_be_returned_on_purchase_day(regular_receipt):
    receipt = regular_receipt(datetime.now())
    assert receipt.status == "can_be_returned"
