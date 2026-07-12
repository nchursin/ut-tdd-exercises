from datetime import datetime, timedelta

from freezegun import freeze_time
from pytest import fixture

from gilded_rose import Item, Receipt
from tests.testable_receipt import TestableReceipt


@fixture
def regular_item():
    return Item("Regular item", 50, 50)


@fixture
def regular_receipt(regular_item):
    return lambda purchase_date: Receipt(regular_item, "Thrall", purchase_date)


@fixture
@freeze_time("2026-07-11")
def saturday_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-12")
def sunday_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 10:00")
def monday_morning_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 18:00")
def monday_evening_receipt(regular_item):
    return Receipt(regular_item, "Thrall", datetime.now())


@fixture
@freeze_time("2026-07-13 10:00")
def expired_monday_morning_receipt(regular_item, monday_morning_receipt):
    return TestableReceipt(
        monday_morning_receipt.return_deadline + timedelta(days=1),
        regular_item,
        monday_morning_receipt.customer_name,
        monday_morning_receipt.purchase_datetime,
    )


@fixture
@freeze_time("2026-07-13 10:00")
def archived_monday_morning_receipt(regular_item, monday_morning_receipt):
    return TestableReceipt(
        monday_morning_receipt.return_deadline + timedelta(days=31),
        regular_item,
        monday_morning_receipt.customer_name,
        monday_morning_receipt.purchase_datetime,
    )
