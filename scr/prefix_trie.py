class Node:
    def __init__(self):
        self.children = {}
        self.is_last = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()

            node = node.children[letter]

        node.is_last = True

    def search(self, word):
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False

        return node.is_last

    def start_with(self, prefix):
        node = self.root

        for letter in prefix:
            if letter in node.children:
                node = node.children[letter]
            else:
                return False
        return True
