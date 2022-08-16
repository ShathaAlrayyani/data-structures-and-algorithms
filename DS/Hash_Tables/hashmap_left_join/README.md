
## Code Challenge 33

Write a function that LEFT JOINs two hashmaps into a single data structure.
  - Arguments: two hash maps.
    - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
    - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.

  - Return: The returned data structure that holds the results is up to you, so long as it achieves the LEFT JOIN logic.

## Approach & Efficiency

- Time Complexity: O(N) liner iteration involved. (for loop)
- Space Complexity:O(N) there is an array created in the memory

## Solution

- create a function called left_join that takes 2 hashmap as arguments.
- declare a left_join_table as array that holds the final result.
- iterate over the first hashmap using for loop.
- iterate over the second hashmap using if statement. 
- append the result from the get method on hashmap_1 based on the key in variable called value_from_hashmap_1.
- append the result from the get method on hashmap_2 based on the key in variable called value_from_hashmap_2.
- append the variable to the left_join_table array.
- return the left_join_table


## Test

pytest .\tests\test_hashmap_left_join.py

