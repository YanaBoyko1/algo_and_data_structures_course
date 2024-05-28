def sorted_numbers(num):
    n = len(num)
    for i in range(n - 1):
        for j in range(0, n - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


def find_k_largest(num, k):
    if len(num) < k:
        return "Розмір масиву менший за k"

    sorted_nums = sorted_numbers(num)
    k_largest = sorted_nums[-k]
    position = num[::-1].index(k_largest)
    return k_largest, position


num = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3
result = find_k_largest(num, k)
k_largest, position = result
print(f"Знайдений {k}-й найбільший елемент: {k_largest}")
print(f"Позиція {k}-го найбільшого елемента в масиві: {position}")
print(sorted_numbers(num))
print(result)
