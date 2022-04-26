# def Noduplicados(lista):
#     nuevaLista=[]
#     for i in lista:
#         if i not in nuevaLista:
#             nuevaLista.append(i)

#     return nuevaLista

def Noduplicados(lista):
    nuevoSet=set(lista)
    nuevaLista=list(nuevoSet)
    return nuevaLista



if __name__ == '__main__':
    listaPrueba=[2,2,4,4,55,5,5,66,55,7,7,7,7]
    print(Noduplicados(listaPrueba))

 