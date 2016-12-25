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
