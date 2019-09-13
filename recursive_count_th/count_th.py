'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count=0):
    
    # word of length (n)
    # must utilize recursion
    #slice off 1 letter at a time until len <= 1
    # sum of th

    if len(word) <= 1:
        return 0
    
    elif word[:2] == 'th':
        count += 1
        count += count_th(word[1:])

    else:
        count += count_th(word[1:])

    
    return count