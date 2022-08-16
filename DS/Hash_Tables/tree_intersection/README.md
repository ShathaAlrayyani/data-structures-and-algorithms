## Challenge
Find common values in 2 binary trees using hashmap.
Write a function called tree_intersection that takes two binary trees as parameters.
Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process

## Approach & Efficiency

**Big(O)**:
- Space: O(1) The function return one array.
- Time: O(n) the worst case in for loops

## Solution

make 2 different binary trees then call the function and give it the 2 binary trees as arguments.

        tree_intersection(b_tree1, b_tree2)

The output will be an array with the common values which have the same position in both trees.

## How to run the test
pytest .\tests\test_tree_intersection.py