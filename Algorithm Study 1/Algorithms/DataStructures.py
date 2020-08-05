class Queue :
    def __init__(self) :
        self.que = []
        self.len = 0
            
    def enqueue(self, data) :
        self.que.append(data)
        self.len += 1
    
    def dequeue(self, data) :
        self.que.pop(0)
        print("0th element of Queue : ", self.que.pop(0))
        self.len -= 1
    
    def List_Size(self) :
        return self.len
    
    def show(self) :
        return self.que
    
    
    

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
    def __init__(self) :
        self.head = None
        self.len = 0
        
    def __str__(self):
        if self.len == 0 :
            print_list = "List is EMPTY"
            return print_list
        else :
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
        new_node = Node(data)
        if self.is_empty() :
            self.head = new_node
                        
        else :
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node
        self.len += 1
        
    def AddNode_AtLast(self, data) :
        new_node = Node(data)
        if self.is_empty() :
            self.head = new_node
            
        else :
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
            return node
        
    def AddNode(self, data, idx = -1) : #idx에 아무것도 안들어오면 idx = -1
        if self.is_empty() :
            self.AddNode_AtFirst(data)
            
        elif idx == -1 :
            self.AddNode_AtFirst(data)
        
        elif idx >= self.len :
            self.AddNode_AtLast(data)
            
        else :
            new_node = Node(data)
            node = self.SelectNode(idx - 1)
            temp_node = node.next
            node.next = new_node
            node.next.next = temp_node
            self.len += 1
            
    def DeleteNode_Head(self) :
        if self.is_empty() :
            print("Error : List is EMPTY")
        
        elif self.len == 1 :
            print("Deleted node's data : ", self.head.data)
            self.head = None
            self.len = 0
            
        else :
            node = self.head
            self.head = node.next
            self.len -= 1
            print("Deleted node's data : ", node.data)
            del node
            
    def DeleteNode(self, idx = -1) :
        if self.is_empty() :
            print("Eror : Underflow")
        
        elif idx >= self.len :
            print("Error : Overflow")
            
        elif idx == 0 or idx == -1 :
            self.DeleteNode_Head()
            
        else :
            node = self.SelectNode(idx - 1)
            del_node = node.next
            node.next = node.next.next
            print("Deleted node's data : ", del_node.data)
            self.len -= 1
            del del_node
            
    def List_Size(self) :
        return self.len
    
    
    

class CircularlyLinkedList :
    def __init__(self) :
        self.head = None
        self.tail = None
        self.len = 0
        
    def __str__(self):
        if self.len == 0 :
            print_list = "List is EMPTY"
            return print_list
        else:
            print_list = '[ '
            node = self.head
            if self.len == 1 :
                print_list += str(node.data)
            else :
                while True:
                    print_list += str(node.data)
                    if node.next == self.head :
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
        new_node = Node(data)
        if self.is_empty() :
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            #self.tail.next = self.head
                        
        else :
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node
            self.tail.next = self.head
        self.len += 1
        
    def AddNode_AtLast(self, data) :
        new_node = Node(data)
        if self.is_empty() :
            self.head = new_node
            self.tail = new_node
            self.head.next = self.tail
            #self.tail.next = self.head
 
        else :
            temp_node = self.tail
            self.tail = new_node
            temp_node.next = self.tail
            self.tail.next = self.head
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
            return node
        
    def AddNode(self, data, idx = -1) : #idx에 아무것도 안들어오면 idx = -1
        if self.is_empty() :
            self.AddNode_AtFirst(data)
            
        elif idx == -1 :
            self.AddNode_AtFirst(data)
        
        elif idx >= self.len :
            self.AddNode_AtLast(data)
            
        else :
            new_node = Node(data)
            node = self.SelectNode(idx - 1)
            temp_node = node.next
            node.next = new_node
            node.next.next = temp_node
            self.len += 1
            
    def DeleteNode_Head(self) :
        if self.is_empty() :
            print("Eror : List is EMPTY")
        
        elif self.len == 1 :
            print("Deleted node's data : ", self.head.data)
            self.head = None
            self.tail = None
            self.len = 0
        
        else :
            node = self.head
            self.head = node.next
            self.tail.next = self.head
            self.len -= 1
            print("Deleted node's data : ", node.data)
            del node
            
    def DeleteNode(self, idx = -1) :
        if self.is_empty() :
            print("Eror : Underflow")
        
        elif idx >= self.len :
            print("Error : Overflow")
            
        elif idx == 0 or idx == -1 :
            self.DeleteNode_Head()
            
        else :
            count = 0
            node = self.head
            while count < idx - 1 :
                node = node.next
                count += 1 
            del_node = node.next
            node.next = node.next.next
            print("Deleted node's data : ", del_node.data)
            self.len -= 1
            del del_node
            
    def List_Size(self) :
        return self.len
    
    

