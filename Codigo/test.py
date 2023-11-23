import unittest
import fibo

class Test(unittest.TestCase):

   

    def testCincoPosicionEqual(self):
       
        #Test assertEqual función position 
        self.assertEqual(fibo.position(5),3,"Test Incorrecto Función POSITION 5 Resultado !=3")
       
    def testCincoFibonacciNotEqual(self):
       
       #Test assertEqual funcion fibonacci position 
        self.assertNotEqual(fibo.fibonacci(5),3,"Test Incorrecto Función POSITION 5 Resultado !=3")
        

    def testCincoFibonacciEqual(self):
       
        #Test assertEqual función fibonacci 
        self.assertEqual(fibo.fibonacci(5),3,"Test Incorrecto Función FIBO 5 Resultado !=3")


if __name__=='__main__':
    Test()
    #unittest.main()
