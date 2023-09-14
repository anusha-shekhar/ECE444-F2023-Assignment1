from utils import utils
import unittest

class test_utils(unittest.TestCase):

    def test_reversed_str(self):
        self.assertEqual(utils.reversed('123'), 321, "Reversed for string input incorrect")

    def test_reversed_float(self):
        self.assertEqual(utils.reversed(4.56), 6.54, "Reversed for float input incorrect")
    
    def test_reversed_int(self):
        self.assertEqual(utils.reversed(789), 987, "Reversed for int input incorrect")

    def test_formatter_str(self):
        self.assertEqual(utils.formatter('2'), (bin(2), oct(2)), "Formatter for string input incorrect")
    
    def test_formatter_float(self):
        self.assertEqual(utils.formatter(4.0), (bin(4), oct(4)), "Formatter for float input incorrect")
    
    def test_formatter_int(self):
        self.assertEqual(utils.formatter(8), (bin(8), oct(8)), "Formatter for int input incorrect")
    

if __name__ == '__main__':
    unittest.main()

# Test the reversed function with inputs that are strings, floats, and integers

# Integers
# self.assertEqual(utils.reversed(345), 543, "Reversed incorrect")


# Test the formatter function with inputs that are strings, floats, and integers

# Commit these changes



# Add screenshots for the commits into your README file on the main branch. Commit and push the changes.