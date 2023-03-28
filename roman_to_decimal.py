import unittest

def roman_to_decimal(roman):
    resultado = 0
    
    for i in range(len(roman)):
        decimal = convertir_romano(roman[i])
        if i != len(roman) - 1:
            decimal_siguiente = convertir_romano(roman[i+1])
        else:
            decimal_siguiente = 0
            
        if decimal < decimal_siguiente:
            resultado = resultado - decimal
        else:
            resultado = resultado + decimal 
    
    return resultado

def convertir_romano(letra):
    if letra == 'I':
        return 1
    elif letra == 'V':
        return 5
    elif letra == 'X':
        return 10
    elif letra == 'L':
        return 50
    elif letra == 'C':
        return 100
    elif letra == 'D':
        return 500
    elif letra == 'M':
        return 1000
    
class TestDecimalToRoman(unittest.TestCase):
    
    def test_I(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('I')
        
        #verificacion
        self.assertEqual(resultado, 1)
    
    def test_II(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('II')
        
        #verificacion
        self.assertEqual(resultado, 2)
    
    def test_IV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('IV')
        
        #verificacion
        self.assertEqual(resultado, 4)
    
    def test_V(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('V')
        
        #verificacion
        self.assertEqual(resultado, 5)
    
    def test_VIII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('VIII')
        
        #verificacion
        self.assertEqual(resultado, 8)
    
    def test_IX(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('IX')
        
        #verificacion
        self.assertEqual(resultado, 9)
    
    def test_X(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('X')
        
        #verificacion
        self.assertEqual(resultado, 10)
    
    def test_XXV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('XXV')
        
        #verificacion
        self.assertEqual(resultado, 25)
    
    def test_XLVIII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('XLVIII')
        
        #verificacion
        self.assertEqual(resultado, 48)
    
    def test_L(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('L')
        
        #verificacion
        self.assertEqual(resultado, 50)
    
    def test_LXXXVII(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('LXXXVII')
        
        #verificacion
        self.assertEqual(resultado, 87)        
    
    def test_C(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('C')
        
        #verificacion
        self.assertEqual(resultado, 100)
    
    def test_CCXXI(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('CCXXI')
        
        #verificacion
        self.assertEqual(resultado, 221)
    
    def test_D(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('D')
        
        #verificacion
        self.assertEqual(resultado, 500)
    
    def test_DCLIV(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('DCLIV')
        
        #verificacion
        self.assertEqual(resultado, 654)
    
    def test_CMXCIX(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('CMXCIX')
        
        #verificacion
        self.assertEqual(resultado, 999)
    
    def test_M(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = roman_to_decimal('M')
        
        #verificacion
        self.assertEqual(resultado, 1000)


        
if __name__ == '__main__':
    unittest.main()
    