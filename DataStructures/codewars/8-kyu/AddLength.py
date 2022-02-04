"""
Add Length

What if we need the length of the words separated by a space to be added at the
end of that same word and have it returned as an array?

add_length('apple ban') => ["apple 5", "ban 3"]
add_length('you will win') => ["you 3", "will 4", "win 3"]
Your task is to write a function that takes a String and returns an Array/list
with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by
a space.

"""


def add_length(str):
    def format_result(item, num):
        return f"{item} {num}"

    return [format_result(x, len(x)) for x in str.split(' ')]


class AddLength(unittest.TestCase):
    def test_add_length(self):
        self.assertEqual(add_length('apple ban'), ["apple 5", "ban 3"])
        self.assertEqual(add_length('you will win'), [
            "you 3", "will 4", "win 3"])
        self.assertEqual(add_length('you'), ["you 3"])
        self.assertEqual(add_length('y'), ["y 1"])


if __name__ == '__main__':
    unittest.main()
