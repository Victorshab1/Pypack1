def sum_array(array):
    total = 0
    for i in array:
        total +=i
    return total

    '''Return sum of all items in array'''

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

    '''Return nth term in fibonacci sequence'''

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

    '''Return n!'''

def reverse(word):
    str = ""
    for i in word:
        str = i + str
    return str

    '''Return word in reverse'''
