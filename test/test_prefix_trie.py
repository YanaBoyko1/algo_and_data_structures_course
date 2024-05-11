from unittest import TestCase, main
from src.prefix_trie import Trie


class TestTrie(TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("banana"))

    def test_start_with(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.start_with("app"))
        self.assertFalse(self.trie.start_with("ban"))


if __name__ == '__main__':
    main()
