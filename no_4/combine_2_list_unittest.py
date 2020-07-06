import unittest
from combine_2_list import SortCombine

class TestNPrime(unittest.TestCase):
    def test_n_prime(self):
        sc = SortCombine()
        self.assertCountEqual(sc.sort_combine([], []),[])
        self.assertCountEqual(sc.sort_combine([4, 3, 6, 5, 1, 2], ["F", "C", "D", "B", "A"]),[[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"F"],[6,"NULL"]])
        self.assertCountEqual(sc.sort_combine([4, 3, 6, 5, 1, 2, 1000, 2000, 3000], ["F", "C", "D", "B", "A", "Q", "Z", "X", "C", "B"]),[[1, 'A'], [2, 'B'], [3, 'B'], [4, 'C'], [5, 'C'], [6, 'D'], [1000, 'F'], [2000, 'Q'], [3000, 'X'], ['NULL', 'Z']])


if __name__ == '__main__':
    unittest.main()