from datetime import datetime, timedelta

from freezegun import freeze_time

from gilded_rose import GildedRose


def test_update_receipt_to_cannot_be_returned(regular_testable_receipt):
    receipt = None
    with freeze_time(datetime.now() - timedelta(days=16)):
        receipt = regular_testable_receipt(datetime.now(), datetime.now())
        assert receipt.status == "can_be_returned"
    gilded_rose = GildedRose([], [receipt])
    gilded_rose.update_receipts()
    assert receipt.status == "cannot_be_returned"


def test_keep_can_be_returned_receipt_status(regular_testable_receipt):
    receipt = None
    with freeze_time(datetime.now() - timedelta(days=13)):
        receipt = regular_testable_receipt(datetime.now(), datetime.now())
        assert receipt.status == "can_be_returned"
    gilded_rose = GildedRose([], [receipt])
    gilded_rose.update_receipts()
    assert receipt.status == "can_be_returned"


def test_keep_cannot_be_returned_receipt_status(regular_testable_receipt):
    receipt = None
    with freeze_time(datetime.now() - timedelta(days=44)) as frozen_time:
        days_ago_44 = datetime.now()
        frozen_time.move_to(days_ago_44 + timedelta(days=43))
        yesterday = datetime.now()
        receipt = regular_testable_receipt(days_ago_44, yesterday)
        assert receipt.status == "cannot_be_returned"
    gilded_rose = GildedRose([], [receipt])
    gilded_rose.update_receipts()
    assert receipt.status == "cannot_be_returned"


def test_update_receipt_to_archived(regular_testable_receipt):
    receipt = None
    with freeze_time(datetime.now() - timedelta(days=45)) as frozen_time:
        days_ago_45 = datetime.now()
        frozen_time.move_to(days_ago_45 + timedelta(days=44))
        yesterday = datetime.now()
        receipt = regular_testable_receipt(days_ago_45, yesterday)
        assert receipt.status == "cannot_be_returned"
    gilded_rose = GildedRose([], [receipt])
    gilded_rose.update_receipts()
    assert receipt.status == "archived"
