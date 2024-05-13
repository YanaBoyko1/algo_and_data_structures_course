from unittest import TestCase, main
from src.red_black_priority_queue import RedBlackPriorityQueue

red = "red"
black = "black"


class TestRedBlackPriorityQueue(TestCase):
    def test_insert_and_search(self):
        rb_tree = RedBlackPriorityQueue()
        rb_tree.insert(5, 10)
        rb_tree.insert(3, 20)
        rb_tree.insert(7, 15)

        self.assertEqual(rb_tree.search(5, 10).key, 5)
        self.assertEqual(rb_tree.search(3, 20).key, 3)
        self.assertEqual(rb_tree.search(7, 15).key, 7)

        self.assertIsNone(rb_tree.search(10, 25))
        self.assertIsNone(rb_tree.search(1, 5))

    def test_delete(self):
        rb_tree = RedBlackPriorityQueue()
        rb_tree.insert(5, 10)
        rb_tree.insert(3, 20)
        rb_tree.insert(7, 15)
        rb_tree.insert(4, 25)

        rb_tree.delete(5, 10)
        self.assertIsNone(rb_tree.search(5, 10))

        rb_tree.delete(4, 25)
        self.assertIsNone(rb_tree.search(4, 25))

        result = rb_tree.delete(10, 30)
        self.assertEqual(result, "Key not found!")

    def test_transplant(self):
        rb_tree = RedBlackPriorityQueue()
        rb_tree.insert(5, 10)
        rb_tree.insert(3, 20)
        rb_tree.insert(7, 15)

        node_to_transplant = rb_tree.search(5, 10)
        replacement_node = rb_tree.search(3, 20)
        rb_tree.transplant(node_to_transplant, replacement_node)

        self.assertIsNone(rb_tree.search(5, 10))
        self.assertEqual(rb_tree.search(3, 20).key, 3)


if __name__ == "__main__":
    main()
