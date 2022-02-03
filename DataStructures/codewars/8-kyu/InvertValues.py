import unittest
import random

"""
Invert values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```python
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

### Notes:
- All values are greater than `INT_MIN`
- The input should be modified, not returned.
- You can assume that all values are integers. Do not mutate the input array/list.
"""


def invert(lst):
    return [-x for x in lst]


class InverValues(unittest.TestCase):
    def test_inver(self):
        self.assertEqual(invert([1, 2, 3, 4, 5]), [-1, -2, -3, -4, -5])
        self.assertEqual(invert([1, -2, 3, -4, 5]), [-1, 2, -3, 4, -5])
        self.assertEqual(invert([]), [])
        self.assertEqual(invert([0]), [0])

    def test_random_input(self):
        for _ in range(500):
            lst = [random.randint(-1000, 1000)
                   for _ in range(random.randint(0, 1000))]
            expected = [-x for x in lst]
            self.assertEqual(invert(lst[:]), expected,
                             f'Testing for lst = {repr(lst)}')


if __name__ == '__main__':
    unittest.main()
