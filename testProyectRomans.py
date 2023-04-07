import unittest
from romanToDecimal import romanToDecimal
from decimalToRoman import decimalToRoman

class TestDecimalToRoman(unittest.TestCase):
    
    def test_I(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('I')
        
        #verificacion
        self.assertEqual(resultado, 1)
    
    def test_II(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('II')
        
        #verificacion
        self.assertEqual(resultado, 2)
    
    def test_IV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('IV')
        
        #verificacion
        self.assertEqual(resultado, 4)
    
    def test_V(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('V')
        
        #verificacion
        self.assertEqual(resultado, 5)
    
    def test_VIII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('VIII')
        
        #verificacion
        self.assertEqual(resultado, 8)
    
    def test_IX(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('IX')
        
        #verificacion
        self.assertEqual(resultado, 9)
    
    def test_X(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('X')
        
        #verificacion
        self.assertEqual(resultado, 10)
    
    def test_XXV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('XXV')
        
        #verificacion
        self.assertEqual(resultado, 25)
    
    def test_XLVIII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('XLVIII')
        
        #verificacion
        self.assertEqual(resultado, 48)
    
    def test_L(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('L')
        
        #verificacion
        self.assertEqual(resultado, 50)
    
    def test_LXXXVII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('LXXXVII')
        
        #verificacion
        self.assertEqual(resultado, 87)        
    
    def test_C(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('C')
        
        #verificacion
        self.assertEqual(resultado, 100)
    
    def test_CCXXI(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('CCXXI')
        
        #verificacion
        self.assertEqual(resultado, 221)
    
    def test_D(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('D')
        
        #verificacion
        self.assertEqual(resultado, 500)
    
    def test_DCLIV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('DCLIV')
        
        #verificacion
        self.assertEqual(resultado, 654)
    
    def test_CMXCIX(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('CMXCIX')
        
        #verificacion
        self.assertEqual(resultado, 999)
    
    def test_M(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = romanToDecimal('M')
        
        #verificacion
        self.assertEqual(resultado, 1000)
    def test_1(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(1)
        
        #verificacion
        self.assertEqual(resultado, 'I')  
    
    def test_2(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(2)
        
        #verificacion
        self.assertEqual(resultado, "II")
        
    def test_4(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(4)
        
        #verificacion
        self.assertEqual(resultado, "IV")           
    
    def test_5(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(5)
        
        #verificacion
        self.assertEqual(resultado, 'V')      
        
    def test_10(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(10)
        
        #verificacion
        self.assertEqual(resultado, 'X')
        
    def test_25(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(25)
        
        #verificacion
        self.assertEqual(resultado, "XXV")   
    
    def test_48(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(48)
        
        #verificacion
        self.assertEqual(resultado, "XLVIII")   
        
    def test_50(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(50)
        
        #verificacion
        self.assertEqual(resultado, 'L') 
    
    def test_87(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(87)
        
        #verificacion
        self.assertEqual(resultado, "LXXXVII") 
    
    def test_100(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(100)
        
        #verificacion
        self.assertEqual(resultado, 'C')

    def test_221(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(221)
        
        #verificacion
        self.assertEqual(resultado, "CCXXI")

    def test_500(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(500)
        
        #verificacion
        self.assertEqual(resultado, 'D')
        
    def test_654(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(654)
        
        #verificacion
        self.assertEqual(resultado, "DCLIV")   
         
    def test_999(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(999)
        
        #verificacion
        self.assertEqual(resultado, "CMXCIX")      
               
    def test_1000(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimalToRoman(1000)
        
        #verificacion
        self.assertEqual(resultado, 'M')   
        
if __name__ == '__main__':
    unittest.main()