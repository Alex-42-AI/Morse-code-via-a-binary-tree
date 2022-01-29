class BinNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __eq__(self, other):
        if isinstance(other, BinNode):
            return self.value == other.value and self.left == other.left and self.right == other.right
        return False
    def __str__(self):
        return '(' + str(self.value) + ')'
    def __repr__(self):
        return str(self)
class BinTree:
    def __init__(self, root):
        self.root = BinNode(root)
    def copy(self, curr_from, curr_to):
        if curr_from is None:
            return
        if curr_from.left is not None:
            curr_to.left = curr_from.left
            self.copy(curr_from.left, curr_to.left)
        if curr_from.right is not None:
            curr_to.right = curr_from.right
            self.copy(curr_from.right, curr_to.right)
    def left(self):
        if self.root.left is not None:
            res = BinTree(self.root.left.value)
            self.copy(self.root.left, res.root)
            return res
        return BinTree(False)
    def right(self):
        if self.root.right is not None:
            res = BinTree(self.root.right.value)
            self.copy(self.root.right, res.root)
            return res
        return BinTree(False)
    def get_height_recursive(self, curr_node=''):
        if curr_node == '':
            curr_node = self.root
        if curr_node.left is None and curr_node.right is None:
            return 0
        left, right = 0, 0
        if curr_node.left is not None:
            left = self.get_height_recursive(curr_node.left)
        if curr_node.right is not None:
            right = self.get_height_recursive(curr_node.right)
        return 1 + max(left, right)
    def get_height(self):
        Last_Node = self.root
        while Last_Node.right is not None:
            Last_Node = Last_Node.right
        node = self.root
        current, Max = 0, 0
        so_far, chain = [], [node]
        while True:
            if node.left not in so_far:
                node = node.left
                chain.append(node)
                current += 1
            elif node.right not in so_far:
                node = node.right
                chain.append(node)
                current += 1
            else:
                Max = max(Max, current)
                if node == Last_Node:
                    break
                current -= 1
                node = chain[chain.index(node) - 1]
                so_far.append(chain.pop())
        return Max
    def count_leaves(self, curr_node=''):
        if curr_node == '':
            curr_node = self.root
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return 1
        return self.count_leaves(curr_node.left) + self.count_leaves(curr_node.right)
    def count_nodes(self, curr_node=''):
        if curr_node == '':
            curr_node = self.root
        if curr_node is None:
            return 0
        return (curr_node.value is not None) + self.count_nodes(curr_node.left) + self.count_nodes(curr_node.right)
    def path_to(self, n: BinNode, tree=None):
        if tree is None:
            tree = self
        if tree.root.value is False:
            return
        if tree.root.left is not None:
            if tree.root.left.value == n.value:
                return '.'
        res = self.path_to(n, tree.left())
        if res:
            return '. ' + res
        if tree.root.right is not None:
            if tree.root.right.value == n.value:
                return
        res = self.path_to(n, tree.right())
        if res:
            return '- ' + res
    def invert(self, node=''):
        if node == '':
            node = self.root
        if node is None:
            return
        self.invert(node.left)
        self.invert(node.right)
        node.left, node.right = node.right, node.left
    def __preorder_print(self, start, traversal):
        if start:
            traversal += [str(start)]
            traversal = self.__preorder_print(start.left, traversal)
            traversal = self.__preorder_print(start.right, traversal)
        return traversal
    def __in_order_print(self, start, traversal):
        if start:
            traversal = self.__in_order_print(start.left, traversal)
            traversal += [str(start)]
            traversal = self.__in_order_print(start.right, traversal)
        return traversal
    def __post_order_print(self, start, traversal):
        if start:
            traversal = self.__post_order_print(start.left, traversal)
            traversal = self.__post_order_print(start.right, traversal)
            traversal += [str(start)]
        return traversal
    def print(self, traversal_type):
        if traversal_type.lower() == 'preorder':
            print(self.__preorder_print(self.root, []))
        elif traversal_type.lower() == 'in-order':
            print(self.__in_order_print(self.root, []))
        elif traversal_type.lower() == 'post-order':
            print(self.__post_order_print(self.root, []))
        else:
            print('Traversal type ' + str(traversal_type) + ' is not supported!')
