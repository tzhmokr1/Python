import math

# Zwei Funktionen
def mw1(a,b):
    c = (a+b)/2
    return c

def mw2(a,b):
    c = math.sqrt(a*b)
    return c

# exec
for i in 1,2:
    t = "print(mw" + str(i) + "(3,4))"
    exec(t)

