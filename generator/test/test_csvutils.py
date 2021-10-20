import os
import unittest
from generator.utils import csvutils, testutils


dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "grocery", "dataset.csv")
data_rows_A_path = os.path.join(dirname, "data", "grocery", "datarows.csv")
csv_wrong_path= os.path.join(dirname, "data", "grocery", "data")

class TestCSVUtils(unittest.TestCase):
    def test_get_data_rows(self):
        actual_result_A = csvutils.CSVUtils(csv_A_path).get_data_rows()
        expected_result_A = testutils.parse_csv_file(data_rows_A_path)
        self.assertListEqual(actual_result_A, expected_result_A)
    
    def test_get_data_rows_exception(self):
        with self.assertRaises(FileNotFoundError):
            csvutils.CSVUtils(csv_wrong_path).get_data_rows()

if __name__ == '__main__':
    unittest.main()