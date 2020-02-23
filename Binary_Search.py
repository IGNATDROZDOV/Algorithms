def binary_searcher(number, massive):
    massive.sort()
    left = massive[0]
    right = len(massive) - 1 
    while left <= right:
        mid = (left + right)//2
        guess = massive[mid]
        if guess == number:
            return mid 
        elif  guess < number:
            left = mid + 1
        else:
            right = mid - 1
    return None

