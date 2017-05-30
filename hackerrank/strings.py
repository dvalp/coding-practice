from collections import Counter


def print_formatted(number):
    '''
    The challenege was to print each number up to (including) the given integer
    in several number formats, with padding to match the length of the largest 
    binary version of the number.

    The interesting point here is that you can insert variables pointers into
    other variable pointers. Here I used them to insert a padding width into 
    each column of the table.
    '''
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print('{0:{fill}d} {0:{fill}o} {0:{fill}X} {0:{fill}b}'.format(i, fill=width))

def is_palindrome(s):
    '''
    The challenge is to discover whether a list of characters has any permutation 
    which is also an anagram. Calculating and comparing all permutations of long 
    strings is expensive.

    The solution requires understanding that in any palindrome no more than one 
    character can appear an odd number of times. Here I used a counter to simplify
    counting the number of times a character appeared.
    '''
    if sum([v % 2 for v in Counter(s).values()]) <= 1:
        return 'YES'
    return 'NO'

