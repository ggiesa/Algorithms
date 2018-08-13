
class SNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return repr(self.value)



class DNode:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return repr(self.value)



class SLinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        nodes = []
        curr = self.head

        while curr:
            nodes.append(curr)
            curr = curr.next_node
        return repr(nodes)


    def prepend(self, value):
        self.head = SNode(value, next_node = self.head)


    def append(self, value):
        if not self.head:
            self.head = SNode(value)
            return

        curr = self.head
        while curr.next_node:
            curr = curr.next_node

        curr.next_node = SNode(value)


    def find(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return curr.value
            curr = curr.next_node

        return False


    def remove(self, value):
        curr = self.head
        if curr.value == value:
            self.head = curr.next_node
            return

        next = curr.next_node
        while next:
            if next.value == value:
                curr.next_node = next.next_node
                return
            curr = curr.next_node
            next = next.next_node

        raise KeyError('Value not found in list')


    def reverse(self):
        curr = self.head
        prev = None
        next = None

        while curr:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next

        self.head = prev



class DLinkedList:
    def __init__(self):
        self.tail = DNode(None)
        self.head = DNode(None)
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            # if curr != self.head and curr != self.tail:
            nodes.append(curr)
            curr = curr.next_node

        return repr(nodes)

    def prepend(self, value):
        self.head.next_node = DNode(value, next_node = self.head.next_node,
                                           prev_node = self.head)

    def append(self, value):
        prev = self.tail.prev_node
        prev.next_node = DNode(value, next_node = self.tail,
                                      prev_node = self.tail.prev_node)
        self.tail.prev_node = prev.next_node


    def remove(self, key):
        raise NotImplemented('2nd node string remove doesnt work')
        
        curr = self.head
        prev = None
        next = None

        while curr:
            if curr.value == key:
                prev.next_node = next
                next.prev_node = prev

                # curr.prev_node = curr.next_node
                # curr.next_node = curr.prev_node
                return
            curr = curr.next_node
            prev = curr.prev_node
            next = curr.next_node
