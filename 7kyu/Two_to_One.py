# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest
# possible, containing distinct letters - each taken only once - coming from s1 or s2.
def sortedANDremoved(a):
    a = sorted(a)
    maped_a = []
    doplicate = None
    for i in a:
        if doplicate == i:
            continue
        maped_a.append(i)
        doplicate = i

    return maped_a


def longest(a1, a2):
    total = sortedANDremoved(a1) + sortedANDremoved(a2)
    return ''.join(map(str, sortedANDremoved(total)))


print(longest("aretheyhere", "yestheyarehere"))
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print(longest("inmanylanguages", "theresapairoffunctions"))



# better ideas

# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))