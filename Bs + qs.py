def quicksort(array):
    if len(array)<2:
        return array
    else:
        reference_element = array[0]
        less = [i for i in array[1:] if i<=reference_element]
        greater = [i for i in array[1:] if i>reference_element]
        return quicksort(less) + [reference_element] + quicksort(greater)


def binary_searcher(array, number):
    arr = quicksort(array)
    left_border = 0
    right_border = len(arr) - 1
    while left_border <= right_border:
        mid =(right_border + left_border)//2
        guess = arr[mid]
        if guess == number:
            return mid
        elif guess < number:
            left_border = mid + 1
        elif guess > number:
            right_border = mid - 1
    return None 