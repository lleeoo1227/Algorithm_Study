class CircularQueue :
    def __init__(self, size) :
        self.size = size 
        self.max = self.size + 1
        self.cq = [None] * self.max 
        self.front = 0
        self.len = 0
        self.rear = None
                
    def empty(self) :
        return self.len == 0
                
    def full(self) :
        if self.empty() :
            return False
        return (self.rear + 1) % self.max == self.front
                    
    def enqueue(self, data) :
        if self.full() :
            raise Exception("Queue is FULL")
           
        elif self.empty() and self.rear != None :#넣었다가 다 뺀 후 다시 넣을 때 rear가 초기화되지 않고 그 다음 포인트로 갈 수 있게 해줌
            pass
        
        else :
            if self.empty() :
                self.rear = 0
        self.rear = (self.rear + 1) % self.max
        self.cq[self.rear] = data
        self.len += 1
        return self.cq[self.rear]
            
    def dequeue(self) :
        if self.empty() :
            raise Exception("Queue is EMPTY")
        else :
            self.front = (self.front + 1) % self.max
        data = self.cq[self.front]
        self.cq[self.front] = None
        self.len -= 1
        return data
        
    def show(self) :
        return self.cq




class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        

class SinglyLinkedList :
    def __init__(self, data) :
        new_node = Node(data)
        self.head = new_node
        self.len = 1
        
    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node.data)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list
        
    def is_empty(self) :
        if self.len == 0 :
            return True
        else :
            return False
        
    def AddNode_AtFirst(self, data) :
        if self.is_empty() :
            self.head = Node(data)
                        
        else :
            new_node = Node(data)
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node
        self.len += 1
        
    def AddNode_AtLast(self, data) :
        if self.is_empty() :
            self.head = Node(data)
            
        else :
            new_node = Node(data)
            node = self.head
            while node.next != None :
                node = node.next
            node.next = new_node
        self.len += 1
        
    def SelectNode(self, idx) :
        if idx >= self.len :
            print("Error : Overflow")
            
        elif self.is_empty() :
            print("Eror : Underflow")
            
        else :
            count = 0
            node = self.head
            while count < idx :
                node = node.next
                count += 1
            print("%dth data : " %idx, node.data)
            return node
        
    def AddNode(self, data, idx = -1) :
        if self.is_empty() :
            self.AddNode_AtFirst(data)
            
        elif idx == -1 :
            self.AddNode_AtFirst(data)
        
        elif idx >= self.len :
            self.AddNode_AtLast(data)
            
        else :
            new_node = Node(data)
            node = self.SelectNode(idx)
            temp_node = node.next
            node.next = new_node
            node.next.next = temp_node
            self.len += 1
            
    def DeleteNode_Head(self) :
        node = self.head
        self.head = node.next
        self.len -= 1
        #print(node)
        del node
            
    def DeleteNode(self, idx) :
        if self.is_empty() :
            print("Eror : Underflow")
        
        elif idx >= self.len :
            print("Error : Overflow")
            
        elif idx == 0 :
            self.DeleteNode_Head()
            
        else :
            count = 0
            node = self.head
            while count < idx - 1 :
                node = node.next
                count += 1 
            del_node = node.next
            node.next = node.next.next
            print(del_node.data)
            self.len -= 1
            del del_node
            
    def List_Size(self) :
        return self.len
 
