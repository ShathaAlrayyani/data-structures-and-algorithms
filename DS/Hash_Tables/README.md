# Hash Tables

Hash tables are a type of data structure in which the address or the index value of the data element is generated from a
hash function, and that makes accessing the data faster.

## Challenge
To write a hash table class with different methods inside:
- set : This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- get : Returns: Value associated with that key in the table.
- contains : Returns: Boolean, indicating if the key exists in the table already.
- keys : Returns Collection of keys.
- hash : Returns Index in the collection for that key.


## Approach & Efficiency

- hash: Time and space complexity is O(1)
- set : Time and space complexity is O(1)
- get	: Time and space complexity is O(n)
- contains	: Time and space complexity is O(n)
- key	: Time and space complexity is O(n)

## API

| Method   | Params     | Output          |
|----------|------------|-----------------|
| hash     | key        | hash code (int) |
| set      | Key, Value | None            |
| get      | Key, Value | Value           |
| contains | key        | Boolean         |
| key      | None       | Array           |



### to run the test :
pytest test\test_hash_map.py
