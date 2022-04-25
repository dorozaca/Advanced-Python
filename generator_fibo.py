import time
def fibo_generator():
    
    counter=0
    n1=0
    n2=1
    
    while True: #ESTE WHILE ES CLAVE PARA QUE SE IMPRIMA LA SECUENCIA
        if counter==0:
            counter+=1
            yield n1

        elif counter==1:
            counter+=1
            yield n2

        else:
            counter +=1
            aux=n1 + n2
            n1, n2 = n2, aux
            yield aux


if __name__== '__main__':
    fibo=fibo_generator()
    for i in fibo:
        print(i)
        time.sleep(.05) #ESTA ES LA FRACCIN DE SEGUNDO


