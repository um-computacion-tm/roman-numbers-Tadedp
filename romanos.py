import unittest

def decimal_to_roman(decimal):
    resultado = ""
    
    if decimal <= 0:
        return ""
    
    elif decimal == 1000:
        return 'M'
    
    else:    
        if decimal < 10:
            resultado = convert(decimal,0) 
        elif decimal < 100 and decimal >= 10:
            resultado = convert(decimal%10,0)
            resultado = convert(decimal//10,1) + resultado
        else:
            resultado = convert((decimal%100)%10,0)
            resultado = convert((decimal%100)//10,1) + resultado
            resultado = convert(decimal//100,2) + resultado
    
    return resultado
        
 
def convert(decimal, decimalPart):
    decimalPart = decimalPart * 2  
    datos = ['I','V','X','L','C','D','M']
    
    if decimal == 0:
        return ""  
    
    elif decimal <= 3:
        return datos[decimalPart] * decimal
    
    elif decimal == 4:
        return datos[decimalPart] + datos[decimalPart + 1]
    
    elif decimal == 5:
        return datos[decimalPart + 1]
    
    elif decimal <= 8:
        return datos[decimalPart + 1] + datos[decimalPart] * (decimal - 5)       
    
    elif decimal == 9:
        return datos[decimalPart] + datos[decimalPart + 2]    

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(1)
        
        #verificacion
        self.assertEqual(resultado, 'I')  
    
    def test_2(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(2)
        
        #verificacion
        self.assertEqual(resultado, "II")
        
    def test_4(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(4)
        
        #verificacion
        self.assertEqual(resultado, "IV")           
    
    def test_5(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(5)
        
        #verificacion
        self.assertEqual(resultado, 'V')      
        
    def test_10(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(10)
        
        #verificacion
        self.assertEqual(resultado, 'X')
        
    def test_25(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(25)
        
        #verificacion
        self.assertEqual(resultado, "XXV")   
    
    def test_48(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(48)
        
        #verificacion
        self.assertEqual(resultado, "XLVIII")   
        
    def test_50(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(50)
        
        #verificacion
        self.assertEqual(resultado, 'L') 
    
    def test_87(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(87)
        
        #verificacion
        self.assertEqual(resultado, "LXXXVII") 
    
    def test_100(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(100)
        
        #verificacion
        self.assertEqual(resultado, 'C')

    def test_221(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(221)
        
        #verificacion
        self.assertEqual(resultado, "CCXXI")

    def test_500(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(500)
        
        #verificacion
        self.assertEqual(resultado, 'D')
        
    def test_654(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(654)
        
        #verificacion
        self.assertEqual(resultado, "DCLIV")   
         
    def test_999(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(999)
        
        #verificacion
        self.assertEqual(resultado, "CMXCIX")      
               
    def test_1000(self):
        #pre condion
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(1000)
        
        #verificacion
        self.assertEqual(resultado, 'M')   
        
if __name__ == '__main__':
    unittest.main()
    
        