# def count_positives_sum_negatives(arr):
#     if not arr or None:
#         return []
#     list_pos = [x for x in arr if x >= 0]
#     list_neg = [x for x in arr if x < 0]

#     # print(sum(list_pos))
#     # print(sum(list_neg))
#     list1 = [len(list_pos),sum(list_neg)]
#     print(list1)

# arr = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15
# count_positives_sum_negatives(arr)

# def count_positives_sum_negatives(arr):
#     if not arr:
#         return []
#     plus = []
#     minus = []

#     for x in arr:
#         if x > 0:
#             plus.append(x)
#         elif x < 0:
#             minus.append(x)


#     list1 =[len(plus),sum(minus)]
#     print (list1)
    
    


# arr = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15
# count_positives_sum_negatives(arr)

def count_positives_sum_negatives(arr):
    if not arr or None:
        return []
    list_pos = [x for x in arr if x > 0]
    list_neg = [x for x in arr if x < 0]
    list1 = [len(list_pos),sum(list_neg)]
    return list1