# 14.-Common-Data-Structure-Implementations-Python
A compilation of various common Data Structure implementations in Python.

## Thoughts on starting this project
Searched the internet, however I haven't found a good compilation of the various common Data Structure implementations in Python. So I decided to make one for myself, or for anyone else who wish to use this compilation. Of course, every version of a Data Structure implementation is slightly different in terms of how they are implemented so if you wish to use the Data Structure Python implementations in this compilation for your personal projects you might need to have a understanding on how these implementations are created, so I strongly suggest you take a look at codebasics' Youtube playlist on Data Structure and Algorithms that I got the Data Structure Python implementations from (here's the [link](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12)), or from looking at the seperate repository in my Github profile '12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python' (here's the [link](https://github.com/WindJammer6/12.-Data-Structures-and-Algorithms-Learning-and-Practice-Python))

<ins>Disclaimer</ins>: These Data Structures Python implementations are done by Dhaval Patel, founder of the Youtube channel [codebasics](https://www.youtube.com/@codebasics), I did not create these Data Structure Python implementations, I merely compiled them while doing some minor changes as well as added some simple Instance Methods on the Data Structure Classes. 

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

## Code Description <a name = "codedescription"></a>

### Singly Linked List Data Structure <a name = "singlylinkedlist"></a>
Here are the Instance Methods and functions available in the 'Node' and 'LinkedList' classes:
+ Under the 'Node' class:
   + __init__ (Instance Method)
+ Under the 'LinkedList' class:
   + __init__ (Instance Method)
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
   + __init__ (Instance Method)
+ Under the 'DoublyLinkedList' class:
   + __init__ (Instance Method)
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

Here are the Instance Methods and functions available in the 'HashTable' classes:
+ Under the "HashTable' class:
  + __init__ (Instance Method)
  + get_hash (Instance Method)
  + __setitem__ (Special Method)
  + __getitem__ (Special Method)
  + __delitem__ (Special Method)

Visualisation of the Hash Table Data Structure (from using Python's 'print()' on the 'HashTable' object's '.arr' attribute):
```

```

<br>

<br>

### Stack Data Structure <a name = "stack"></a>
Makes use of the deque special Data structure from Python's collections library

Here are the Instance Methods and functions available in the 'Node' and 'LinkedList' classes:
+ Under the 'Node' class:
   + __init__ (Instance Method)
+ Under the 'LinkedList' class:
   + __init__ (Instance Method)
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

### Queue Data Structure <a name = "queue"></a>

<br>

<br>

### General Tree Data Structure <a name = "generaltree"></a>

<br>

<br>

### Binary Search Tree Data Structure <a name = "binarysearchtree"></a>

<br>

<br>
