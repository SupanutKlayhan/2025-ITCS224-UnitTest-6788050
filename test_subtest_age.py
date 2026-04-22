import unittest
from age import categorize_by_age


class TestIsChild(unittest.TestCase):
    def test_child_range_with_subtests(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                result = categorize_by_age(age)
                self.assertEqual(result, "Child")
                print(f"Age {age} is correctly categorized as Child.")

if __name__ == "__main__":
	unittest.main(verbosity=2)
