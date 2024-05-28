red = "red"
black = "black"


class Node:
    def __init__(self, key, priority, color=red):
        self.key = key
        self.priority = priority
        self.color = color
        self.p = None
        self.left = None
        self.right = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.nil = Node(None, None, color=black)
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.p = x

        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y

        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.p = x

        y.p = x.p

        if x.p is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x
        x.p = y

    def insert(self, key, priority):
        z = Node(key, priority)
        z.left = self.nil
        z.right = self.nil

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if z.priority > x.priority or z.priority == x.priority:
                x = x.left
            else:
                x = x.right

        z.p = y
        if y is None:
            self.root = z
        elif z.priority > y.priority or z.priority == y.priority:
            y.left = z
        else:
            y.right = z

        self.insert_fixup(z)

    def insert_fixup(self, z):
        while z.p and z.p.color == red:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == red:
                    z.p.color = black
                    y.color = black
                    z.p.p.color = red
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = black
                    z.p.p.color = red
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == red:
                    z.p.color = black
                    y.color = black
                    z.p.p.color = red
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = black
                    z.p.p.color = red
                    self.left_rotate(z.p.p)
            if z == self.root:
                break
        self.root.color = black

    def delete(self, k, priority):
        z = self.search(k, priority)

        if z is None:
            return "Key not found!"

        y = z
        y_orig_color = y.color

        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_orig_color = y.color
            x = y.right

            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        if y_orig_color == black:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == black:
            if x == x.p.left:
                w = x.p.right
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == black and w.right.color == black:
                    w.color = red
                    x = x.p
                else:
                    if w.right.color == black:
                        w.left.color = black
                        w.color = red
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = black
                    w.right.color = black
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == black and w.left.color == black:
                    w.color = red
                    x = x.p
                else:
                    if w.left.color == black:
                        w.right.color = black
                        w.color = red
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = black
                    w.left.color = black
                    self.right_rotate(x.p)
                    x = self.root
        x.color = black

    def transplant(self, u, v):
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def search(self, k, priority):
        x = self.root
        while x != self.nil and (priority != x.priority or k != x.key):
            if priority > x.priority or (priority == x.priority and k <= x.key):
                x = x.left
            else:
                x = x.right
        if x == self.nil:
            return None
        return x

    def print_tree(self, root, level=0, prefix=""):
        if root != self.nil:
            if root.right != self.nil:
                self.print_tree(root.right, level + 1, "┌───")
            print(
                " " * (level * 4) + prefix + f"{root.key}({root.priority}){root.color}"
            )
            if root.left != self.nil:
                self.print_tree(root.left, level + 1, "└───")
