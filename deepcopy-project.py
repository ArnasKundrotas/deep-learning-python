import copy

a = {'q':1, 'w':2}
b = a
print('a --> ' + str(id(a)))
print('b --> ' + str(id(b)))
b = copy.deepcopy(a)

print('Deep copy ---------------')
print('a --> ' + str(id(a)))
print('b --> ' + str(id(b)))
