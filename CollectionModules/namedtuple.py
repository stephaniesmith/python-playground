from collections import namedtuple

Dog = namedtuple('Dog', 'age bread name')
sam = Dog(2, 'Lab', 'Sam')
print(sam)
print(sam.name)