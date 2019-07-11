#  Let A be an array of size n≥2 containing integers from 1 to n−1 inclusive, one of which is repeated.
#  Describe an algorithm for ﬁnding the integer in A that is repeated.
def getRepeated(array):
    s = sum(array)
    return s - len(array) * (len(array) - 1) / 2


print(getRepeated([1, 1, 2]))

# Let B be an array of size n≥6 containing integers from 1 to n−5 inclusive, ﬁve of which are repeated.
# Describe an algorithm for ﬁnding the ﬁve integers in B that are repeated.
def getRepeated2(array):
    arr2 = [0] * (len(array) - 5)
    result = []
    for i in array:
        if arr2[i - 1] != i:
            arr2[i - 1] = i
        else:
            result.append(i)
            print(i)
    return result


getRepeated2([1, 1, 2, 3, 3, 4, 5, 5, 4, 6, 6])
