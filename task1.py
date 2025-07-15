def find_min_max(arr):
    # Базовий випадок: один елемент
    if len(arr) == 1:
        return (arr[0], arr[0])

    # Базовий випадок: два елементи
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))

    # Рекурсивний випадок
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return (min(left_min, right_min), max(left_max, right_max))

# Приклад використання
arr = [7, 2, 9, 4, 1, 10, 5, -3 , 5, -6, 3]
print(find_min_max(arr))  # (-6, 10)
