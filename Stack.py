
class Stack:
    def __init__(self,text,lists=[]):
        self.text=text
        self.lists=lists
        
        
        
    def inserting(self):
        for i in self.text:
            self.lists.append(i)
        return self.lists
            


    def reverse_output(self):
        rlist=[]
        for i in range(len(self.lists)):
            rlist.append(self.lists.pop())
        return rlist
             

r1=Stack("Hello")
r1.inserting()
print(r1.reverse_output())






# 
# stack=[]
# text='Hello'
# 
# for i in text:
#     stack.append(i)
# print (stack)
# 
# 
# for j in range(len(stack)):
#     s=stack.pop()
#     print(s,end='')

