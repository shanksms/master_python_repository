
import builtins
import collections
# Shadow input with a global name
input = 42
pylookup = collections.ChainMap(locals(), globals(), vars(builtins))

#Retrive input from global namespace
print(pylookup['input'])

#remove input from global namespace
del globals()['input']

#retrive from builtin namespace
print(pylookup['input'])
