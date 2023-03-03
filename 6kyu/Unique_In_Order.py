# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of
# elements.


def unique_in_order(sequence):
    letter = None
    order = []
    for i in sequence:

        if letter == i:
            continue
        letter = i
        order.append(letter)

    return order


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))

# better ideas


# from itertools import groupby
#
# def unique_in_order(iterable):
#     return [k for (k, _) in groupby(iterable)]
# --------------------------------------------------------------------------------------

# def unique_in_order(iterable):
#     return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
