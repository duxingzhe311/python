target_path = {"server":["download\\server\\windows\\","..\\..\\Build\\PxPos3.0"],
               "pos":["download\\pos\\windows\\","..\\..\\Build\\PxPos3.0"]}

for k,v in target_path.items():
    print 'k:' , k
    print 'v:' , v

L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
for i in g:
    print i ,

def fib(v):
    n, a, b = 0, 0, 1
    while n < v:
        print(b)
        a, b = b, a + b
        n = n + 1

fib(10)

def fib2(v):
    n, a, b = 0, 0, 1
    while n < v:
        yield b
        a, b = b, a + b
        n += 1

f = fib2(15)
for i in f:
    print i ,