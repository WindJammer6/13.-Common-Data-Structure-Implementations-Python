# 14.-Common-Data-Structure-Implementations-Python:large_blue_circle::heavy_minus_sign::large_blue_circle::heavy_minus_sign::large_blue_circle:

A compilation of various common Data Structure implementations in Python.

## Thoughts on starting this compilation
Searched the internet, however I haven't found a good compilation of the various common Data Structure implementations in Python. So I decided to make one for myself, or for anyone else who wish to use this compilation. Of course, every version of a Data Structure implementation is slightly different in terms of how they are implemented so if you wish to use the Data Structure Python implementations in this compilation for your personal projects you might need to have a understanding on how these implementations are created, so I strongly suggest you take a look at [codebasics' Youtube playlist on Data Structure and Algorithms](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12) that I got the Data Structure Python implementations from, or from looking at the seperate repository in my Github profile ['12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python'](https://github.com/WindJammer6/12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python)

<ins>Disclaimer</ins>: These Data Structures Python implementations are done by Dhaval Patel, founder of the Youtube channel [codebasics](https://www.youtube.com/@codebasics), I did not create these Data Structure Python implementations, I merely compiled them while doing some minor changes as well as added some simple Instance Methods on the Data Structure Classes. 

<br>

<br>

## Table of Contents
Here are the common Data Structure Python implementations in this compilation:
+ [Code Description](#codedescription)
   1. Linked List Data Structures:
      + [Singly Linked List Data Structure](#singlylinkedlist)
      + [Doubly Linked List Data Structure](#doublylinkedlist)
   2. [Hash Table Data Structure](#hashtable)
   3. [Stack Data Structure](#stack)
   4. [Queue Data Structure](#queue)
   5. Tree Data Structures:
      + [General Tree Data Structure](#generaltree)
      + [Binary Search Tree Data Structure](#binarysearchtree)

Note: Arrays are also a very common Data Structure, however, it is a bit redundant to try to re-implement them again in Python as there are already 3 different Array Data Structure implementations in Python as built-in data types, Lists, Sets and Tuples. Hence, I will be omitting Array Data Structures implementations in Python in this compilation.

<br>

<br>

## Code Description <a name = "codedescription"></a>

### Singly Linked List Data Structure <a name = "singlylinkedlist"></a>
Here are the Instance Methods and functions available in the 'Node' and 'LinkedList' classes:
+ Under the 'Node' class:
   + __init__ (Special Method)
+ Under the 'LinkedList' class:
   + __init__ (Special Method)
   + insert_node_at_beginning (Instance Method)
   + insert_at_end (Instance Method)
   + get_length_of_linked_list (Instance Method)
   + print_linked_list (Instance Method)
   + remove_at_index (Instance Method)
   + insert_at_index (Instance Method)
   + insert_multiple_values_at_index (Instance Method)
   + merge_linked_list_at_end (function)
 
Visualisation of the Singly Linked List Data Structure (from 'print_linked_list()'):
```
56-->86-->89-->39-->99-->7-->90-->
```

<br>

<br>

### Doubly Linked List Data Structure <a name = "doublylinkedlist"></a>
Here are the Instance Methods and functions available in the 'Node' and 'DoublyLinkedList' classes:
+ Under the 'Node' class:
   + __init__ (Special Method)
+ Under the 'DoublyLinkedList' class:
   + __init__ (Special Method)
   + insert_node_at_beginning (Instance Method)
   + insert_at_end (Instance Method)
   + get_length_of_doubly_linked_list (Instance Method)
   + print_doubly_linked_list (Instance Method)
   + remove_at_index (Instance Method)
   + insert_at_index (Instance Method)
   + insert_multiple_values_at_index (Instance Method)
   + print_forward (Instance Method)
   + print_backwards (Instance Method)
 
Visualisation of the Doubly Linked List Data Structure (from 'print_doubly_linked_list()'):
```
banana <--> mango <--> grapes <--> orange
```

<br>

<br>

### Hash Table Data Structure <a name = "hashtable"></a>
I understand that there is already a Hash Table Data Structure implementation in Python as the built-in data type, Dictionaries. However I believe we can learn a lot more about Hash Tables and how Python's Dictionaries work from learning how to re-implement Hash Tables in Python.

This Hash Table Data Structure implementation in Python handles collisions via Seperate Chaining.

Here are the Instance Methods and functions available in the 'HashTable' class:
+ Under the 'HashTable' class:
  + __init__ (Special Method)
  + get_hash (Instance Method)
  + __setitem__ (Special Method)
  + __getitem__ (Special Method)
  + __delitem__ (Special Method)

Visualisation of the Hash Table Data Structure (from using Python's 'print()' function on the 'HashTable' object's '.arr' attribute):
```
[[], [('march 8', 380)], [('march 9', 302)], [], [], [], [], [], [], [('march 6', 110), ('march 17', 450)]]
```

<br>

<br>

### Stack Data Structure <a name = "stack"></a>
This Stack Data Structure implementation in Python is created using the 'deque' (or Double-Ended Queue) special Data Structure from Python's 'collections' library.

Here are the Instance Methods and functions available in the 'Stack' class:
+ Under the ‘Stack' class:
   + _init_ (Special Method)
   + push (Instance Method)
   + pop (Instance Method)
   + peek (Instance Method)
   + is_empty (Instance Method)
   + size (Instance Method)
   + __repr__ (Special Method)

Visualisation of the Stack Data Structure (from Python’s ‘print()’ function on the ‘Stack’ object and ‘__repr__’):
```
deque([67, 7, 748])
```

<br>

<br>

### Queue Data Structure <a name = "queue"></a>
This Queue Data Structure implementation in Python is created using the 'deque' (or Double-Ended Queue) special Data Structure from Python's 'collections' library.

Here are the Instance Methods and functions available in the 'Queue' class:
+ Under the ‘Queue' class:
   + _init_ (Special Method)
   + enqueue (Instance Method)
   + dequeue (Instance Method)
   + is_empty (Instance Method)
   + size (Instance Method)
   + __repr__ (Special Method)

Visualisation of the Queue Data Structure (from Python’s ‘print()’ function on the ‘Queue’ object and ‘__repr__’):
```
deque([{'company': 'Walmart', 'timestamp': '15 apr, 11.03am', 'price': 135}, {'company': 'Walmart', 'timestamp': '15 apr, 11.02am', 'price': 131.12}])
```

<br>

<br>

### General Tree Data Structure <a name = "generaltree"></a>
Here are the Instance Methods and functions available in the 'GeneralTreeNode' class:
+ Under the ‘GeneralTreeNode' class:
   + _init_ (Special Method)
   + add_child_node (Instance Method)
   + get_level_of_node (Instance Method)
   + print_general_tree (Instance Method)
   + build_electronics_tree (function)

Visualisation of the General Tree Data Structure (from ‘print_general_tree()’):
```
Electronics
   |__Laptop
      |__Macbook
      |__Microsoft Surface
      |__Thinkpad
   |__Cell Phone
      |__iPhone
      |__Google Pixel
      |__Vivo
   |__Television
      |__Samsung
      |__LG
```

<br>

<br>

### Binary Search Tree Data Structure <a name = "binarysearchtree"></a>
Here are the Instance Methods and functions available in the 'BinarySearchTreeNode' class:
+ Under the ‘BinarySearchTreeNode' class:
   + _init_ (Special Method)
   + depth_first_search_in_order_traversal (Instance Method)
   + depth_first_search_pre_order_traversal (Instance Method)
   + depth_first_search_post_order_traversal (Instance Method)
   + search_binary_search_tree (Instance Method)
   + print_binary_search_tree (Instance Method)
   + search_binary_search_tree (Instance Method)
   + calculate_sum (Instance Method)
   + find_min (Instance Method)
   + find_max (Instance Method)
   + delete_node (Instance Method)
   + build_electronics_tree (function)

Visualisation of the Binary Search Tree Data Structure (from ‘print_binary_search_tree()’’):
```
        -> 88
    -> 27
            -> 23
        -> 20
-> 15
        -> 14
    -> 12
        -> 7
```
