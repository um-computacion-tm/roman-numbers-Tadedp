def romanToDecimal(roman):
    resultado = 0
    
    for i in range(len(roman)):
        decimal = convertirRomano(roman[i])
        if i != len(roman) - 1:
            decimal_siguiente = convertirRomano(roman[i+1])
        else:
            decimal_siguiente = 0
            
        if decimal < decimal_siguiente:
            resultado = resultado - decimal
        else:
            resultado = resultado + decimal 
    
    return resultado

def convertirRomano(letra):
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
            
if __name__ == '__main__':
    pass