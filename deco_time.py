from datetime import datetime

def exec_time(func):
    def wrapper(*args, **kwargs):
        initial_time=datetime.now()
        func(*args, **kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print(f'Pasaron {str(time_elapsed.total_seconds())} segundos')

    return wrapper

@exec_time
def random_func():
    for _ in range(1,1000000): #IMPORTANTE CUANDO QUEREMOS USAR UN LOOP PERO NO NOS IMPORTAN LOS VALORES QUE ITERAN
        pass

@exec_time
def suma(a: int, b: int) -> int:
    return a + b

@exec_time
def saludo (nombre='Diego'):
    print(f'Hola {nombre}!')

if __name__== '__main__':
    random_func()
    suma(5,7)
    saludo()