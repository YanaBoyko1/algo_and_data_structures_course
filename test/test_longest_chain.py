from src.longest_chain import longest_chain, process_file
from unittest import TestCase, main
import os


class TestProcessFile(TestCase):
    def test_process_file(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.input_file = os.path.join(current_directory, "..", "src", "wchain.in")
        self.output_file = os.path.join(current_directory, "..", "src", "wchain.out")
        process_file(self.input_file, self.output_file)

        with open(self.output_file, "r") as f:
            result = int(f.read().strip())

        self.assertEqual(result, 1)

    def test_example_1(self):
        words = [
            "crates",
            "car",
            "cats",
            "crate",
            "rate",
            "at",
            "ate",
            "tea",
            "rat",
            "a",
        ]
        expected_result = 6
        result = longest_chain(words)
        self.assertEqual(result, expected_result)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        expected_result = 4
        result = longest_chain(words)
        self.assertEqual(result, expected_result)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        expected_result = 1
        result = longest_chain(words)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
