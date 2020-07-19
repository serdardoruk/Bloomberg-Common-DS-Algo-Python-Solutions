'''
Design a data structure with requirements:

You have a <Key, Value> structured input data for all objects
Where you have
Insert : O(1)
Lookup : O(1)
Delete : O(1)
You can traverse the added elements in the order they were inserted.
'''

# Thank you for posting the question.
# Here's an idea for such a data structure (correct me if I am wrong):
# It shares similarity between LRU cache.
# We will use std::unordered_map(hashmap) and std::list(doubly linked list).
# our map will also save the list::iterator(pointer to an element in the list). Note that list iterators do not get 
# invalidated on movement of elements(unlike vector).

# Insert : We will push_front value in the list simply insert the <key, list::iterator tofirst 
# element(list.begin())> into the map. [map insertion : amortized O(1) + list push_front O(1)]
# lookup : simple map lookup. [ O(1)]
# Delete : lookup the item in the map (O(1)) and save list iterator. delete from the map. using the saved 
# iterator delete from the list O(1).
# Traversal : We can traverse the list in the order they were inserted as its a doubly linked list.