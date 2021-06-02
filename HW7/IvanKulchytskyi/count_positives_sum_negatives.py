def count_positives_sum_negatives(arr):
    if not len(arr):
        return []
    return [len(list(1 for num in arr if num > 0)), sum(num for num in arr if num < 0)]
