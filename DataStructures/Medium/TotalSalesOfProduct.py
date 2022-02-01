import unittest

"""
Total Sales of Product

In this question you will be given a table as below, where the first row lists
the names of products, and each of row after that lists the sales of the product
for each day (over some time range).

[
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
]
Write a function that receives:

A sales table sales_table as shown above.
The name of a product product.
... and returns the total sales if the product is on the list, otherwise return
the string "Product not found".

Examples
total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "A") ➞ 9

# 2 + 3 + 4 = 9


total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "C") ➞ 12

# 1 + 6 + 5 = 12


total_sales([
  ["A", "B", "C"],
  [ 2 ,  7 ,  1 ],
  [ 3 ,  6 ,  6 ],
  [ 4 ,  5 ,  5 ]
], "D") ➞ "Product not found"

Notes
The examples above all use the same sales table, but in the tests the table will
vary.
"""


def total_sales(sales_table, product):
    try:
        index_of_product = sales_table[0].index(product)
        total = 0
        for row in range(len(sales_table)):
            for column in range(len(sales_table[row])):
                if(column == index_of_product):
                    value = sales_table[row][column]
                    total += value if value is not product else 0

        return total
    except ValueError:
        return 'Product not found'


class TotalSalesOfProduct(unittest.TestCase):
    def test_total_sales(self):
        table1 = [
            ['A', 'B', 'C'],
            [2,  7,  1],
            [3,  6,  6],
            [4,  5,  5]]

        table2 = [
            ['W', 'X', 'Y', 'Z'],
            [3,  5,  7,  1],
            [4,  5,  2,  3]]

        table3 = [
            ['R', 'T', 'V', 'W', 'C'],
            [2,  3,  7,  7,  4],
            [8,  5,  2,  9,  0],
            [2,  5,  8,  7,  4],
            [5,  3,  7,  2,  3]]

        self.assertEqual(total_sales(table1, 'A'), 9)
        self.assertEqual(total_sales(table1, 'B'), 18)
        self.assertEqual(total_sales(table1, 'C'), 12)
        self.assertEqual(total_sales(table1, 'D'), 'Product not found')

        self.assertEqual(total_sales(table2, 'A'), 'Product not found')
        self.assertEqual(total_sales(table2, 'W'), 7)
        self.assertEqual(total_sales(table2, 'Y'), 9)
        self.assertEqual(total_sales(table2, 'Z'), 4)

        self.assertEqual(total_sales(table3, 'A'), 'Product not found')
        self.assertEqual(total_sales(table3, 'T'), 16)
        self.assertEqual(total_sales(table3, 'Y'), 'Product not found')
        self.assertEqual(total_sales(table3, 'W'), 25)


if __name__ == '__main__':
    unittest.main()
