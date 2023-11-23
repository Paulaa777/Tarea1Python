import unittest
import fibo

class Test(unittest.TestCase):
    def testCinco(self):
       
        mensaxe="Test Incorrecto Fibo Posición 5 Resultado 3"
        
        self.assertEqual(fibo.position(5),3,mensaxe)
        self.assertNotEqual(fibo.fibonacci(5),3,mensaxe)
        #self.assertEqual(fibo.fibonacci(5),3,mensaxe)


if __name__=='__main__':
    Test()
    #unittest.main()
