class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class link_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        new_node=node(data)
        cur=self.head
        while(cur.next!= None):
            cur=cur.next
        cur.next=new_node
    def length1(self):
        cur =self.head
        total=0
        while cur.next!=None:
            
            total =total+1
            cur=cur.next
        return total

    def display(self):
        elem=[]
        cur=self.head
        while cur.next!=None:
            cur=cur.next
            elem.append(cur.data)
        print('all elements in linklist are',elem)
    def get(self,index):
        if index>=self.length1():
            return('index out of range')
        else:
            cur_indx=0
            cur_node=self.head
            while True:
                cur_node=cur_node.next
                if cur_indx==index:
                    return (cur_node.data)
                cur_indx +=1
    def erease(self,index):
        if index>=self.length1():
            return ('not valid index')
        else:
            cur_indx=0
            cur_node=self.head
            while True:
                last_node=cur_node
                cur_node=cur_node.next
                if cur_indx==index:
                    last_node.next=cur_node.next
                    return
                cur_indx +=1
l=link_list()
l.append(10)
l.append(20)
l.display()
print(l.length1())
print(l.get(1))
l.erease(1)
l.display()