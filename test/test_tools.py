import unittest

from pycalculator.tools import *

class TestModuleTools(unittest.TestCase):
    """Unit test for the tools module functions."""

    def test_color(self):
        # check return string
        self.assertEqual(color('<r>ERROR: critical error.'),
                         '\x1b[31mERROR: critical error.\x1b[0m')
        self.assertEqual(color('<g><+>All checks passed!'),
                         '\x1b[32m\x1b[1mAll checks passed!\x1b[0m')


# Shell command to run the test:
# $ python -m unittest -v test.test_tools
if __name__ == '__main__':
    unittest.main()