MorseCode = BinTree('')
MorseCode.root.left = BinNode('e')
MorseCode.root.left.left = BinNode('i')
MorseCode.root.left.left.left = BinNode('s')
MorseCode.root.left.left.left.left = BinNode('h')
MorseCode.root.left.left.left.left.left = BinNode('4')
MorseCode.root.left.left.left.left.right = BinNode('5')
MorseCode.root.left.left.left.right = BinNode('v')
MorseCode.root.left.left.left.right.right = BinNode('3')
MorseCode.root.left.left.right = BinNode('u')
MorseCode.root.left.left.right.left = BinNode('f')
MorseCode.root.left.left.right.right = BinNode(None)
MorseCode.root.left.left.right.right.left = BinNode(None)
MorseCode.root.left.left.right.right.left.left = BinNode('?')
MorseCode.root.left.left.right.right.right = BinNode('2')
MorseCode.root.left.right = BinNode('a')
MorseCode.root.left.right.left = BinNode('r')
MorseCode.root.left.right.left.right = BinNode(None)
MorseCode.root.left.right.left.right.left = BinNode('+')
MorseCode.root.left.right.left.right.left.right = BinNode('.')
MorseCode.root.left.right.left.left = BinNode('l')
MorseCode.root.left.right.left.left.left = BinNode('&')
MorseCode.root.left.right.left.left.right = BinNode(None)
MorseCode.root.left.right.left.left.right.left = BinNode('"')
MorseCode.root.left.right.right = BinNode('w')
MorseCode.root.left.right.right.left = BinNode('p')
MorseCode.root.left.right.right.left.right = BinNode(None)
MorseCode.root.left.right.right.left.right.left = BinNode('@')
MorseCode.root.left.right.right.right = BinNode('j')
MorseCode.root.left.right.right.right.left = BinNode('\'')
MorseCode.root.left.right.right.right.right = BinNode('1')
MorseCode.root.right = BinNode('t')
MorseCode.root.right.left = BinNode('n')
MorseCode.root.right.left.left = BinNode('d')
MorseCode.root.right.left.left.left = BinNode('b')
MorseCode.root.right.left.left.left.left = BinNode('6')
MorseCode.root.right.left.left.left.left.right = BinNode('-')
MorseCode.root.right.left.left.left.right = BinNode('=')
MorseCode.root.right.left.left.right = BinNode('x')
MorseCode.root.right.left.left.right.left = BinNode('/')
MorseCode.root.right.left.right = BinNode('k')
MorseCode.root.right.left.right.left = BinNode('c')
MorseCode.root.right.left.right.left.right = BinNode(None)
MorseCode.root.right.left.right.left.right.right = BinNode('!')
MorseCode.root.right.left.right.right = BinNode('y')
MorseCode.root.right.left.right.right.left = BinNode('(')
MorseCode.root.right.left.right.right.left.right = BinNode(')')
MorseCode.root.right.right = BinNode('m')
MorseCode.root.right.right.left = BinNode('g')
MorseCode.root.right.right.left.left = BinNode('z')
MorseCode.root.right.right.left.left.right = BinNode(None)
MorseCode.root.right.right.left.left.right.right = BinNode(',')
MorseCode.root.right.right.left.left.left = BinNode('7')
MorseCode.root.right.right.left.right = BinNode('q')
MorseCode.root.right.right.right = BinNode('o')
MorseCode.root.right.right.right.left = BinNode(None)
MorseCode.root.right.right.right.left.left = BinNode('8')
MorseCode.root.right.right.right.left.left.left = BinNode(':')
MorseCode.root.right.right.right.right = BinNode(None)
MorseCode.root.right.right.right.right.left = BinNode('9')
MorseCode.root.right.right.right.right.right = BinNode('0')
MorseCode.print('in-order')  # ['(4)', '(h)', '(5)', '(s)', '(v)', '(3)', '(i)', '(f)', '(u)', '(?)', '(None)', '(None)', '(2)', '(e)', '(&)', '(l)', '(")', '(None)', '(r)', '(+)', '(.)', '(None)', '(a)', '(p)', '(@)', '(None)', '(w)', "(')", '(j)', '(1)', '()', '(6)', '(-)', '(b)', '(=)', '(d)', '(/)', '(x)', '(n)', '(c)', '(None)', '(!)', '(k)', '(()', '())', '(y)', '(t)', '(7)', '(z)', '(None)', '(,)', '(g)', '(q)', '(m)', '(:)', '(8)', '(None)', '(o)', '(9)', '(None)', '(0)']
print(MorseCode.path_to(BinNode('!')))  # - . - . - -
print(MorseCode.count_nodes(), MorseCode.count_leaves())  # 52 23
print(MorseCode.get_height_recursive(), MorseCode.get_height())  # 6 6
