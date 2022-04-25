def decorador(func):
    def wrapper(*args):
        print('Esto se agrega a mi funcion original')
        func(*args)
    return wrapper

def saludo():
    print('Hola')

saludo()
saludo=decorador(saludo) #En cuanto se crea una funcion se tiende a decorarla automaticamente, pero de la forma mas pythonica con @
saludo()


#@decorador
#def saludo():
#   print('Hola')

#saludo()