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

insertAtTop("A")
insertAtTop("B")
insertAtTop("C")
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

insertAtEnd("Q")
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

def deleteAtTop():
  global head
  if head is not Node:
    head=head.next

def deleteAtEnd():
  global head
  if (head is not None and head.next is None):
    head=None
  elif (head is not None and head.next is not None):
    curr=head
    while (curr is not None and curr.next is not None and curr.next.next is not None):
      curr=curr.next
    curr.next=None


insertAtPos("D",1)
insertAtPos("E",0)
insertAtPos("F",100)
insertAtPos("G",0)
deleteAtTop()
deleteAtTop()
deleteAtEnd()
deleteAtEnd()
traverse()

    
     