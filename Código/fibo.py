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
    
#Temos en conta que Función Fibonacci previa conta os indices dende Cero coma un array
#Para facer coincidir a Posición co Indice creo Función no que gardamos en array a secuencia e mostramos a posición requerida
def position(p=int(input("Introduce unha Posición:"))):
  
    if p <= 0:
        print("Sorry!!!, La Posición debe ser un Número Mayor que Cero")
    else:
        posicion=[fibonacci(n) for n in range(p)]
        return print ("Para la Posición", p, "el Número es:", posicion[-1])
       

#chamamos o programa principal

if __name__ == '__main__':
    #print(position())
    position()