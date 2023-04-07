import unittest

def decimal_to_roman(decimal):
    #Cadena que contendrá al número romano final
    resultado = ""

    #Verificación de la validez del número   
    if decimal <= 0 or decimal > 1000:
        return ""
    
    else:
        #Cada iteración transforma una cifra del número de derecha a izquierda
        for i in range(0,4):
            if decimal >= 10**i:
                resultado = convertirDecimal((decimal % 10**(i+1)) // 10**i, i) + resultado 
            else:
                break
                
    return resultado
        
#Recibe una cifra y su posición en el número original
#Devuelve el número romano correspondiente a la cifra
def convertirDecimal(decimal, puntero):
    #Ajuste de la variable así apunta a los valores del vector acordes a la posición de la cifra 
    puntero = puntero * 2  
    romanos = ['I','V','X','L','C','D','M']

    #Salida del número romano   
    if decimal == 0:
        return ""  
    
    elif decimal <= 3:
        return romanos[puntero] * decimal
    
    elif decimal == 4:
        return romanos[puntero] + romanos[puntero + 1]
    
    elif decimal == 5:
        return romanos[puntero + 1]
    
    elif decimal <= 8:
        return romanos[puntero + 1] + (romanos[puntero] * (decimal - 5))       
    
    else:
        return romanos[puntero] + romanos[puntero + 2]    

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(1)
        
        #verificacion
        self.assertEqual(resultado, 'I')  
    
    def test_2(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(2)
        
        #verificacion
        self.assertEqual(resultado, "II")
        
    def test_4(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(4)
        
        #verificacion
        self.assertEqual(resultado, "IV")           
    
    def test_5(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(5)
        
        #verificacion
        self.assertEqual(resultado, 'V')      
        
    def test_10(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(10)
        
        #verificacion
        self.assertEqual(resultado, 'X')
        
    def test_25(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(25)
        
        #verificacion
        self.assertEqual(resultado, "XXV")   
    
    def test_48(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(48)
        
        #verificacion
        self.assertEqual(resultado, "XLVIII")   
        
    def test_50(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(50)
        
        #verificacion
        self.assertEqual(resultado, 'L') 
    
    def test_87(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(87)
        
        #verificacion
        self.assertEqual(resultado, "LXXXVII") 
    
    def test_100(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(100)
        
        #verificacion
        self.assertEqual(resultado, 'C')

    def test_221(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(221)
        
        #verificacion
        self.assertEqual(resultado, "CCXXI")

    def test_500(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(500)
        
        #verificacion
        self.assertEqual(resultado, 'D')
        
    def test_654(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(654)
        
        #verificacion
        self.assertEqual(resultado, "DCLIV")   
         
    def test_999(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(999)
        
        #verificacion
        self.assertEqual(resultado, "CMXCIX")      
               
    def test_1000(self):
        #pre condición
        ### NO HAY ### 
        
        #proceso
        resultado = decimal_to_roman(1000)
        
        #verificacion
        self.assertEqual(resultado, 'M')   
        
if __name__ == '__main__':
    unittest.main()
    
        