class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList: 
    def __init__(self, value):
        self.head = NewNode(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = NewNode(value)

        self.tail.next = new_node
        self.tail = new_node

        self.length+=1
        self.display()

    def prepend(self, value):
        new_node = NewNode(value)

        new_node.next= self.head
        self.head = new_node

        self.length+=1
        return self.display()

    def display(self):
        current_node = self.head
        values = []
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        print(" -> ".join(values))

    def insert(self, index, value):
        if index > self.length:
            return print(f"Index {index} out of range: {self.lenght}")

        if index == 0:
            self.prepend(value)
            return self.display()
        
        new_node = NewNode(value)
        current_node = self.head
        
        i=0
        while i < index:
            if i==index-1:
                new_node.next = current_node.next
                current_node.next=new_node
                self.length+=1
                return self.display()
            i+=1
            current_node = current_node.next
 
    def remove(self, index):
        if index > self.length:
            return print(f"Index {index} out of range: {self.lenght}")
        
        current_node = self.head
        
        i=0
        while i <= index:
            if i==index-1:
                leader = current_node
            if i==index:
                leader.next = current_node.next
                self.length+=-1
                return self.display()
            current_node = current_node.next
            i+=1

    def reverse(self):
        pass