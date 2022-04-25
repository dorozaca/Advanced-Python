def myname(numero):
    
    def repeticion(string):
        assert type(string)==str, "Solo puedes utilizar strings"
        return (string * numero)

    return repeticion

def run():
    # Diego=myname(5)
    # print(Diego('Toto '))
    Diego=myname(5)('Toto ')
    print(Diego)

if __name__ == '__main__':
    run()