class Node_DLL :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedList :
    def __init__(self) :
        self.head = Node_DLL(None)
        self.tail = Node_DLL(None)
        self.head.prev = None
        self.tail.next = None
        self.len = 0
        
    def __str__(self):
        if self.len == 0 :
            print_list = "List is EMPTY"
            return print_list
        else :
            print_list = '[ '
            node = self.head.next
            while True:
                print_list += str(node.data)
                if node.next == self.tail:
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
        new_node = Node_DLL(data)
        if self.is_empty() :
            self.node = new_node
            self.node.prev = self.head
            self.node.next = self.tail
            self.head.next = self.node
            self.tail.prev = self.node
                        
        else :
            temp_node = self.head.next
            self.head.next = new_node
            self.head.next.prev = self.head
            self.head.next.next = temp_node
            temp_node.prev = self.head.next
            
        self.len += 1
        
    def AddNode_AtLast(self, data) :
        new_node = Node_DLL(data)
        if self.is_empty() :
            self.node = new_node
            self.node.prev = self.head
            self.node.next = self.tail
            self.head.next = self.node
            self.tail.prev = self.node
            
        else :
            node = self.tail.prev
            node.next = new_node
            node.next.prev = node
            node.next.next = self.tail
            self.tail.prev = node.next
            
        self.len += 1
        
    def SelectNode(self, idx) :
        if idx >= self.len :
            print("Error : Overflow")
            
        elif self.is_empty() :
            print("Eror : Underflow")
                        
        else :
            if idx + 1 <= self.len / 2 :
                node = self.head
                count = 0
                while count <= idx :
                    node = node.next
                    count += 1
                return node
            
            else :
                node = self.tail
                count = 0
                while count < self.len - idx :
                    node = node.prev
                    count += 1
                return node
        
    def AddNode(self, data, idx = -1) : #idx에 아무것도 안들어오면 idx = -1
        if self.is_empty() :
            self.AddNode_AtFirst(data)
            
        elif idx == -1 :
            self.AddNode_AtFirst(data)
        
        elif idx >= self.len :
            self.AddNode_AtLast(data)
            
        else :
            new_node = Node_DLL(data)
            node = self.SelectNode(idx - 1)
            temp_node = node.next
            node.next = new_node
            node.next.next = temp_node
            node.next.prev = node
            temp_node.prev = node.next
            self.len += 1
            
    def DeleteNode_Head(self) :
        if self.is_empty() :
            print("Error : List is EMPTY")
        
        elif self.len == 1 :
            node = self.head.next
            print("Deleted noed's data : ", node.data)
            self.len = 0
            del node
            
        else :
            node = self.head.next
            self.head.next = node.next
            self.head.next.prev = self.head
            self.len -= 1
            print("Deleted node's data : ", node.data)
            del node
            
    def DeleteNode(self, idx = -1) :
        if self.is_empty() :
            print("Eror : Underflow")
        
        elif idx >= self.len :
            print("Error : Overflow")
            
        elif idx == 0 or idx == -1 :
            self.DeleteNode_Head()
            
        else :
            node = self.SelectNode(idx - 1)
            del_node = node.next
            node.next = del_node.next
            node.next.prev = node
            self.len -= 1
            print("Deleted node's data : ", del_node.data)
            del del_node
            
    def List_Size(self) :
        return self.len



