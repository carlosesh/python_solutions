import unittest

"""
Filtering by Star Rating
Given a dictionary of some items with star ratings and a specified star rating,
return a new dictionary of items which match the specified star rating.
Return "No results found" if no item matches the star rating given.

Examples
filter_by_rating({
  "Luxury Chocolates" : "*****",
  "Tasty Chocolates" : "****",
  "Aunty May Chocolates" : "*****",
  "Generic Chocolates" : "***"
}, "*****") ➞ {
  "Luxury Chocolates" : "*****",
  "Aunty May Chocolates" : "*****"
}

filter_by_rating({
  "Continental Hotel" : "****",
  "Big Street Hotel" : "**",
  "Corner Hotel" : "**",
  "Trashviews Hotel" : "*",
  "Hazbins" : "*****"
}, "*") ➞ {
  "Trashviews Hotel" : "*"
}

filter_by_rating({
  "Solo Restaurant" : "***",
  "Finest Dinings" : "*****",
  "Burger Stand" : "***"
}, "****") ➞ "No results found"
"""


def filter_by_rating(d, rating):
    filtered_results = {k: v for k, v in d.items() if v == rating}
    return filtered_results if bool(filtered_results) else "No results found"


class FilteringByStarRating(unittest.TestCase):
    def test_filter_by_rating(self):
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "*", "Brand D": "**", "Brand E": "****", "Brand F": "*****", "Brand G": "****", "Brand H": "****", "Brand I": "*****",
                         "Brand K": "***", "Brand L": "*****", "Brand M": "***", "Brand N": "*", "Brand O": "***", "Brand P": "*****", "Brand Q": "**", "Brand R": "****"}, "***"), {"Brand K": "***", "Brand M": "***", "Brand O": "***"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "***", "Brand C": "**", "Brand D": "*****", "Brand E": "*", "Brand F": "****", "Brand G": "*****", "Brand H": "*****", "Brand I": "**", "Brand K": "*", "Brand L": "*", "Brand M": "***", "Brand N": "*", "Brand O": "*",
                         "Brand P": "**", "Brand Q": "**", "Brand R": "****", "Brand S": "****", "Brand T": "**", "Brand U": "*", "Brand V": "*", "Brand W": "*", "Brand X": "***", "Brand Y": "*****", "Brand Z": "****"}, "**"), {"Brand C": "**", "Brand I": "**", "Brand P": "**", "Brand Q": "**", "Brand T": "**"})
        self.assertEqual(filter_by_rating({"Brand A": "***", "Brand B": "**", "Brand C": "****", "Brand D": "*", "Brand E": "*", "Brand F": "**", "Brand G": "***",
                         "Brand H": "*", "Brand I": "**", "Brand K": "*****", "Brand L": "**", "Brand M": "*"}, "**"), {"Brand B": "**", "Brand F": "**", "Brand I": "**", "Brand L": "**"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "***", "Brand C": "***", "Brand D": "***", "Brand E": "*", "Brand F": "**", "Brand G": "***", "Brand H": "*****", "Brand I": "**", "Brand K": "***", "Brand L": "*", "Brand M": "****", "Brand N": "****", "Brand O": "***",
                         "Brand P": "**", "Brand Q": "*****", "Brand R": "*", "Brand S": "*", "Brand T": "*****", "Brand U": "*****", "Brand V": "*", "Brand W": "*****", "Brand X": "****", "Brand Y": "*", "Brand Z": "*****"}, "****"), {"Brand M": "****", "Brand N": "****", "Brand X": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "****", "Brand C": "*****", "Brand D": "*", "Brand E": "**", "Brand F": "***", "Brand G": "*",
                         "Brand H": "**", "Brand I": "*", "Brand K": "**", "Brand L": "****"}, "*"), {"Brand A": "*", "Brand D": "*", "Brand G": "*", "Brand I": "*"})
        self.assertEqual(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "**", "Brand D": "*", "Brand E": "**", "Brand F": "***", "Brand G": "***", "Brand H": "**", "Brand I": "*", "Brand K": "*",
                         "Brand L": "****", "Brand M": "*", "Brand N": "*****", "Brand O": "**", "Brand P": "*", "Brand Q": "*****", "Brand R": "*"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand L": "****"})
        self.assertEqual(filter_by_rating(
            {"Brand A": "**", "Brand B": "*", "Brand C": "*"}, "**"), {"Brand A": "**"})
        self.assertEqual(filter_by_rating(
            {"Brand A": "****", "Brand B": "*", "Brand C": "****", "Brand D": "***", "Brand E": "*****"}, "**"), "No results found")
        self.assertEqual(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "***", "Brand D": "****", "Brand E": "*****", "Brand F": "*", "Brand G": "****", "Brand H": "*****", "Brand I": "*", "Brand K": "****", "Brand L": "****", "Brand M": "*", "Brand N": "***", "Brand O": "**", "Brand P": "*", "Brand Q": "*", "Brand R": "****",
                         "Brand S": "*****", "Brand T": "****", "Brand U": "*****", "Brand V": "****", "Brand W": "****", "Brand X": "**", "Brand Y": "*"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand D": "****", "Brand G": "****", "Brand K": "****", "Brand L": "****", "Brand R": "****", "Brand T": "****", "Brand V": "****", "Brand W": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "**", "Brand B": "****", "Brand C": "***", "Brand D": "****", "Brand E": "*", "Brand F": "*", "Brand G": "**", "Brand H": "***", "Brand I": "***", "Brand K": "**", "Brand L": "***", "Brand M": "**", "Brand N": "**", "Brand O": "*", "Brand P": "*",
                         "Brand Q": "*****", "Brand R": "***", "Brand S": "**", "Brand T": "*", "Brand U": "**", "Brand V": "*", "Brand W": "**", "Brand X": "****"}, "**"), {"Brand A": "**", "Brand G": "**", "Brand K": "**", "Brand M": "**", "Brand N": "**", "Brand S": "**", "Brand U": "**", "Brand W": "**"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "**", "Brand C": "****", "Brand D": "*****", "Brand E": "*****", "Brand F": "*****", "Brand G": "****", "Brand H": "*", "Brand I": "*", "Brand K": "*", "Brand L": "****",
                         "Brand M": "*", "Brand N": "***", "Brand O": "****", "Brand P": "****", "Brand Q": "****", "Brand R": "****", "Brand S": "**", "Brand T": "****"}, "*"), {"Brand A": "*", "Brand H": "*", "Brand I": "*", "Brand K": "*", "Brand M": "*"})
        self.assertEqual(filter_by_rating({"Brand A": "**", "Brand B": "*", "Brand C": "*****",
                         "Brand D": "*****"}, "*****"), {"Brand C": "*****", "Brand D": "*****"})
        self.assertEqual(filter_by_rating({"Brand A": "*****", "Brand B": "***", "Brand C": "***", "Brand D": "***", "Brand E": "***", "Brand F": "***", "Brand G": "****", "Brand H": "*", "Brand I": "**", "Brand K": "***", "Brand L": "****", "Brand M": "*", "Brand N": "*****", "Brand O": "**",
                         "Brand P": "*", "Brand Q": "****", "Brand R": "**", "Brand S": "****", "Brand T": "*", "Brand U": "*****", "Brand V": "**", "Brand W": "*", "Brand X": "**", "Brand Y": "*****"}, "****"), {"Brand G": "****", "Brand L": "****", "Brand Q": "****", "Brand S": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "*****", "Brand D": "*", "Brand E": "****", "Brand F": "*", "Brand G": "****", "Brand H": "*****", "Brand I": "***", "Brand K": "***",
                         "Brand L": "***", "Brand M": "*", "Brand N": "****", "Brand O": "****", "Brand P": "**", "Brand Q": "*****", "Brand R": "***"}, "****"), {"Brand E": "****", "Brand G": "****", "Brand N": "****", "Brand O": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "***", "Brand B": "****", "Brand C": "****", "Brand D": "*", "Brand E": "**", "Brand F": "****",
                         "Brand G": "*****", "Brand H": "****", "Brand I": "*"}, "****"), {"Brand B": "****", "Brand C": "****", "Brand F": "****", "Brand H": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "*****", "Brand C": "**", "Brand D": "*****", "Brand E": "**", "Brand F": "*",
                         "Brand G": "**", "Brand H": "***", "Brand I": "***", "Brand K": "*****"}, "*****"), {"Brand B": "*****", "Brand D": "*****", "Brand K": "*****"})
        self.assertEqual(filter_by_rating({"Brand A": "****", "Brand B": "****", "Brand C": "*****", "Brand D": "*****", "Brand E": "****", "Brand F": "***", "Brand G": "**", "Brand H": "**", "Brand I": "****", "Brand K": "****",
                         "Brand L": "****", "Brand M": "****", "Brand N": "***", "Brand O": "**"}, "****"), {"Brand A": "****", "Brand B": "****", "Brand E": "****", "Brand I": "****", "Brand K": "****", "Brand L": "****", "Brand M": "****"})
        self.assertEqual(filter_by_rating(
            {"Brand A": "***", "Brand B": "***"}, "*****"), "No results found")
        self.assertEqual(filter_by_rating({"Brand A": "***", "Brand B": "*****", "Brand C": "*", "Brand D": "****", "Brand E": "*", "Brand F": "**", "Brand G": "**", "Brand H": "*****",
                         "Brand I": "**", "Brand K": "****", "Brand L": "**", "Brand M": "**", "Brand N": "****", "Brand O": "****", "Brand P": "*****"}, "***"), {"Brand A": "***"})
        self.assertEqual(filter_by_rating({"Brand A": "**", "Brand B": "*", "Brand C": "*****", "Brand D": "*****", "Brand E": "*", "Brand F": "***", "Brand G": "*", "Brand H": "**",
                         "Brand I": "*", "Brand K": "**", "Brand L": "*", "Brand M": "***", "Brand N": "*****", "Brand O": "*"}, "*****"), {"Brand C": "*****", "Brand D": "*****", "Brand N": "*****"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "*", "Brand C": "*", "Brand D": "***", "Brand E": "****", "Brand F": "***", "Brand G": "*****", "Brand H": "**", "Brand I": "*", "Brand K": "*****", "Brand L": "***", "Brand M": "***", "Brand N": "***", "Brand O": "**", "Brand P": "**",
                         "Brand Q": "*****", "Brand R": "****", "Brand S": "***", "Brand T": "****", "Brand U": "*****", "Brand V": "***", "Brand W": "*****", "Brand X": "*****", "Brand Y": "***"}, "*****"), {"Brand G": "*****", "Brand K": "*****", "Brand Q": "*****", "Brand U": "*****", "Brand W": "*****", "Brand X": "*****"})
        self.assertEqual(filter_by_rating({"Brand A": "*****", "Brand B": "****", "Brand C": "****", "Brand D": "*", "Brand E": "*", "Brand F": "****", "Brand G": "****", "Brand H": "**", "Brand I": "****", "Brand K": "****", "Brand L": "*****", "Brand M": "*****", "Brand N": "***", "Brand O": "****", "Brand P": "**",
                         "Brand Q": "***", "Brand R": "***", "Brand S": "*****", "Brand T": "*", "Brand U": "*****", "Brand V": "****", "Brand W": "***"}, "****"), {"Brand B": "****", "Brand C": "****", "Brand F": "****", "Brand G": "****", "Brand I": "****", "Brand K": "****", "Brand O": "****", "Brand V": "****"})
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "****", "Brand C": "*", "Brand D": "*****", "Brand E": "**", "Brand F": "****", "Brand G": "***", "Brand H": "****", "Brand I": "*", "Brand K": "*", "Brand L": "*****", "Brand M": "*****", "Brand N": "*",
                         "Brand O": "**", "Brand P": "*****", "Brand Q": "**", "Brand R": "*****", "Brand S": "*****", "Brand T": "****", "Brand U": "*****", "Brand V": "*****", "Brand W": "**", "Brand X": "***"}, "**"), {"Brand E": "**", "Brand O": "**", "Brand Q": "**", "Brand W": "**"})
        self.assertEqual(filter_by_rating({"Brand A": "**", "Brand B": "**", "Brand C": "**",
                         "Brand D": "***", "Brand E": "*****", "Brand F": "**"}, "****"), "No results found")
        self.assertEqual(filter_by_rating({"Brand A": "*", "Brand B": "*", "Brand C": "**", "Brand D": "*", "Brand E": "****", "Brand F": "****", "Brand G": "**", "Brand H": "*", "Brand I": "***", "Brand K": "**", "Brand L": "***", "Brand M": "***", "Brand N": "****", "Brand O": "*",
                         "Brand P": "*****", "Brand Q": "*****", "Brand R": "*", "Brand S": "****", "Brand T": "****", "Brand U": "*", "Brand V": "**", "Brand W": "****", "Brand X": "****", "Brand Y": "****", "Brand Z": "**"}, "***"), {"Brand I": "***", "Brand L": "***", "Brand M": "***"})
        self.assertEqual(filter_by_rating({"Brand A": "**", "Brand B": "*****", "Brand C": "***", "Brand D": "**", "Brand E": "*", "Brand F": "****", "Brand G": "****", "Brand H": "*",
                         "Brand I": "*", "Brand K": "*", "Brand L": "****", "Brand M": "*", "Brand N": "**", "Brand O": "*", "Brand P": "**", "Brand Q": "*"}, "*****"), {"Brand B": "*****"})
        self.assertEqual(filter_by_rating({"Brand A": "****", "Brand B": "*****", "Brand C": "*****", "Brand D": "****", "Brand E": "**", "Brand F": "*", "Brand G": "**", "Brand H": "**", "Brand I": "***", "Brand K": "***", "Brand L": "***", "Brand M": "***", "Brand N": "****",
                         "Brand O": "*****", "Brand P": "*", "Brand Q": "*", "Brand R": "****", "Brand S": "**", "Brand T": "**", "Brand U": "*****", "Brand V": "***", "Brand W": "***"}, "**"), {"Brand E": "**", "Brand G": "**", "Brand H": "**", "Brand S": "**", "Brand T": "**"})


if __name__ == '__main__':
    unittest.main()
