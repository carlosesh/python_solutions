import unittest

"""
Got Enough Money?

Create a function that returns any of the items you can afford in the store with
the money you have in your wallet. Sort the list in alphabetical order.

Examples
items_purchase({
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}, "$300") ➞ ["Bread", "Fertilizer", "Water"]

items_purchase({
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
  }, "$100") ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase({
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"},
"$1") ➞ "Nothing"

Notes
Return "Nothing" if you can't afford anything from the store.
"""


def items_purchase(store, wallet):
    affordable_items = [key for key, values in store.items()
                        if int(values[1:]) <= int(wallet[1:])]
    return "Nothing" if len(affordable_items) == 0 else sorted(affordable_items)


class GotEnoughMoney(unittest.TestCase):
    def test_items_purchase(self):
        self.assertEqual(items_purchase({"Water": "$1", "Bread": "$3", "TV": "$1000", "Fertilizer": "$20"}, "$300"), [
            "Bread", "Fertilizer", "Water"])
        self.assertEqual(items_purchase({"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4",
                                         "Pan": "$100", "Spoon": "$2"}, "$100"), ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"])
        self.assertEqual(items_purchase(
            {"Phone": "$999", "Speakers": "$300", "Laptop": "$5000", "PC": "$1200"}, "$1"), "Nothing")


if __name__ == '__main__':
    unittest.main()
