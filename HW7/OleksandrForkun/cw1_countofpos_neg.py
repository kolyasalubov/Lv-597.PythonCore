def count_positives_sum_negatives(arr):
    count = 0
    summa = 0
    if arr:
        for num in arr:
            if num > 0:
                count += 1
            elif num < 0:
                summa += num
        return [count, summa]
    else:
        return []
