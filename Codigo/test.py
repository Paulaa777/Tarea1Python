#importamos o módulo unittest e o noso programa fibo
import unittest
import fibo


class Test(unittest.TestCase):
    
    #función setup prepara entorno probas
    def setUp(self) -> None:
        return super().setUp()
    #función teardown execútase despois de cada setup
    def tearDown(self) -> None:
        return super().tearDown()
          
    #Proba Unitaria de Verificación > Programa fibo mostra na posición 5 o resultado 3
    def testCinco_Position_Equal(self):
       
        #Test assertEqual función position         
        self.assertEqual(fibo.position(5),3,"Test Incorrecto Función POSITION 5 Resultado !=3")

   
    #Proba Unitaria de Verificación > función fibonnacci posición 5 o resultado non é 3
    def testCinco_Fibonacci_NotEqual(self):
       
       #Test assertEqual funcion fibonacci position 
        self.assertNotEqual(fibo.fibonacci(5),3,"Test Incorrecto Función POSITION 5 Resultado !=3")
        
       
    #Proba Unitaria > función fibonnacci posición 5 o resultado es 5
    def testCinco_Fibonacci_Equal(self):
       
        #Test assertEqual función fibonacci 
        self.assertEqual(fibo.fibonacci(5),5,"Test Incorrecto Función FIBO 5 Resultado !=5")
    
    
    def doCleanups(self) -> None:
        return super().doCleanups()
    
if __name__=='__main__':
    #Test()
    unittest.main()
