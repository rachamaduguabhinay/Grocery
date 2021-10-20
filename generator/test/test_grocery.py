import os
import unittest
from generator.utils import testutils
from generator.grocery import Generator
from generator.utils import conutils


dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "grocery", "dataset.csv")
nested_json_patth = os.path.join(dirname, "data", "grocery", "nestedjson.json")


class TestCSVUtils(unittest.TestCase):
    def test_populate_json_structure(self):
        actual_result_A = Generator(csv_A_path).convert()
        
        expected_result_A = testutils.parse_json_file(nested_json_patth)
        self.assertEqual(actual_result_A.as_dict(), expected_result_A)

if __name__ == '__main__':
    unittest.main()