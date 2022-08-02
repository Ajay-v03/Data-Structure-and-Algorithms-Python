'''Merge sort implementation using new array'''
# insertion_sort + selection_sort = merge_sort (.sort() function in python)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    sorted_list = [] #new array to store sorted elements

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

if __name__ == '__main__':
    arr = [10,3,15,7,8,23,98,29]

    print(merge_sort(arr))