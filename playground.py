import itertools

words = 'these are a bunch of words'.split()
print(words[:])

values = [1, 2, 3, 4]
dicts = [{'key1': 'value', 'key2': 2},
         {'key1': 'value2', 'key2': 3, 'key3': (1, 2, 3)}]
my_gen = (d['key1'] for d in dicts)
for g in my_gen:
    print(g)

square = (i*i for i in range(100))
bounded_square = itertools.takewhile(lambda x: x < 20, square)
lowerbound_square = itertools.dropwhile(lambda x: x < 40, square)

print(list(map(lambda x: x * 2, [1, 2, 3])))
print([2*x for x in [1, 2, 3]])
print(list(dicts[1].keys()))