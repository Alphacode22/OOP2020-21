# import python_testing
import unittest
from python_testing import TypesAndStrings

class MyFirstTest(unittest.TestCase):

    def setUp(self):
        self.ts = TypesAndStrings()
        self.value = ['h']

    def test_last_char(self):
        result = self.ts.last_char(self.value[0])
        self.assertEqual(result, self.value[-1])

    def test_first_char(self):
        result = self.ts.first_char(self.value[0])
        self.assertEqual(result, self.value[0])

    def test_replace_all_a(self):
        result = self.ts.replace_all_a(self.value[0])
        self.assertEqual(result, self.value[0])

    def test_lower(self):
        result = self.ts.all_lower(self.value[0])
        self.assertEqual(result, self.value[0].lower())


if __name__ == '__main__':
    unittest.main()

