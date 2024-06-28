class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    """
    Build a linked list manually by adding the list nodes and assigning
    """
#     # Building a linked list manually
#     def build_linkedlist():
#         print("Build a linked list")
#         node_1 = ListNode(1)
#         node_2 = ListNode(3)
#         node_3 = ListNode(5)
#         node_4 = ListNode(7)

#         node_1.next = node_2
#         node_2.next = node_3
#         node_3.next = node_4

#         return node_1


# def traverse_linkedlist():
#     node_1 = ListNode(1)
#     node_2 = ListNode(3)
#     node_3 = ListNode(5)
#     node_4 = ListNode(7)

#     node_1.next = node_2
#     node_2.next = node_3
#     node_3.next = node_4

#     # Make current pointer points to node_1
#     current = node_1

#     # Loop thru the linked list until None
#     while current is not None:
#         print("Current node: ", current.val)
#         # Update the current to point to the next node

#         current = current.next


class LinkedList:
    def __init__(self):
        self.head = None
    """
    CRUD functionalities:
    1. Create/Add
    2. Read/Get
    3. Update
    4. Delete
        
    """
    # Create/Add/Insert
    # a. Insert a node to an existing linked list
    #         -> use prev pointer to keep track of the location where you want to insert
    #         -> create a new node
    #         -> new node .next points to prev.next
    #         -> prev.next = new node
    # b. Insert a node at front to an existing linked list
    #         -> create a new node
    #         -> new node .next = self.head
    #         -> self.head = new node
    
    # check if the linked list is empty
    def is_empty(self):
        return self.head is None
    
    def add(self, location, val):
        # if location > 0 -> set prev to head
        if(location > 0):
            prev = self.head
            # loop thru the linked list till the position that is one before the inserting location
            for i in range(location - 1 ):
                # make prev = prev.next in each iteration
                prev = prev.next
            
            # after the loop, prev has arrived the poistion before the location
            # -> create a new list node
            new_node = ListNode(val)
            new_node.next = prev.next
            prev.next = new_node
        elif(location == 0):
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node
        return
    
    # traverse the whole linked list
    def traverse(self):
        # make current = self.head
        current = self.head
        # loop thru the whole linked list
        while(current is not None):
            print(current.val)
            current = current.next
        return
            
    # read one node
    def read(self, location):
        # loop till the location
        current = self.head
        """
        Method 1: while
        """
        # i = 0 
        # while( i != location):
        #     current = current.next
        #     i += 1
        
        """
        Method 2: for
        """
        for i in range(location):
            current = current.next
            
        return current.val
    
    # update one node
    def update(self, location, val):
        # create a current pointer and loop till the location
        current = self.head
        for i in range(location):
            current = current.next
        # outside the loop -> current arrive the location
        current.val = val
        
        return 
    
    # delete
    def delete(self,location):
        # if location is greater than 0 -> loop till the location
        if(location > 0):
            prev = self.head
            for i in range(location - 1):
                prev = prev.next
            # outside the loop -> prev arrives the position before the location
            prev.next =prev.next.next
        
        elif(location == 0):
            self.head = self.head.next
            
if __name__ == "__main__":
    linked_list_1 = LinkedList()
    linked_list_1.add(0,1)
    linked_list_1.add(1,3)
    linked_list_1.add(2,5)
    linked_list_1.add(3,7)
    # add at front
    linked_list_1.add(0,0)
    
    # traverse the linked list
    linked_list_1.traverse()
    
    # read
    # print("Read: ",linked_list_1.read(0))
    # print("Read: ",linked_list_1.read(1))
    # print("Read: ",linked_list_1.read(2))
    # print("Read: ",linked_list_1.read(3))
    # print("Read: ",linked_list_1.read(4))
    
    # update 
    print("Update the linked list:")
    linked_list_1.update(0,0)
    # print("Read: ",linked_list_1.read(0))
    linked_list_1.update(1,2)
    linked_list_1.update(2,4)
    linked_list_1.update(3,6)
    linked_list_1.update(4,8)
    linked_list_1.traverse()
    
    
    # delete
    # print("Delete:")
    # linked_list_1.delete(0)
    # linked_list_1.traverse()
    # linked_list_1.add(0,0)
    # linked_list_1.add(5,100)
    # linked_list_1.traverse()
    # linked_list_1.delete(5)
    # linked_list_1.traverse()
    
    print("Linked list 2:")
    linked_list_2 = LinkedList()
    print("Is linked list 1 empty? ",linked_list_1.is_empty())
    print("Is linked list 2 empty? ",linked_list_2.is_empty())