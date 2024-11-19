def min_max(numbers):
    if not numbers:  
        return None
    return (min(numbers), max(numbers))


result = min_max([4, 2, 8, 6])
print(result)  