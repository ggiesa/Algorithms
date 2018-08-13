from nose.tools import assert_equal


def cycle_check_prob():
    '''
    Given a singly linked list, write a function which takes in the first node
    in a singly linked list and returns a boolean indicating if the linked
    list contains a "cycle".

    A cycle is when a node's next point actually points back to a previous node
    in the list. This is also sometimes known as a circularly linked list.
    '''

    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None

    def solution1(node):
        # O(n) time, O(n) space

        n = node
        seen = set()
        seen.add(n)

        while n.next_node is not None:
            n = n.next_node

            if n in seen:
                return True
            else:
                seen.add(n)

        return False

    def solution2(node):
        # O(n) time, O(1) space

        cursor1 = cursor2 = node

        while cursor2 != None and cursor2.next_node != None:

            cursor1 = cursor1.next_node
            cursor2 = cursor2.next_node.next_node

            if cursor1 == cursor2:
                return True

        return False


    def test_cycle_check(sol):

        # CYCLE LIST
        a = Node(1)
        b = Node(2)
        c = Node(3)

        a.next_node = b
        b.next_node = c
        c.next_node = a # Cycle Here!

        # NON CYCLE LIST
        x = Node(1)
        y = Node(2)
        z = Node(3)

        x.next_node = y
        y.next_node = z

        assert_equal(sol(a),True)
        assert_equal(sol(x),False)

        print('All test cases passed.')

    test_cycle_check(solution1)
    test_cycle_check(solution2)



def list_reversal_prob():
    '''
    Write a function to reverse a Linked List in place.
    The function will take in the head of the list as input and return
    the new head of the list.
    '''

    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None

    def solution1(head):

        current = head
        previous = None
        next = None

        while current:
            next = current.next_node
            current.next_node = previous
            previous = current
            current = next

    def test_reversal(sol):

        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        f = Node(6)
        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = e
        e.next_node = f

        vals = [
            a.value, a.next_node.value, a.next_node.next_node.value,
            a.next_node.next_node.next_node.value,
            a.next_node.next_node.next_node.next_node.value,
            a.next_node.next_node.next_node.next_node.next_node.value
            ]
        assert_equal(vals, [1,2,3,4,5,6])

        sol(a)
        vals = [
            f.value, f.next_node.value, f.next_node.next_node.value,
            f.next_node.next_node.next_node.value,
            f.next_node.next_node.next_node.next_node.value,
            f.next_node.next_node.next_node.next_node.next_node.value
            ]
        assert_equal(vals, [6,5,4,3,2,1])

        print('Test case passed')

    test_reversal(solution1)



def nth_to_last_prob():
    '''
    Write a function that takes a head node and an integer value n and then
    returns the nth to last node in the linked list.
    '''

    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None

    def solution1(n, head):
        # O(2n)

        length = 1
        node = head
        while node.next_node is not None:
            node = node.next_node
            length += 1

        node = head
        for i in range(length-n):
            node = node.next_node

        return node

    def solution2(n, head):
        # O(n)

        left_node = right_node = head

        for i in range(n-1):
            if right_node.next_node is not None:
                right_node = right_node.next_node
            else:
                raise ValueError('There are fewer than n nodes in the list')

        while right_node.next_node is not None:
            left_node = left_node.next_node
            right_node = right_node.next_node

        return left_node


    def test_nth_to_last(sol):

        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)

        a.next_node = b
        b.next_node = c
        c.next_node = d
        d.next_node = e

        assert_equal(sol(2,a), d)
        print('Test case passed')

    # Run test
    test_nth_to_last(solution1)
    test_nth_to_last(solution2)
