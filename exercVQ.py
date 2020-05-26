#Faz um pgm que diz qual tipo de triangle it is.

def triangle(a,b,c):
    if a == b and a == c : 
        return 'equilatero'

    elif a == b and a!=c or a == c and a != b or b == c and b!= a :
        return 'isosceles'
    
    else:
        return 'escaleno'

d = int(input('qual a medida do lado1?'))
e = int(input('qual a medida do lado2?'))
f = int(input('qual a medida do lado3?'))

tipo_triang = triangle(d,e,f)
area_triang = area(d,e,f)
print(tipo_triang)

