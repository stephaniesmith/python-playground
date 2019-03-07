from collections import Counter

l = [1, 1, 1, 1, 12, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5]
count_l = Counter(l)
print(count_l)

s = 'lskdjfasdlfksj'
count_s = Counter(s)
print(count_s)

w = 'Hello how are you? you?'.split()
count_w = Counter(w)
print(count_w)

common_w = count_w.most_common()
print(common_w)

common_1 = count_w.most_common(1)
print(common_1)