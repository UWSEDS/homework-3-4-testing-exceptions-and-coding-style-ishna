"""
Unit Testing.
"""
import unittest
from dataframe import test_create_dataframe
from dataframe import read_data

# Testing for column data types
DATA = read_data()
CONVERT_DICT = {'mpg': int}
NEW_DATA1 = DATA.astype(CONVERT_DICT)

# Example test function, can be run independently


def test_column_data_type(data_frame):
    """code for unit test to be run manually"""
    result = test_create_dataframe(data_frame, DATA)
    if result:
        print("Worked! column data types are equal")
    else:
        print("Sorry, the column name types are not equal according")
    return result
# test_column_data_type(NEW_DATA1)

# To test data rows, if they are enough
DATA = read_data()
NEW_DATA2 = DATA.iloc[0]
# Example Function to be run independently


def test_data_rows(data_frame):
    """code for unit test to be run manually"""
    result = test_create_dataframe(data_frame, DATA)
    if result:
        print("Worked! rows number are enough")
    else:
        print("Sorry, the rows are not enough according to unit test")
    return result


class MyTest(unittest.TestCase):
    """code for unit test"""
    def test1(self):
        """column data type test"""
        self.assertEqual(test_create_dataframe(NEW_DATA1, DATA), False)

    def test2(self):
        """row test"""
        self.assertEqual(test_create_dataframe(NEW_DATA2, DATA), False)

if __name__ == '__main__':
    """calling main"""
    unittest.main()
