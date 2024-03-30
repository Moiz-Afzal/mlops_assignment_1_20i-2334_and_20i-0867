import unittest
from app import convert_timestamp_to_datetime


class TestConvertTimestampToDatetime(unittest.TestCase):

    def test_convert_timestamp_to_datetime(self):
        # Test with a sample timestamp in milliseconds
        timestamp_ms = 1617195600000
        expected_datetime = "2021-03-31 18:00:00"
        actual_datetime = convert_timestamp_to_datetime(timestamp_ms)

        # Convert actual datetime to string for comparison
        actual_datetime_str = actual_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Check
        self.assertEqual(actual_datetime_str, expected_datetime)

    def test_convert_timestamp_to_datetime(self):
        # Test with a sample timestamp in milliseconds
        timestamp_ms = 1617195600001
        expected_datetime = "2021-03-31 18:01:00"
        actual_datetime = convert_timestamp_to_datetime(timestamp_ms)

        # Convert actual datetime to string for comparison
        actual_datetime_str = actual_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Check
        self.assertEqual(actual_datetime_str, expected_datetime)

if __name__ == '__main__':
    unittest.main()
