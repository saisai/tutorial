def partition(S, low, high):
    i = (low -1 )
    pivot = S[high]
    for j in range(low, high):
        if S[j] <= pivot:
            i = i + 1
            S[i], S[j] = S[j], S[i]
    S[i+1], S[high] = S[high], S[i+1]
    return (i+1)

def quick_sort(S, low, high):
    if low < high:
        partition_index = partition(S, low, high)
        quick_sort(S, low, partition_index - 1)
        quick_sort(S, partition_index+1, high)

        
    
    

S = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
quick_sort(S, 0, len(S)-1)
print(S)

