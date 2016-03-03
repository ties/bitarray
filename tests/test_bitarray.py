from unittest import TestCase

from bitarray import BitArray


class TestItemSetUnset(TestCase):
    def test_length(self):
        for l in range(2, 10):
            data = BitArray(2**l)

            self.assertEqual(len(data), 2**l)

    def test_set_to_true(self):
        data = BitArray(2**10)

        for x in range(len(data)):
            self.assertFalse(data[x])
            data[x] = True
            self.assertTrue(data[x])

    def test_to_false(self):
        data = BitArray(2**10, True)

        for x in range(len(data)):
            self.assertTrue(data[x])
            data[x] = False
            self.assertFalse(data[x])


class TestIteration(TestCase):
    def setUp(self):
        fib = [1, 1]

        # Fibonacci numbers under 2**10
        while (fib[-1] + fib[-2]) < 2**10:
            fib.append(fib[-1] + fib[-2])

        self.data = BitArray(2**10)
        self.fibs = fib

        for i in fib:
            self.data[i] = True

    def test_iterate(self):
        fib_set = set(self.fibs)

        for idx, i in enumerate(self.data):
            self.assertEqual(self.data[idx], idx in fib_set)
