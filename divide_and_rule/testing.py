'''    def run(self):
        a, b = 0, 1
        for _ in xrange(self):
            yield a
            a, b = b, a + b

    print list(run(a))

a = int(raw_input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b

print fib(a)

def fib(n):
    cur = 1
    old = 1
    i = 1
    while (i < n):
        cur, old, i = cur+old, cur, i+1
    return cur

for i in range(10):
    print(fib(i))
'''
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
