from functools import reduce
import random
import unittest

import mean_median as m

class TestMeanMedian(unittest.TestCase):
    def test_simple(self):
        """Tests a simple case, happy path"""
        test = [22, 38, 75, 86, 97]
        with self.subTest():
            actual_mean = m.mean(test)
            self.assertEqual(63, actual_mean)
        with self.subTest():
            actual_median = m.median(test)
            self.assertEqual(75, actual_median) 

    def test_enormous(self):
        """Tests a massive sample size"""
        test = []
        for x in range(36234):
            test.append(random.randint(0,100))
        test.sort()

        with self.subTest():
            expected = int(reduce(lambda a, b: a + b, test) / len(test))
            actual = m.mean(test)
            self.assertEqual(expected, actual)
        with self.subTest():
            half = len(test) // 2
            expected = (test[half] + test[half - 1]) / 2
            actual = m.median(test)
            self.assertEqual(expected, actual)

    def test_some_invalid(self):
        """Tests discarding of invalid values."""
        test = [-12, 23, 46, 68, 89, 90, 123, 158]
        with self.subTest():
            actual = m.mean(test)
            self.assertEqual(63, actual)
        with self.subTest():
            actual = m.median(test)
            self.assertEqual(68, actual)

    def test_all_invalid(self):
        """Tests scenario with all invalid test scores."""
        test = [-12, -8, -1, 101, 104, 193]
        with self.subTest():
            actual = m.mean(test)
            self.assertEqual(-1, actual)
        with self.subTest():
            actual = m.median(test)
            self.assertEqual(-1, actual)

if __name__ == '__main__':
    unittest.main()
