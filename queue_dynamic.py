
class dqueue:
    def __init__(self):
        self.data=[]
    def len(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)== 0
    def insertion(self,e):
        self.data.append(e)
    def dqueue(self):
        if self.isempty():
            return ('queue is empty')
        else:
            return self.data.pop(0)

q=dqueue()
q.insertion(3)
q.insertion(4)
q.insertion(5)
print('queue',q.data)

print(q.dqueue())

print('queue',q.data)
print(q.dqueue())
print(q.dqueue())
q.insertion(1)
print('queue',q.data)
print(q.dqueue())