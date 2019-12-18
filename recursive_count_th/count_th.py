'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences
of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Plan 1:
    # Base case should be if a word is < 2, if so, return 0
    # Will not count capitalized TH
    # then...basically go through each of the letters (two at a time)
    # looking for a paired 'th'
    # if one is found, add to the count
    # if there isn't any, and nothing to the count

    if len(word) < 2:
        return 0
    elif word[:2] == "th":
        return 1 + count_th(word[1:])
        print("********", word[1:])
    else:
        return 0 + count_th(word[1:])
    
    pass

print(count_th(""))
print(count_th("thTHthTHthTH"))