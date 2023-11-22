"""
 Números da secuencia de Fibonacci corresponden á suma das duas secuencias previas 
 Definimos previamente os dous primeiros números f0 e f1 e sempre e cando n >= 2 quedan definidos pola seguinte ecuación:
"""
#f0=0 , f1=1 , fn=fn−1+fn−2

def fibonacci(n=int(input("Introduce unha Posición:"))):

  
    if n < 0:
        print("Sorry!!!, La Posición debe ser un Número Mayor que Cero")
    
    elif n == 0:   
            
        return n
       
    elif n == 1:
        return n
        
    elif n >= 2:
        return ((fibonacci(n - 1) + fibonacci(n - 2)))
   
#chamamos á función
# a ter en conta que as posicións comenzan en cero 

if __name__ == '__main__':
        print(fibonacci())
   
 