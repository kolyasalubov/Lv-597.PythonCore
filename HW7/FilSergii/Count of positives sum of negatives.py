def count_positives_sum_negatives(arr):
    return_list = [0, 0]
    for item in arr:
        if item > 0:
            return_list[0] += 1
        else:
            return_list[1] += item
    if return_list[0] == 0 and return_list[1] == 0:
        return arr[:2]
    else:
        return return_list

