# Tuplas não podem ter seus elementos alterados ao contrario das listas
# Tuplas são inicializadas com parenteses ()

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

tuple = ('abcd', 786, 2.23, 'john', 70.2)
list = ['abcd', 786, 2.23, 'john', 70.2]
tuple[2] = 1000 #error
list[2] = 1000
