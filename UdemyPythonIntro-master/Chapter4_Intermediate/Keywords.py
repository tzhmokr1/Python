# break, continue, pass, None

l1 = [1, 2, 3, 4, 5]

for val in l1:
    if val > 3:
        break
    print(val)


print("")


for val in l1:
    if val % 2 == 0:
        continue
    print(val)


def print_list(l1):
    pass    # Platzhalterwert, um Funktion schon mal leer zu definieren


print_list(l1)


print("")


val1 = None # Patzhalterwert für Variable
print(val1)
