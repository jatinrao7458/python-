# made class bcz we have our own type of data type 
class Node: 
    # next = none means its is the deafault value  
    def __init__(self,info,next=None):
        self.data = info
        self.next = next
    #making other class as with this technique we can make multiple linked list
class singly_linked_list:
    def __init__ (self,head=None):
        self.head = head

    def inert_at_end(self,value):
        # we are calling the constructor it will call the function 
        # 
        # there is no name for the memory created on the runtime it just has address 
        # temp will store the address of the memory created
        temp = Node(value)
        #   this is to check if the head is pointing to a linked list
        if (self.head!=None):
            # if condition is aggred this means the linked list is already made 
            # we cannot move the head neither the temp as the temp points to the last position and head to the first 
            # making a temporary variable to move it easily (an aasistent)

            t1 = self.head
            # t1 point on first location bcz we have only address of first location
            # we will now move t1 to end by checking last node will be equal to null
            while(t1.next!= None):
                t1 = t1.next
            # now we have to link the t1 to temp node  
            # to link it we ave to assign the temp address in the next of t1
            t1.next = temp
        else: 
            # if the linked list is not made then we will make it by assigning the address of temp to head
            # if linked list is node made means the head is pointing to none
            self.head = temp
    def printLL(self):              
        t1 = self.head
        while(t1!=None):
            # print it first bcz if we will do it at the end it will print only the last node 
            print(t1.data)
            t1 = t1.next
            # to print the last node bcz the t1 reaches last node after printing so it will be prevented.
            # to print the last node we will do it after the while loop
        print(t1.data)
obj = singly_linked_list()
obj.inert_at_end(10)
obj.inert_at_end(20)
obj.inert_at_end(30)
obj.printLL()
                 




        
