from nose.tools import assert_equal


def implement_deque():
    '''
    Implement a Deque class. It should be able to do the following:

        - Check if its empty
        - Add to both front and rear
        - Remove from Front and Rear
        - Check the Size
    '''

    class Deque:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def size(self):
            return len(self.items)

        def addFront(self, item):
            self.items.append(item)

        def addRear(self, item):
            self.items.insert(0,item)

        def removeFront(self):
            self.items.pop()

        def removeRear(self):
            self.items.pop(0)


    def test_deque():
        d = Deque()
        assert_equal(d.isEmpty(), True)
        assert_equal(d.size(), 0)

        d.addFront(1)
        d.addRear(0)
        assert_equal(d.items[0], 0)
        assert_equal(d.items[1], 1)
        assert_equal(d.isEmpty(), False)
        assert_equal(d.size(), 2)

        d.removeRear()
        assert_equal(d.items[0], 1)
        d.removeFront()
        assert_equal(d.size(),0)

        print('All test cases passed')

    test_deque()


def implement_queue():
    '''
    Implement a Queue class. The class should be able to do the following:

        - Check if Queue is Empty
        - Enqueue
        - Dequeue
        - Return the size of the Queue
    '''

    class Queue:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def size(self):
            return len(self.items)

        def enqueue(self, item):
            self.items.insert(0,item)

        def dequeue(self):
            return self.items.pop()


    def test_queue():
        q = Queue()
        assert_equal(q.isEmpty(), True)
        assert_equal(q.size(), 0)

        q.enqueue(1)
        assert_equal(q.items[0], 1)
        q.enqueue(2)
        assert_equal(q.items[0], 2)
        q.enqueue(3)
        assert_equal(q.items[0], 3)
        q.enqueue(4)
        assert_equal(q.items[0], 4)

        q.dequeue()
        assert_equal(q.items[0], 4)
        q.dequeue()
        assert_equal(q.items[0], 4)
        q.dequeue()
        assert_equal(q.items[0], 4)
        q.dequeue()

        assert_equal(q.isEmpty(), True)
        assert_equal(q.size(), 0)

        print('All test cases passed')

    test_queue()


def implement_stack():
    '''
    Implement a Stack.

    It should have the methods:

        - Check if its empty
        - Push a new item
        - Pop an item
        - Peek at the top item
        - Return the size
    '''

    class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def size(self):
            return len(self.items)

        def pop(self):
            return self.items.pop()

        def push(self, item):
            self.items.append(item)

        def peek(self):
            return self.items[-1]

    def test_stack():
        s = Stack()
        assert_equal(s.isEmpty(), True)
        assert_equal(s.size(), 0)

        s.push(1)
        assert_equal(s.items[-1], 1)
        s.push(2)
        assert_equal(s.items[-1], 2)
        s.push(3)
        assert_equal(s.items[-1], 3)
        s.push(4)
        assert_equal(s.items[-1], 4)

        s.pop()
        s.pop()
        s.pop()
        s.pop()

        assert_equal(s.isEmpty(), True)
        assert_equal(s.size(), 0)

        print('All test cases passed')

    test_stack()
