class Node:
    def __init__(self,data):
        self.left_node = None
        self.right_node = None
        self.data = data
    def insert_node(self,data):
        if self.data:
            if data < self.data:
                if self.left_node == None:
                    self.left_node = Node(data)
                else:
                    self.left_node.insert_node(data)
            elif data > self.data:
                if self.right_node == None:
                    self.right_node = Node(data)
                else:
                    self.right_node.insert_node(data)
        else:
            self.data = data
    def find_val(self,val):
        if val < self.data:
            if self.left_node == None:
               return str(val) + " Value not found"
            else:
                return  self.left_node.find_val(val)
        elif val > self.data:
            if self.right_node == None:
               return str(val) + " Value not found"
            else:
                return  self.right_node.find_val(val)
        else:
            return str(self.data) + " value is found"

    def lowest_common_ancester(self,n1,n2):
        if self.data>max(n1,n2):
            return self.left_node.lowest_common_ancester(n1,n2)
        elif self.data<min(n1,n2):
            return self.right_node.lowest_common_ancester(n1, n2)
        else:
            return self.data

    def print_tree(self):
        if self.left_node:
            self.left_node.print_tree()
        print(self.data),
        if self.right_node:
            self.right_node.print_tree()

root = Node(5)
root.insert_node(4)
root.insert_node(6)
root.insert_node(7)
root.insert_node(8)
print(root.find_val(7))
print(root.find_val(14))
print(root.lowest_common_ancester(7,8))

