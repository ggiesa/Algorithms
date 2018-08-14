from nose.tools import assert_equal



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
