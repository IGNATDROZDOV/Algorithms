def qsort(array):
    if len(array) < 2:
        return array
    else:
        reference_element = array[0]
        less = [i for i in array[1:] if i <=  reference_element]
        greater = [i for i in array[1:] if i > reference_element] 
        return qsort(less) + [reference_element] + qsort(greater)