class Node_Tree :
    def __init__(self, data) :
        self.data = data
        self.left, self.right = None, None
        
class BST :
    def __init__(self) :
        self.root = None
        
    def insert(self, data) :
        new_node = Node_Tree(data)
        if self.root == None :
            self.root = new_node
            
        else :
            current_node = self.root
            while True :
                if data < current_node.data :
                    if current_node.left != None :
                        current_node = current_node.left
                    else :
                        current_node.left = new_node
                        break
                        
                else :
                    if current_node.right != None :
                        current_node = current_node.right
                    else :
                        current_node.right = new_node
                        break
                        
    def delete(self, data) :
        self.current = self.root
        self.parent = self.root
        
        if self.root == None :
            return False
        
        else :
            while True :
                if self.current.data == data :
                    break
                    
                else :
                    if data < self.current.data :
                        if self.current.left == None :
                            return "No Data to Delete"
                        else :
                            self.parent = self.current
                            self.current = self.current.left
                    else :
                        if self.current.right == None :
                            return "No Data to Delete"
                        else :
                            self.parent = self.current
                            self.current = self.current.right
                        
        #case1 - no child
        
        if self.current.left == None and self.current.right == None :
            if self.current.data < self.parent.data :
                self.parent.left = None
            else :
                self.parent.right = None
                
        #case2 - 1 child
        
        elif self.current.left != None and self.current.right == None :
            if self.current.data < self.parent.data :
                self.parent.left = self.current.left
            else :
                self.parent.right = self.current.left
                
        elif self.current.left == None and self.current.right != None :
            if self.current.data < self.parent.data :
                self.parent.left = self.current.right
            else :
                self.parent.right = self.current.right
                
        #case3 - 2 children
        
        elif self.current.left and self.current.right :
            if self.current == self.root :
                temp_left = self.current.left
                self.change_node = self.current.right
                self.change_node_parent = self.current.right
                stack = []
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    stack.append(self.change_node_parent)
                    self.change_node = self.change_node.left
                self.root = self.change_node
                last = self.change_node.right
                while stack :
                    node = stack.pop()
                    node.left = last
                    last = node
                self.root.left = temp_left
                self.root.right = last
                
            elif self.current.data < self.parent.data :
                temp_left = self.current.left
                self.change_node = self.current.right
                self.change_node_parent = self.current.right
                stack = []
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    stack.append(self.change_node_parent)
                    self.change_node = self.change_node.left
                self.parent.left = self.change_node
                last = self.change_node.right
                while stack :
                    node = stack.pop()
                    node.left = last
                    last = node
                self.parent.left.left = temp_left
                self.parent.left.right = last
            
            elif self.current.data >= self.parent.data :
                temp_left = self.current.left
                self.change_node = self.current.right
                self.change_node_parent = self.current.right
                stack = []
                while self.change_node.left != None :
                    self.change_node_parent = self.change_node
                    stack.append(self.change_node_parent)
                    self.change_node = self.change_node.left
                self.parent.right = self.change_node
                last = self.change_node.right
                while stack :
                    node = stack.pop()
                    node.left = last
                    last = node
                self.parent.right.left = temp_left
                self.parent.right.right = last

                    
    def pre_order_traversal(self) :
        def _pre_order_traversal(root) :
            if root == None :
                pass
            else :
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
        
    def in_order_traversal(self) :
        def _in_order_traversal(root) :
            if root == None :
                pass
            else :
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)
        
    def post_order_traversal(self) :
        def _post_order_traversal(root) :
            if root == None :
                pass
            else :
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)
