def count_positives_sum_negatives(arr):
    count = summ = 0
    if arr:
        for num in arr:
            if num > 0:
                count += 1
            elif num < 0:
                summ += num
        return [count, summ]
    else:
        return []
