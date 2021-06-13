def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return arr
    final = []
    positive = []
    negative = []
    for i in arr:
        if i > 0:
            positive.append(i)
        if i < 0:
            negative.append(i)
    final.append(len(positive))
    final.append(sum(negative))
    return final