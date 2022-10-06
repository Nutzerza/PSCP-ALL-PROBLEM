"""funcwithin"""

def func_f(num):
    """cal f"""
    return 2*num

def func_g(num):
    """cal g"""
    return (3*(num**4))-(num**3)+(2*num**2)+10

def func_h(numx, numy, numz):
    """cal h"""
    return ((numz+numx)**2)-(numx*numy)+(numy**2)

def func_i(numa, numb, numc, numd):
    """cal i"""
    return (numa**2 + numb**2 - numc**2)/(numd**2 - 2*numa*numd + 2*numa)

def main(numa, numb, numc, numd):
    """print ans"""
    print(func_f(func_f(numa)))
    print(func_g(func_f(numa-numb)))
    print(func_h(func_f(numa+numb), func_f(numa+numc), func_g(func_f(numd**2))))
    print(func_i(func_h(func_f(numa+numb), func_f(numa-numc), func_g(func_f(numd**2)))\
        , func_g(func_f(numa-numb)), func_f(func_f(func_f(func_f(func_f(numc))))), numd**8))
main(float(input()), float(input()), float(input()), float(input()))
