from collections import Counter

l = [1, 1, 1, 1, 12, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
countL = Counter(l)
print(countL)

s = 'lskdjfasdlfksj'
countS = Counter(s)
print(countS)

w = 'Hello how are you? you?'.split()
countW = Counter(w)
print(countW)

commonW = countW.most_common()
print(commonW)

common1 = countW.most_common(1)
print(common1)