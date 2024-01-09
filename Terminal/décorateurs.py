import time

def temps(affichage):    
    def _temps(f):
        def g(*args):
            t0 = time.time_ns()
            sortie = f(*args)
            t1 = time.time_ns()
            if affichage:
                print((t1 - t0) * 1e-9 )
            return sortie
        
        return g
    if affichage:
        return _temps
    else:
        return lambda f: f
    
    
@temps(False)
def mafonction(x):
    return x ** 2

sortie = mafonction(2)
print(sortie)