class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_doubly_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' <--> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length_of_doubly_linked_list(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_node_at_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)  
            self.head.prev = node 
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        else:
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = Node(data, None, itr)             

    def insert_at_index(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr) 
                if node.next is not None:              
                    node.next.prev = node     
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at_index(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None              
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next is not None:             
                    itr.next.prev = itr.prev           
                break

            itr = itr.next
            count+=1

    def insert_multiple_values_at_index(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print_forward(self):
        # This method prints list in forward direction. Use node.next for this.
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr.next is not None:
            llstr += str(itr.data)+' --> '
            itr = itr.next
        llstr += str(itr.data)
        print(llstr)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        iterator = self.head
        while iterator.next is not None:
            iterator = iterator.next

        llstr = ''
        while iterator.prev is not None:
            llstr += str(iterator.data)+' --> '
            iterator = iterator.prev
        llstr += str(iterator.data)
        print(llstr)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.print_forward()
    ll.print_backward()
    
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.print_backward()
    
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.print_backward()
    
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.print_backward()
    
    ll.insert_at(2,"kiwi")
    ll.print_forward()
    ll.print_backward()
