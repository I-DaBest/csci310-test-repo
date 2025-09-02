"""
demo


|By : Me
|August 28 2025
"""

def ugugug(words):
    """
    converts a string to all captial
    parameters -
    words : string
    | string to be mad all upperrcase
    returns -
    string
|an uppercase version of words
    """
    return words.upper()

"""
code inside this statement will only run if xalled as a script
"""
if __name__ == "__main__":
    print("goodbye forever")

    mStr = input("enter your test string")
    uStr = ugugug(mStr)
    print(uStr)
    theset = input("give me another string")

    print("every other letter capitalized")
    for n in range(len(theset)):
        if n%2: #odd numbered indexes
            print(theset[n].lower(), end='')
        else:
            print(theset[n].upper(), end='')

    print("every vowel capitalized")
    for letter in theset:
        if letter in 'aeiou':
            print(letter.upper(), end='')
        else:
            print(letter.lower(), end='')

    print("every vowel + y")
    for letter in theset:
        if letter in 'aeiouy':
            print(letter.upper(), end='')
        elif letter in '1234567890':
            print(letter, end='')
        else:
            print(letter.lower(), end='')
    print(theset.upper())
    
    print("only numbers")
    for letter in theset:
        if letter in '1234567890':
            print(letter, end='')
        
"""
idk if that one works
"""