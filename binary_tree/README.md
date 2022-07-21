# Trees

A Tree is a Data structure in which data items are connected. Each Tree
consists of a root node from which we can access each element of the tree. Starting from the root node, each node
contains zero or more nodes connected to it as children. A simple binary tree each node can't have more than two
children

## Challenge

In this challenge we need to write two classes Binary Tree class and Binary Search Tree class and each one contains
different methods.

**Binary Tree Class** :

- Pre-Order method : this method should traverse as the following order first print node's value then traverse left then
  traverse right.
- In-Order method : this method should traverse as the following order first traverse left then print node's value then
  traverse right.
- Post-Order method : this method should traverse as the following order first traverse left then traverse right then
  print node's value

**Binary Search Tree Class**:

- Add method : to add a value according to a specific order.
- Contain method : to tell you if the given value can be found in the tree or not.

**For Code Challenge 16** :

- find maximum value method : To find the maximum value in a tree.


## Approach & Efficiency

For Time and Space complexity:

- Pre-Order method : O(n) because it depends on number of nodes and here we visit each node once.
- In-Order method : O(n) because it depends on number of nodes and here we visit each node once.
- Post-Order method : O(n) because it depends on number of nodes and here we visit each node once.

- Add method : O(log n) because each time we exclude half of remaining nodes, so we don't need to walk through the whole
  tree.
- Contain method : O(log n) because each time we exclude half of remaining nodes, so we don't need to walk through the
  whole tree.

**For Code Challenge 16** :

- find maximum value method : because it depends on number of nodes and here we visit each node once.

## Whiteboard For Code Challenge 16:




## API
<!-- Description of each method publicly available in each of your trees -->
**For methods in Binary Tree Class** : 
- first we made a tree

    
    tree = BinaryTree()
    tree.root = Node(15)
    tree.root.left = Node(7)
    tree.root.right = Node(19)

- then we call the method we want 


     print(tree.pre_order())
    Output : [15, 7, 19] 

     print(tree.in_order())
     Output : [7, 15, 19]
     
     print(tree.post_order())
     Output : [7, 19, 15]

**For methods in Binary Search Tree** :
- first we made a binary search tree by using ***Add*** method

      btree = BinarySearchTree()
      btree.add(10)
      btree.add(15)
      btree.add(7)
      btree.add(19)
      btree.add(9)
      btree.add(5)

- We can search for a certain value if it's exist or not by using ***Contains*** method


    print(btree.contains(77))
     Output : False

     
**For Code Challenge 16** :

**find maximum value method**

- first we made a tree


    tree = BinaryTree()
    tree.root = Node(15)
    tree.root.left = Node(7)
    tree.root.right = Node(19)

- then we call the method

      tree.find_max()
       Output : 19