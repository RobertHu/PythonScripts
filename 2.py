def fib(n):
    result = []
    a , b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


def ask_ok(prompt, retries=4,complaint='yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print(complaint)




def f(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L




def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    


def function(a):
    pass

function(0,a=0)
