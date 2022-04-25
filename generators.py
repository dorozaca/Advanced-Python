


def my_gen():
    """
        Un ejemplo de generadores
    """

    print('Hello World')
    n=0
    yield n
    
    print('Hello Heaven')
    n=1
    yield n
    
    print('Hello Loco')
    n=2
    yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) 