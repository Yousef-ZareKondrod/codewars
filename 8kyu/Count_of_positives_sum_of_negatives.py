# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum
# of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
#
def count_positives_sum_negatives(arr):
    cont = 0
    sum = 0
    if arr == []:
        return []
    for i in arr:
        if i > 0:
            cont += 1
        else:
            sum += i

    return [cont, sum]


def basic_test_cases():
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  # ,[10,-65]
    print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))  # ,[8,-50]
    print(count_positives_sum_negatives([1]))  # ,[1,0]
    print(count_positives_sum_negatives([-1]))  # ,[0,-1]
    print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))  # ,[0,0]
    print(count_positives_sum_negatives([]))  # ,[]


basic_test_cases()

# better ideas


# def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []


# def count_positives_sum_negatives(arr):
#     return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []
