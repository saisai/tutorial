def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    print('left')
    merge_sort(array, left_index, middle)
    print('right')
    merge_sort(array, middle + 1, right_index)
    print(list(array))
    print(left_index)
    print(right_index)
    print(middle)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    print('merge')
    # make copies of both arrays we're trying to merge

    # the second paramerter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index: middle+1]
    right_copy = array[middle+1:right_index+1]

    print(left_copy)
    print(right_copy)

    # initial values for variables that we use to keep
    # track of where we are in each array

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy ( by incresing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1


        # regardless of where we got our elements from
        # move forward in the sorted part
        sorted_index = sorted_index + 1
    print(array)
    # we ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array) - 1)
print(array)


# https://stackabuse.com/merge-sort-in-python/
