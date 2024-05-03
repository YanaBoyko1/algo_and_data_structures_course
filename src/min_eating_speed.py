def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        total_hours = sum((bananas - 1) // mid + 1 for bananas in piles)
        if total_hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left
