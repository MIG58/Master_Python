def add1():
    return (1 + 1)

def add2(x):
    x = x + 1
    return (x)

def add3(x,y):
    return x+y

print("Non-Parameter",add1())
print("Single Parameter",add2(4))
print("Multi Parameter",add3(8,8)) 