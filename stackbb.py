class arrstack:
    def __init__(self):
        self.data=[]
    def len(self):
        return(len(self.data))
    def isempty(self):
        return len(self.data)==0
    def push(self,e):
        self.data.append(e)
    def pop(self):
        if self.isempty():
            raise Empty("stack is empty")
        return self.data.pop()
    def top(self):
        if self.isempty():
            raise Empty("stack is empty")
        return self.data[-1]
st=arrstack()
st.push(5)
print(st.len())
print(st.top())
print(st.pop())
print(st.len())
print(st.pop())
