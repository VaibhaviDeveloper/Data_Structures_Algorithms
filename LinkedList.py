class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

head=None
def insertAtTop(data):
  global head
  nn=Node(data)
  if head is None:
    head=nn
  else:
    nn.next=head
    head=nn

def traverse():
  curr=head
  while curr is not None:
    print(curr.data)
    curr=curr.next

insertAtTop(10)
insertAtTop(20)
insertAtTop(30)
 # traverse()

def insertAtEnd(data):
  global head
  nn=Node(data)
  if head is None:
    head=nn
  else:
    curr=head
    while curr.next is not None:
      curr=curr.next
    curr.next=nn

insertAtEnd(40)
#traverse()

def insertAtPos(data,pos):
  global head
  nn = Node(data)
  if head is None:
    head=nn
  elif pos==0:
    nn.next=head
    head=nn
  else:
    curr=head
    i=0
    while (i<pos-1 and curr is not None and curr.next is not None):
      curr=curr.next
      i+=1
    nn.next=curr.next
    curr.next=nn

insertAtPos(20,1)
insertAtPos(90,0)
insertAtPos(100,100)
insertAtPos(100,0)
traverse()

    
     