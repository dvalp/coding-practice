def print_to_N():
    '''
    The challenge was to write a function that could take a given integer 
    and print all the numbers leading up to it without any spaces.

    Two interesting things are happening here. First, the '*' is unpacking 
    the generator created by range and passing the elements individually. 
    Second, I find it interesting that you can tell print how to separate 
    the elements, and in this case not separate them at all.
    '''

    N = int(input())
    print(*range(1, N + 1), sep='')
