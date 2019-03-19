def bubble_sort(items):
    out = items.copy() # in place protection on items
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

    '''Return array of items, sorted in ascending order'''

def merge_sort(items):
    def merge(A, B):
        list1 = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                list1.append(A[0])
                A.pop(0)
            else:
                list1.append(B[0])
                B.pop(0)

        if len(A) == 0:
            list1 = list1 + B
        if len(B) == 0:
            list1 = list1 + A

        return list1

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i_1 = merge_sort(items[:mid_point])
    i_2 = merge_sort(items[mid_point:])

    return merge(i_1, i_2)
    '''Return array of items, sorted in ascending order'''

def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        return quick_sort([x for x in items[1:] if x < items[0]]) + \
               [items[0]] + \
               quick_sort([x for x in items[1:] if x >= items[0]])


    '''Return array of items, sorted in ascending order'''
