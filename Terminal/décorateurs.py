import time


def mafonction(x):
    return x ** 2

t0 = time.time_ns()
sortie = mafonction(2)
t1 = time.time_ns()
print((t1 - t0) * 1e-9 )
print(sortie)