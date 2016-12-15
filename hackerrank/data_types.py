def use_list_methods():
    '''
    The challenge was to take the various list methods as raw input and 
    use them to manioulate a list.

    One popular solution was eval(), which can be dangerous because
    it allows running of raw code on a system. I chose the getattr()
    function because it runs more directly the particular attributes of
    the list (or other functions) without the associated dangers.
    '''
    N = int(input())
    lst = []
    
    for _ in range(N):
        command = input().split()
        if command[0] == 'print':
            print(lst)
        else:
            getattr(lst, command[0])(*map(int, command[1:]))
