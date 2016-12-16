def count_valid_parens(parens = '()()(()(())'):
    '''
    The challenge is to count the length of the longest set 
    of valid (opened and closed) parentheses in a string.

    Use an array to keep track of the state at each closing
    parenthesis and count back as needed to find the full
    number of validly closed parentheses.
    '''

    state = []
    
    for i, p in enumerate(parens):
        if p == '(':
            state.append(0)
        else:
            if state[i-1] == 0:
                state.append(2 + state[i - 2])
            else:
                if parens[i - state[i - 1] - 1] == '(':
                    state.append(2 + state[i - 1] + state[state[i - 1] - 1])
                else:
                    state.append(0)

    return max(state)
