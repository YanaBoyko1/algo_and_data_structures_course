from unittest import TestCase, main
from src.max_binary_tree_diameter import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(TestCase):
    def test_binary_tree_diameter(self):
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        expected_diameter = 6

        diameter = binary_tree_diameter(root)

        self.assertEqual(diameter, expected_diameter)


if __name__ == "__main__":
    main()
