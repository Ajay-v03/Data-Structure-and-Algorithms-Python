'''Bubble sort --> technique in which all 0th index element check all elements in array one by one,
and swap if element is greater or less than with them'''

from sqlalchemy import true


def bubble_sort(elements):
    size = len(elements)

    swap = False #Flag for checking if it's already sorted array we traverse only one time in array
    for i in range(size-1):
        for j in range(size-1-i): #-i here defines already sorted elements, we don't need to traverse again
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swap = True

        if not swap:
            break

if __name__ == "__main__":
    elements = [2,5,1,3,56,23,45,67]
    elements = [1,2,3,4,2]
    bubble_sort(elements)
    print(elements)