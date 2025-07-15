import random

def quick_select(arr, k):
    if not arr:
        return None

    pivot = random.choice(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivots[0]  # всі елементи у pivots рівні, беремо будь-який
    else:
        return quick_select(highs, k - len(lows) - len(pivots))

# Приклад використання
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(quick_select(arr, k))  # 7 (третій найменший елемент)