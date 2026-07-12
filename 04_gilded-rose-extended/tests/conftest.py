from pytest import fixture

from gilded_rose import Receipt, Item


@fixture
def regular_receipt():
    return lambda purchase_date: Receipt(Item("Regular item", 50, 50), "Thrall", purchase_date)
