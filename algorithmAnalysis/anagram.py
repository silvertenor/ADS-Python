# one string is an anagram of another if the second is a rearrangement of the first (heart and earth)


# 1st solution - "checking off"
# HORRIBLY INEFFICIENT
# O(n^2) runtime
def anagramSolution1(s1, s2):
    stillOk = True

    if len(s1) != len(s2):
        stillOk = False

    aList = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(aList) and not found:
            if s1[pos1] == aList[pos2]:
                found = True
            else:
                pos2 += 1
        
        if found:
            aList[pos2] = None
        else:
            stillOk = False
        pos1 += 1
    return stillOk


# 2nd solution - "Sort and Compare"
# Cleaner, but due to sorting still takes O(n^2) or O(nlogn) runtime
def anagramSolution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)

    list1.sort()
    list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if list1[pos] == list2[pos]:
            pos += 1
        else:
            matches = False

    return matches

# 3rd solution - "count and compare"
# O(N) running time - no nested loop!
# requires more memory though
def anagramSolution3(s1, s2):
    # 26 letters in alphabet
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a') # get 'position' of letter in alphabet
        c1[pos] += 1 # increment 'count' of letter

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillOk = True

    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False
    return stillOk

print(anagramSolution1('apple', 'pleap'))
print(anagramSolution1('abcd', 'dcda'))

print(anagramSolution2('apple', 'pleap'))
print(anagramSolution2('abcd', 'dcda'))

print(anagramSolution3('apple', 'pleap'))
print(anagramSolution3('abcd', 'dcda'))