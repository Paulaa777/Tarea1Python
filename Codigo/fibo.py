"""
 Números da secuencia de Fibonacci corresponden á suma das duas secuencias previas 
 Definimos previamente os dous primeiros números f0 e f1 e sempre e cando n >= 2 quedan definidos pola seguinte ecuación:
"""
#f0=0 , f1=1 , fn=fn−1+fn−2

# Defino a Función Fibonacci, xerará a secuencia de modo recursivo
def fibonacci(n):
      
    if n == 0 or n == 1:               
        return n
       
    elif n >= 2:
        return ((fibonacci(n - 1) + fibonacci(n - 2)))

  
#Temos en conta que Función Fibonacci previa conta os indices dende Cero coma un Array
#Para facer coincidir a Posición co Indice creo Función no que gardamos en array a secuencia e mostramos a posición requerida
#def position(p=(input("Introduce unha Posición:"))):  
def position(p):  

    try:
        p=int(p)  
        
        if p <= 0:
            print("Sorry!!!, A Posición debe ser un Número Maior de Cero")
        else:
            posicion=[fibonacci(n) for n in range(p)]
            #return print ("Para la Posición", p, "el Número es:", posicion[-1])
            return posicion[-1]
    except ValueError:
        print("ERRO na Posición Introducida!!!")

#chamamos o programa principal
if __name__ == '__main__':
    
    print(position(p=(input("Introduce unha Posición:"))))  
    #position(p=(input("Introduce unha Posición:")))