from Graphs.Tree import BinNode, BinTree
from Lists import build_heap
def binary_heap(l: list):
    build_heap(l, len(l))
    def helper(curr_root, rest, i=1):
        left = helper(rest[0], rest[(2 ** i):], i + 1) if rest else None
        right = helper(rest[1], rest[2 * 2 ** i:], i + 1) if rest[1:] else None
        res = BinNode(curr_root, left, right)
        return res
    return BinTree(helper(l[0], l[1:]))
def print_zig_zag(t: BinTree):
    def helper(from_left: bool, *nodes: BinNode):
        new = []
        if from_left:
            for n in nodes:
                if n.left is not None:
                    new.insert(0, n.left), print(n.left, end=' ')
                if n.right is not None:
                    new.insert(0, n.right), print(n.right, end=' ')
        else:
            for n in nodes:
                if n.right is not None:
                    new.insert(0, n.right), print(n.right, end=' ')
                if n.left is not None:
                    new.insert(0, n.left), print(n.left, end=' ')
        if not new:
            return
        print(), helper(not from_left, *new)
    print(t.root), helper(True, t.root)
MorseCode = BinTree('')
MorseCode.root.left = BinNode('E')
MorseCode.root.left.left = BinNode('I')
MorseCode.root.left.left.left = BinNode('S')
MorseCode.root.left.left.left.left = BinNode('H')
MorseCode.root.left.left.left.left.left = BinNode('5')
MorseCode.root.left.left.left.left.right = BinNode('4')
MorseCode.root.left.left.left.right = BinNode('V')
MorseCode.root.left.left.left.right.left = BinNode()
MorseCode.root.left.left.left.right.left.left = BinNode()
MorseCode.root.left.left.left.right.left.left.right = BinNode('$')
MorseCode.root.left.left.left.right.right = BinNode('3')
MorseCode.root.left.left.right = BinNode('U')
MorseCode.root.left.left.right.left = BinNode('F')
MorseCode.root.left.left.right.right = BinNode()
MorseCode.root.left.left.right.right.left = BinNode()
MorseCode.root.left.left.right.right.left.left = BinNode('?')
MorseCode.root.left.left.right.right.left.right = BinNode('_')
MorseCode.root.left.left.right.right.right = BinNode('2')
MorseCode.root.left.right = BinNode('A')
MorseCode.root.left.right.left = BinNode('R')
MorseCode.root.left.right.left.left = BinNode('L')
MorseCode.root.left.right.left.left.left = BinNode('&')
MorseCode.root.left.right.left.left.right = BinNode()
MorseCode.root.left.right.left.left.right.left = BinNode('"')
MorseCode.root.left.right.left.right = BinNode()
MorseCode.root.left.right.left.right.left = BinNode('+')
MorseCode.root.left.right.left.right.left.right = BinNode('.')
MorseCode.root.left.right.right = BinNode('W')
MorseCode.root.left.right.right.left = BinNode('P')
MorseCode.root.left.right.right.left.right = BinNode()
MorseCode.root.left.right.right.left.right.left = BinNode('@')
MorseCode.root.left.right.right.right = BinNode('J')
MorseCode.root.left.right.right.right.right = BinNode('1')
MorseCode.root.left.right.right.right.right.left = BinNode('\'')
MorseCode.root.right = BinNode('T')
MorseCode.root.right.left = BinNode('N')
MorseCode.root.right.left.left = BinNode('D')
MorseCode.root.right.left.left.left = BinNode('B')
MorseCode.root.right.left.left.left.left = BinNode('6')
MorseCode.root.right.left.left.left.left.right = BinNode('-')
MorseCode.root.right.left.left.left.right = BinNode('=')
MorseCode.root.right.left.left.right = BinNode('X')
MorseCode.root.right.left.left.right.left = BinNode('/')
MorseCode.root.right.left.right = BinNode('K')
MorseCode.root.right.left.right.left = BinNode('C')
MorseCode.root.right.left.right.left.right = BinNode()
MorseCode.root.right.left.right.left.right.left = BinNode(';')
MorseCode.root.right.left.right.left.right.right = BinNode('!')
MorseCode.root.right.left.right.right = BinNode('Y')
MorseCode.root.right.left.right.right.left = BinNode('(')
MorseCode.root.right.left.right.right.left.right = BinNode(')')
MorseCode.root.right.right = BinNode('M')
MorseCode.root.right.right.left = BinNode('G')
MorseCode.root.right.right.left.left = BinNode('Z')
MorseCode.root.right.right.left.left.left = BinNode('7')
MorseCode.root.right.right.left.left.right = BinNode()
MorseCode.root.right.right.left.left.right.right = BinNode(',')
MorseCode.root.right.right.left.right = BinNode('Q')
MorseCode.root.right.right.right = BinNode('O')
MorseCode.root.right.right.right.left = BinNode()
MorseCode.root.right.right.right.left.left = BinNode('8')
MorseCode.root.right.right.right.left.left.left = BinNode(':')
MorseCode.root.right.right.right.right = BinNode()
MorseCode.root.right.right.right.right.left = BinNode('9')
MorseCode.root.right.right.right.right.right = BinNode('0')
if __name__ == '__main__':
    print_zig_zag(MorseCode)
    for Type in ('preorder', 'in-order', 'post-order'):
        MorseCode.print(Type)
    print(MorseCode.code_in_morse('4'), MorseCode.count_nodes(), MorseCode.count_leaves(), MorseCode.get_height_recursive(), MorseCode.get_height(), MorseCode.nodes_on_level(6), MorseCode.width())
    print(MorseCode.encode('Testing encode.'))
