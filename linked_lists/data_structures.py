
class SNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class DNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = DNode(1)
b = DNode(2)
c = DNode(3)

a.next_node = b

b.next_node = c
b.prev_node = a

c.prev_node = b
