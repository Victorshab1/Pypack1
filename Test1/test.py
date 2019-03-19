from Pypack1 import recursion

def sum_array():
    """
    make sure sum_array correctly
    """

    assert recursion.sum_array([1,2,3,4]) == 10, 'correct'
def fibonacci():
    """
    make sure fibonacci correctly
    """
    assert recursion.fibonacci(10) ==89, 'correct'
def factorial():
    """
    make sure factorial correctly
    """
    assert recursion.factorial(5) == 120, 'correct'

def reverse():
    """
    make sure reverse works correctly
    """
    assert recursion.reverse('victor') == rotciv, 'correct'

from Pypack1 import sorting

def bubble_sort():
    """
    make bubble_sort works correctly
    """
    assert recursion.bubble_sort([1,2,3,4]) == [1,2,3,4], 'correct'

def merge_sort():
    """
    make merge_sort works correctly
    """
    assert recursion.merge_sort([1,2,3,4]) == [1,2,3,4], 'correct'

def quick_sort():
    """
    make quick_sort works correctly
    """
    assert recursion.quick_sort([1,2,3,4]) == [1,2,3,4], 'correct'
