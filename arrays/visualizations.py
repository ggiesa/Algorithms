import sys
import ctypes
from math import log
import numpy as np
import matplotlib.pyplot as plt
from arrays.data_structures import DynamicArray
plt.style.use('bmh')


def algo_complexity():
    '''Plot relative runtime vs. algorithmic complexity for some common
        complexities.'''

    n = np.linspace(1,10,1000)
    demo = {
        'Constant':np.ones(n.shape),
        'Logarithmic':np.log(n),
        'Linear':n,
        'Loglinear':n*np.log(n),
        'Quadratic':n**2,
        'Cubic':n**3,
        'Exponential':2**n
        }

    fig = plt.figure(figsize=(12,10))

    plt.ylim(0,50)
    plt.xlabel('N')
    plt.ylabel('Relative Runtime')
    plt.title('Big O complexity')

    for label, f in demo.items():
        plt.plot(n, f, label=label)

    plt.legend(loc=0)
    return fig


def list_length_viz(n):
    '''Print the length of the a growing list with the amount of memory
        it takes up.'''
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        data.append(i)
        print(f'Length: {a}, Size in bytes: {b}')


def visualize_DynamicArray(n):
    '''Print the length of the a growing list and the amount of memory
        it takes up.'''
    data = DynamicArray()
    for i in range(n):
        a = len(data)
        b = ctypes.sizeof(data.A)
        data.append(i)
        print(f'Length: {a}, Size in bytes: {b}')
