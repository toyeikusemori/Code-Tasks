class Node: #node constructor that has properties of its data and the pointers to the other nodes before and after it
    def __init__(self, dataval = None):
        self.data = dataval
        self.next = None
        self.prev = None


class SLinkedList:# linked list constructor with head and tail as its class properties
    def __init__(self):
        self.head = None
        self.tail = None

    def listprint(self): #linked list method to print the list out using a while loop. starts at the head then goes to next node after printing
                         #if the pointer is not null
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next



    def AtBeginning(self,newdata): #method to set node as the beginning of the linked list
            NewNode = Node(newdata)

    def AtEnd(self, newNode): #method to set node as the end of the linked list
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.nexts = newNode

        
    def ElementInsert(self,e7,e2): #define insert function that takes the list(self), the node to be inserted + the node that
                                    #the new node will be inserted after
        if e2!=0: #runs the conditions and next statements if the node before the node to be inserted is not null
            e7.next=e2.next #links the new node to the node that it shifted to the right upon insertion
            e2.next=e7 #links the new node to be the next node after e2
            e7.prev=e2 #links e2 as the node before the current node
            if e7.next!=0:#runs this statement if the next node after e7 is not null
                e7=e7.next.prev #change the previous link of the next element to e7
            if list.head==0: #if the list is empty, use e7 as the first element assigning it to the head and tail pointer
                list.head=e7
                list.tail=e7
            elif list.tail==e2: #if the last element was the element before, make e7 the last element
                list.tail=e7


list = SLinkedList() # intialise linked list 
list.head = Node("Mon")#set "Mon" node as head of the linked list
e7 = Node("Wed")#intialise the e7 node as "Wed"
e2 = Node("Tue")#intialise the e2 node as "Tue"
e3 = Node("Thur")#intialise the e3 node as "Thur"
e4 = Node("Fri")#intialise the e4 node as "Fri"
e5 = Node("Sat")#intialise the e5 node as "Sat"
e6 = Node("Sun")#intialise the e6 node as "Sun"
list.head.next = e2 #set the next pointer after the head as e2
e2.next = e3#set the next pointer after e2 to e3
e2.prev=list.head #set the head as the previous pointer to e2
e3.next = e4#set e4 as the next pointer to e3
e3.prev = e2#set e2 as the previous pointer to e3
e4.next = e5#set the e5 as the next pointer to e4
e4.prev = e3#set the previous pointer to e4 as e3
e5.next = e6#set the next ponter to e5 as e6
e5.prev = e4#set e4 as the previous pointer to e5
e6.prev = e5#set e5 to be the previous pointer to e6
e7.next = None #intialise the e7 next and previous pointers as null as e7 has not been inserted
e7.prev = None #
list.AtEnd(e5) # 

list.ElementInsert(e7,e2)#insert element using e7 as the new node and e2 as the node to place e7 after
list.listprint()#call method to print linked list



            
