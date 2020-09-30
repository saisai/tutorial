def mergeSort(myList):
    print('mylist len ', len(myList))
    if len(myList) > 1:
        
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # recursive call on each half
        mergeSort(left)
        mergeSort(right)

        print('left')
        print(left)
        print('right')
        print(right)


        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # iterator for the main list
        k = 0
        print('hello')
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # the value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1

            # Move to the next slot
            k += 1

        # For all the remaingin values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)

# https://www.educative.io/edpresso/merge-sort-in-python
