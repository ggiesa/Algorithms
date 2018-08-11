from nose.tools import assert_equal
from copy import copy
from collections import defaultdict
from time import time

def anagram_problem():
    '''
    Given two strings, check to see if they are anagrams.
    An anagram is when the two strings can be written using the exact same
    letters.

    Example:

    "public relations" is an anagram of "crap built on lies."

    "clint eastwood" is an anagram of "old west action"
    '''

    # Solution 1
    def anagram1(s1, s2):

        s1 = s1.lower()
        s2 = s2.lower()
        s1 = [i for i in s1 if i != ' ']
        s2 = [i for i in s2 if i != ' ']

        # Edge case
        if len(s1) != len(s2):
            return False

        for i in s1:
            if i in s2:
                s2.remove(i)
        return False if s2 else True

    # Solution 2
    def anagram2(s1, s2):
        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()

        return sorted(s1) == sorted(s2)

    # Solution 3
    def anagram3(s1, s2):
        s1 = s1.replace(' ', '').lower()
        s2 = s2.replace(' ', '').lower()

        # Edge case
        if len(s1) != len(s2):
            return False

        count = {}
        for letter in s1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in s2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for value in count.values():
            if value:
                return False

        return True


    def anagram_test(sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

    # Run Tests
    anagram_test(anagram1)
    anagram_test(anagram2)
    anagram_test(anagram3)


def pair_sum_problem():

    '''
    Given an integer array, output all the unique pairs that sum up to a
    specific value k.

    Example:

        pair_sum([1,3,2,2],4)

        would return 2 pairs:

        (1,3)
        (2,2)
    '''

    # Soltion 1
    def pair_sum1(array, k):
        count = 0
        unique = []
        for i, value1 in enumerate(array):
            for value2 in array[i+1:]:
                if value1 + value2 == k:
                    if (value1,value2) not in unique:
                        if (value2,value1) not in unique:
                            count+=1
                            unique.append((value1, value2))
        return count

    def pair_sum2(array,k):

        # Edge Case
        if len(array) < 2:
            return 0

        # Sets for tracking
        seen = set()
        count = 0

        for num in array:
            target = k-num
            if target in array:
                 if (num, target) not in seen:
                    count+=1
                    seen.add((target,num))
                    seen.add((num,target))

        return count



    class TestPair(object):

        def test(self,sol):
            assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
            assert_equal(sol([1,2,3,1],3),1)
            assert_equal(sol([1,3,2,2],4),2)
            print('ALL TEST CASES PASSED')

    #Run tests
    t = TestPair()
    t.test(pair_sum1)
    t.test(pair_sum2)




def find_mising_element():
    '''
    Consider an array of non-negative integers. A second array is formed by
    shuffling the elements of the first array and deleting a random element.
    Given these two arrays, find which element is missing in the second array.

    Example:

        The first array is shuffled and the number 5 is
    removed to construct the second array.

    Input:

    finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

    Output:

    5 is the missing number
    '''

    def solution1(array1, array2):
        # Brute force, O(n^2)

        result = copy(array1)
        for element in array1:
            if element in array2:
                result.remove(element)
                array2.remove(element)
        return result[0]


    def solution2(array1, array2):
        # O(nlog(n))

        array1.sort()
        array2.sort()

        for i, el in enumerate(array1):
            if array2[i] != array1[i]:
                return el


    def solution3(array1, array2):
        # O(n)

        d = defaultdict(int)

        for num in array2:
            d[num] += 1

        for num in array1:
            d[num] -= 1
            if d[num] < 0:
                return num


    def solution4(array1, array2):
        # O(n), constant space complexity
        result = 0
        for num in array1+array2:
            result ^= num
        return result


    class TestFinder(object):

        def test(self,sol):
            assert_equal(sol([5,5,7,7],[5,7,7]),5)
            assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
            assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
            print('ALL TEST CASES PASSED')

    # Run test
    t = TestFinder()
    t.test(solution1)
    t.test(solution2)
    t.test(solution3)
    t.test(solution4)



def largest_continuous_sum():
    '''
    Given an array of integers (positive and negative), find the
    largest continuous sum.
    '''

    def solution1(array):
        # O(n)

        if len(array) == 0:
            return 0

        maximum = minimum = array[0]
        for num in array:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num

        if maximum <= 0:
            return maximum
        elif minimum >= 0:
            return sum(array)


        for i, _ in enumerate(array):
            a = sum(array[i:])
            b = sum(array[:i])
            if a > maximum:
                maximum = a
            if b > maximum:
                maximum = b

        return maximum


    def solution2(array):
        # O(n)

        if len(array) == 0:
            return 0

        max_sum = current_sum = array[0]
        for num in array[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum


    class LargeContTest(object):
        def test(self,sol):
            assert_equal(sol([1,2,-1,3,4,-1]),9)
            assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
            assert_equal(sol([-1,1]),1)
            assert_equal(sol([-10,-10,-10,1,2,3,4,5]), 15)
            assert_equal(sol([]),0)
            assert_equal(sol([1,2,3,4,5]), sum([1,2,3,4,5]))
            assert_equal(sol([-1,-2,-4]), -1)
            assert_equal(sol([1]), 1)
            assert_equal(sol([0]), 0)

            print('ALL TEST CASES PASSED')

    #Run Test
    t = LargeContTest()
    t.test(solution1)
    t.test(solution2)
