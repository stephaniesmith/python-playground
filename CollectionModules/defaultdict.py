from collections import defaultdict

d = { 'k1': 1 }
k1_val = d['k1']
print(k1_val)

dd = defaultdict(object)
dd['one']
print(dd['one'])

for item in dd:
    print(item)

ddl = defaultdict(lambda: 0)
one_val = ddl['one']
print(one_val)

two_val = ddl['two'] = 2
print(two_val)
