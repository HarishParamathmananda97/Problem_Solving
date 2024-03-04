# import textwrap

def wrap1(string, max_width):
    # printing on screen
    for index, letter in enumerate(string):
        if (index + 1) % max_width == 0:
            print(letter)
        else:
            print(letter, end='')
    return

def wrap2(string, max_width):
    # using list
    wrapped_text = []
    temp  = []
    for index, letter in enumerate(string):
        temp.append(letter)
        if (index + 1) % max_width == 0:
            # print(letter)
            wrapped_text.append(''.join(temp))
            temp = []
    if temp != []:
        wrapped_text.append(''.join(temp))
    return wrapped_text


def wrap(string, max_width):

    docstring_text = """"""
    for index, letter in enumerate(string):
        if (index + 1) % max_width == 0:
            docstring_text += f"{letter}\n"
        else:
            docstring_text += letter
    return docstring_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    # string, max_width = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',4
    result = wrap(string, max_width)
    print(result)



"""
sample input: 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4
sample output: 
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
"""