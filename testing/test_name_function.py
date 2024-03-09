import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    def test_first_last_name(self):
        """Do names like 'Rakesh Kumar' work?"""
        formatted_name = get_formatted_name('RAkesh', 'KUMAR')
        self.assertEqual(formatted_name, 'Rakesh Kumar')

if __name__ =='__main__':
    unittest.main()

# Assert method => matches a result to a function