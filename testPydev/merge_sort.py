def merge_srot(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_srot(left)
        merge_srot(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                k += 1
                i += 1
            else:
                array[k] = right[j]
                k += 1
                j += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    print array

merge_srot([7,1,3,4])
