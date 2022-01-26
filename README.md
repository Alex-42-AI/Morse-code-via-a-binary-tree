# Morse-code-via-a-binary-tree
A binary tree is a recursive data structure, composing of a root, a left subtree and a right subtree. Morse code can be implemented with the help of a binary tree, where, for example,
a left subtree means adding a dot and a right subtree could mean adding a dash. That way, the letter 'k', which in Morse code is written as "- . -", can be the root of the right subtree
of the left subtree of the right subtree of the original tree of the Morse code. On top of that, the implemented binary tree in this project has:
1) methods left() and right(), that return respectively the left subtree and the right subtree;
2) methods to return the height of the tree - one recursive and one using DFS;
3) a method for counting the leaves of the tree;
4) a method for counting the nodes of the tree;
5) a method for finding the path from the root to a node with a given value in the tree;
6) a method for inverting the tree;
7) methods for printing all the node values in the tree preorder, in order and post order.
