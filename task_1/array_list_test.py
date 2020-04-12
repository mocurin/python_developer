import unittest
from task_1.array_list import ArrayList


class ArrayListTests(unittest.TestCase):
    # possible type checks on creation
    def test_creation(self):
        self.assertRaises(TypeError, ArrayList,
                          'b', [float(elem) for elem in range(-10, 10)])
        ArrayList('b', [*range(-10, 10)])
        self.assertRaises(TypeError, ArrayList,
                          'B', [*range(-10, 10)])
        ArrayList('B', [*range(0, 20)])
        self.assertRaises(TypeError, ArrayList,
                          'u', ['a' * i for i in range(1, 10)])
        ArrayList('u', [str(i) for i in range(0, 10)])
        self.assertRaises(TypeError, ArrayList,
                          'f', [*range(-10, 10)])
        ArrayList('f', [float(elem) for elem in range(-10, 10)])

    # indexing & co
    def test_get_set(self):
        a = ArrayList('B', [1, 2, 3])
        self.assertEqual(a[0], 1)
        self.assertEqual(a[1], 2)
        self.assertEqual(a[2], 3)
        a[0], a[1], a[2] = 3, 2, 1
        self.assertEqual(a[0], 3)
        self.assertEqual(a[1], 2)
        self.assertEqual(a[2], 1)
        self.assertRaises(TypeError, a.__setitem__, 0, 1.0)
        self.assertRaises(TypeError, a.__setitem__, 0, -1)
        self.assertRaises(TypeError, a.__setitem__, 0, '1')

    # pop, del, remove
    def test_deletion(self):
        a = ArrayList('b', [*range(0, 10)])
        f = a[0]
        del a[0]
        self.assertFalse(f in a)
        f = a.pop(-1)
        self.assertFalse(f in a)
        a.remove(5)
        self.assertFalse(5 in a)

    # insert, append, extend, op+=
    def test_insertion(self):
        a = ArrayList('B', [])
        a.insert(0, 1)
        a.insert(10, 2)
        a.insert(-1, 0)
        self.assertEqual(a.pop(-1), 2)
        self.assertEqual(a.pop(-1), 0)
        self.assertEqual(a.pop(-1), 1)
        a.append(10)
        self.assertEqual(a.pop(-1), 10)
        self.assertRaises(TypeError, a.append, -1)
        a.extend(ArrayList('B', [0, 1, 2]))
        self.assertEqual(a.pop(-1), 2)
        self.assertEqual(a.pop(-1), 1)
        self.assertEqual(a.pop(-1), 0)
        self.assertRaises(TypeError, a.extend, ArrayList('b', [0, 1, 2]))
        self.assertRaises(TypeError, a.extend, [0, 1, 2])
        a += ArrayList('B', [0, 1, 2])
        self.assertEqual(a.pop(-1), 2)
        self.assertEqual(a.pop(-1), 1)
        self.assertEqual(a.pop(-1), 0)

    # iteration, reversing, count
    def test_various(self):
        a = ArrayList('b', [i for i in range(5) for _ in range(i)])
        self.assertEqual(4, a.count(4))
        self.assertEqual(0, a.count(0))
        b = ArrayList('b', [*reversed(a)])
        a.reverse()
        for i, j in zip(a, b):
            self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()
