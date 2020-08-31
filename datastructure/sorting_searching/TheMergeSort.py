
def mergeSort(alist, param="left"):
    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        print(param)
        mergeSort(lefthalf, "left")
        mergeSort(righthalf, "right")



        i=0
        j=0
        k=0
        print('down ', param)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


# https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
