def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    new_items = items.copy()
    for i in range(len(new_items)):
        for j in range(len(new_items)-1-i):
            if new_items[j] > new_items[j+1]:
                new_items[j], new_items[j+1] = new_items[j+1], new_items[j]

    return new_items


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    my_len = len(items)
    if my_len == 1:
        return items

    mid = int(my_len / 2)
    l1 = merge_sort(items[:mid])
    l2 = merge_sort(items[mid:])

    new_list = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            new_list.append(l1[0])
            l1.pop(0)
        else:
            new_list.append(l2[0])
            l2.pop(0)

    if len(l1) == 0:
        new_list = new_list + l2
    if len(l2) == 0:
        new_list = new_list + l1

    return new_list


def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

     mylen = len(items)

    if mylen <= 1:
        return items

    pivot = items[-1]
    small = []
    large = []
    same = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            same.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + same + large
