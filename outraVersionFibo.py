#Outra versión do programa pedido
def fibonacci_prueba(n):

    try:
        n=int(n)  
        
        if n <= 0:
                print("Sorry!!!, A Posición debe ser un Número Maior de Cero")
        else:
            
            result = []
            a, b = 0, 1

            while a < n:

                result.append(a)    
                a, b = b, a+b

            return result[-1]     
         
    except ValueError:
        print("ERRO na Posición Introducida!!!")

if __name__ == '__main__':
    print(fibonacci_prueba(n=(input("Introduce unha Posición:"))))  
