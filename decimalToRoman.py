def decimalToRoman(decimal):
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
        
if __name__ == '__main__':
    pass