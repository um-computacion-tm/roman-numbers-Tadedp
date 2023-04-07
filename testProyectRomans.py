import unittest
from romanToDecimal import romanToDecimal
from decimalToRoman import decimalToRoman

class TestDecimalToRoman(unittest.TestCase):
    #Test romanos a decimales.
    def test_I(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('I')
        
        #Verificación:
        self.assertEqual(resultado, 1)
    
    def test_II(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('II')
        
        #Verificación:
        self.assertEqual(resultado, 2)
    
    def test_IV(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('IV')
        
        #Verificación:
        self.assertEqual(resultado, 4)
    
    def test_V(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('V')
        
        #Verificación:
        self.assertEqual(resultado, 5)
    
    def test_VIII(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('VIII')
        
        #Verificación:
        self.assertEqual(resultado, 8)
    
    def test_IX(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('IX')
        
        #Verificación:
        self.assertEqual(resultado, 9)
    
    def test_X(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('X')
        
        #Verificación:
        self.assertEqual(resultado, 10)
    
    def test_XXV(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('XXV')
        
        #Verificación:
        self.assertEqual(resultado, 25)
    
    def test_XLVIII(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('XLVIII')
        
        #Verificación:
        self.assertEqual(resultado, 48)
    
    def test_L(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('L')
        
        #Verificación:
        self.assertEqual(resultado, 50)
    
    def test_LXXXVII(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('LXXXVII')
        
        #Verificación:
        self.assertEqual(resultado, 87)        
    
    def test_C(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('C')
        
        #Verificación:
        self.assertEqual(resultado, 100)
    
    def test_CCXXI(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('CCXXI')
        
        #Verificación:
        self.assertEqual(resultado, 221)
    
    def test_D(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('D')
        
        #Verificación:
        self.assertEqual(resultado, 500)
    
    def test_DCLIV(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('DCLIV')
        
        #Verificación:
        self.assertEqual(resultado, 654)
    
    def test_CMXCIX(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('CMXCIX')
        
        #Verificación:
        self.assertEqual(resultado, 999)
    
    def test_M(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = romanToDecimal('M')
        
        #Verificación:
        self.assertEqual(resultado, 1000)
        
    #Tests decimales a romanos.
    def test_1(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(1)
        
        #Verificación:
        self.assertEqual(resultado, 'I')  
    
    def test_2(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(2)
        
        #Verificación:
        self.assertEqual(resultado, "II")
        
    def test_4(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(4)
        
        #Verificación:
        self.assertEqual(resultado, "IV")           
    
    def test_5(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(5)
        
        #Verificación:
        self.assertEqual(resultado, 'V')      
        
    def test_10(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(10)
        
        #Verificación:
        self.assertEqual(resultado, 'X')
        
    def test_25(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(25)
        
        #Verificación:
        self.assertEqual(resultado, "XXV")   
    
    def test_48(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(48)
        
        #Verificación:
        self.assertEqual(resultado, "XLVIII")   
        
    def test_50(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(50)
        
        #Verificación:
        self.assertEqual(resultado, 'L') 
    
    def test_87(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(87)
        
        #Verificación:
        self.assertEqual(resultado, "LXXXVII") 
    
    def test_100(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(100)
        
        #Verificación:
        self.assertEqual(resultado, 'C')

    def test_221(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(221)
        
        #Verificación:
        self.assertEqual(resultado, "CCXXI")

    def test_500(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(500)
        
        #Verificación:
        self.assertEqual(resultado, 'D')
        
    def test_654(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(654)
        
        #Verificación:
        self.assertEqual(resultado, "DCLIV")   
         
    def test_999(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(999)
        
        #Verificación:
        self.assertEqual(resultado, "CMXCIX")      
               
    def test_1000(self):
        #Pre-condición:
        ### NO HAY ### 
        
        #Proceso:
        resultado = decimalToRoman(1000)
        
        #Verificación:
        self.assertEqual(resultado, 'M')   
        
if __name__ == '__main__':
    unittest.main()