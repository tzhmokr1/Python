# 1: Zahl mit Nachkommastellen
x = 100/7
y = 2/7
print("Zahlen:")
print(x, y)
print()

2# 2: Format f
print("Format f")
print("{0:12.2f} {1:30.2f}".format(x,y))
print("{0:12.2f} {1:30.2f}".format(x,y))
print()

# 3: Format e
print("Format e")
print("{0:e}".format(x))
print("{0:12.3e}".format(x))
print("{0:.3e}".format(x))
print()

# 4: Format %
print("Format %")
print("{0:%}".format(y))
print("{0:12.3%}".format(y))
print("{0:.3%}".format(y))
