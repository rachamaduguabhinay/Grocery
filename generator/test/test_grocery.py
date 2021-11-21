import os
import unittest
from generator.utils import testutils
from generator.grocery import Generator
from generator.utils import conutils


dirname = os.path.dirname(__file__)
csv_A_path = os.path.join(dirname, "data", "grocery", "dataset.csv")
csv_2level_path = os.path.join(dirname, "data", "grocery", "2levels.csv")
nested_json_patth = os.path.join(dirname, "data", "grocery", "nestedjson.json")
twolevel_nested_json = os.path.join(dirname, "data", "grocery", "2levelnestedjson.json")
csv_invaild_levels_data = os.path.join(dirname, "data", "grocery", "invalidlevel.csv")


class TestCSVUtils(unittest.TestCase):
    def test_populate_json_structure(self):
        actual_result_A = Generator(csv_A_path).convert()
        
        expected_result_A = testutils.parse_json_file(nested_json_patth)
        self.assertEqual(actual_result_A.as_dict(), expected_result_A)

    def test_populate_json_structure_with_2_levels(self):
        actual_result_A = Generator(csv_2level_path).convert()
        
        expected_result_A = testutils.parse_json_file(twolevel_nested_json)
        self.assertEqual(actual_result_A.as_dict(), expected_result_A)

    def test_invalid_level_data(self):
        with self.assertRaises(Exception):
            Generator(csv_invaild_levels_data).convert()


if __name__ == '__main__':
    unittest.main()