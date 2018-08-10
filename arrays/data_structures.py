import ctypes
import sys

class DynamicArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self._make_array(self.capacity)

    def __len__(self):
        '''Return the length of the dynamic array.'''
        return self.n

    def __getitem__(self, k):
        '''Return element k in dynamic array.'''
        if k < 0 or k > self.n-1:
            raise IndexError('K is out of bounds.')
        return self.A[k]

    def append(self, add):
        '''Append a single element to the dynamic array.'''
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = add
        self.n += 1

    def _resize(self, new_capacity):
        '''Extend the amount of memory used for the array.'''
        B = self._make_array(new_capacity)
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()
