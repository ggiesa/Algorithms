from nose.tools import assert_equal

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
