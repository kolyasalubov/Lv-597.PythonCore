def count_positives_sum_negatives(arr):
    count_pos = 0
    sum_neg = 0
    if len(arr) == 0:
        return []
    elif len(arr) == 1 and arr[0] > 0:
        return [arr[0], 0]
    elif len(arr) == 1 and arr[0] < 0:
        return [0, arr[0]]
    else: 
        for i in arr:
            if i > 0:
                count_pos += 1
            elif i < 0:
                sum_neg += i
        return [count_pos, sum_neg]