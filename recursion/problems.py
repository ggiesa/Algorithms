from nose.tools import assert_equal
from time import time

def timer(msg, function, args, iterations=500):
    t = time()
    for i in range(iterations):
        function(args)
    print(msg, time()-t)


def rec_sum_prob():

    def rec_sum(n):
        '''
        Write a recursive function which takes an integer and computes
        the cumulative sum of 0 to that integer
        '''
        if n == 0:
            return 0
        else:
            return n + rec_sum(n-1)

    def test_rec_sum(solution):
        assert_equal(solution(5), 15)
        assert_equal(solution(4), 10)
        assert_equal(solution(10), 55)


        print('All tests passed')

    test_rec_sum(rec_sum)



def sum_func_prob():

    def sum_func(n):
        '''
        Given an integer, create a function which returns the sum of all
        the individual digits in that integer.

            - For example: if n = 4321, return 4+3+2+1
        '''
        if n < 10:
            return n%10
        else:
            return n%10 + sum_func(n//10)


    def test_sum_func(solution):
        assert_equal(solution(12345), 15)
        assert_equal(solution(1111), 4)
        assert_equal(solution(567), 18)

        print('All tests passed')

    test_sum_func(sum_func)



def word_split_prob():

    def word_split(phrase, dictionary, output=None):
        '''
        Create a function called word_split() which takes in a string phrase
        and a set list_of_words. The function will then determine if it is
        possible to split the string in a way in which words can be made from
        the list of words. You can assume the phrase will only contain words
        found in the dictionary if it is completely splittable
        '''

        if output is None:
            output = []

        for word in dictionary:
            if phrase.startswith(word):
                output.append(word)
                return word_split(phrase[len(word):], dictionary, output = output)
        return output


    def test_word_split(solution):
        assert_equal(solution('themanran',['the','ran','man']),
                     ['the', 'man', 'ran'])
        assert_equal(solution('ilovedogsJohn',['i','am','a','dogs','lover','love','John']),
                     ['i', 'love', 'dogs', 'John'])
        assert_equal(solution('themanran',['clown','ran','man']),
                     [])

        print('All tests passed')

    test_word_split(word_split)



def reverse_string_prob():
    '''
    Reverse a string using recursion.
    '''

    def reverse(string):
        length = len(string)
        if not length:
            return ''
        return string[length-1] + reverse(string[:length-1])


    def test_reverse(solution):
        assert_equal(solution('hello'),'olleh')
        assert_equal(solution('hello world'),'dlrow olleh')
        assert_equal(solution('123456789'),'987654321')

        print('Passed all test cases.')

    # Run Tests
    test_reverse(reverse)



def string_permutation_prob():
    '''
    Given a string, write a function that uses recursion to output a list of
    all the possible permutations of that string.

    For example, given s='abc' the function should return:
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    If a character is repeated, treat each occurence as distinct, for example
    an input of 'xxx' would return a list with 6 "versions" of 'xxx'
    '''

    def permute(string):
        ret = []
        if len(string) == 1:
            ret = [string]

        for ind, letter in enumerate(string):
            for permutation in permute(string[:ind] + string[ind+1:]):
                ret.append(letter + permutation)

        return ret

    def test_permute(solution):
        assert_equal(sorted(solution('abc')),
                     sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),
                     sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']))

        print('Passed all test cases.')

    # Run Tests
    test_permute(permute)



def fibonnaci_prob():
    '''
    Implement a Fibonnaci Sequence in three different ways:

        - Recursively
        - Dynamically (Using Memoization to store results)
        - Iteratively

    '''

    def fib_i(n):
        '''Solved iteratively.'''
        if n <= 1:
            return 1

        ret = [0,1]
        for i in range(n-1):
            ret.append(ret[-2] + ret[-1])

        return ret[-1]

    def fib_r(n):
        '''Solved recursively.'''
        if n <= 1:
            if n == 0:
                return 0
            return 1

        return fib_r(n-1)+fib_r(n-2)


    class Memoize:
        def __init__(self, f):
            self.f = f





            self.cache = {}
        def __call__(self, *args):
            if args not in self.cache:
                self.cache[args] = self.f(*args)
            return self.cache[args]

    @Memoize
    def fib_m(n):
        '''Solved recursively.'''
        if n <= 1:
            if n == 0:
                return 0
            return 1

        return fib_m(n-1)+fib_m(n-2)


    def test_fibonnaci(solution, prnt=False):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)

        if prnt:
            print('Passed all test cases.')

    # Run Tests
    timer('Iteratively: ', test_fibonnaci, fib_i)
    timer('Recursively: ', test_fibonnaci, fib_r)
    timer('Recursively with mem: ', test_fibonnaci, fib_m)

fibonnaci_prob()
