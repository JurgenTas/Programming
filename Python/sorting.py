__author__ = 'J Tas'

'''
Insertion sort is a simple sorting algorithm that builds
the final sorted array (or list) one item at a time. When humans
manually sort something (for example, a deck of playing cards),
most use a method that is similar to insertion sort.

see: http://en.wikipedia.org/wiki/Insertion_sort
'''


def insertion_sort(arr):

    for i in range(len(arr)):
        val = arr[i]
        for j in range(0, i):
            if val < arr[j]:
                val, arr[j] = arr[j], val
        arr[i] = val

'''
Selection sort is a sorting algorithm, specifically an
in-place comparison sort. It has O(n2) time complexity,
making it inefficient on large lists, and generally performs
worse than the similar insertion sort.

see: http://en.wikipedia.org/wiki/Selection_sort
'''


def selection_sort(arr):

    for i in range(len(arr)):
        val = arr[i]
        index=i
        for n in range(i, len(arr)):
            if arr[n] < val:
                val = arr[n]
                index = n
                arr[index] = arr[i]
            arr[i] = val

'''
The idea is to arrange the list of elements so that, starting
anywhere, considering every hth element gives a sorted list.
Such a list is said to be h-sorted.
'''


def hsort(arr, h):

    for i, el in enumerate(arr):
        while i >= h and arr[i - h] > el:
            arr[i] = arr[i - h]
            i -= h
        arr[i] = el

'''
a binary search will start by examining the middle item.
If that item is the one we are searching for, we are done.
If it is not the correct item, we can use the ordered nature
of the list to eliminate half of the remaining items.
'''


def binary_search(arr, item):

    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found


def main():

    import numpy
    arr = numpy.arange(500)
    numpy.random.shuffle(arr)
    print(arr)
    insertion_sort(arr)
    print(arr)

    print(binary_search(arr, 13))

if __name__ == "__main__":
    main()
