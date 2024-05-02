def verificar_triangulo(a,b,c):
    if a >= b+c:
        print('NAO FORMA TRIANGULO')
    else:
        if a**2 == b**2 + c**2:
            print('TRIANGULO RETANGULO')
        elif a**2 > b**2 + c**2:
            print('TRIANGULO OBTUSANGULO')
            if a == b and b == c:
                print('TRIANGULO EQUILATERO')
            elif (a==b and b!= c) or (b==c and c!=a) or (a==c and c!=b):
                print('TRIANGULO ISOSCELES')
        elif a**2 < b**2 + c**2:
            print('TRIANGULO ACUTANGULO')
            if a == b and b == c:
                print('TRIANGULO EQUILATERO')
            elif (a==b and b!= c) or (b==c and c!=a) or (a==c and c!=b):
                print('TRIANGULO ISOSCELES')
                
def maior3(a,b,c):
    v1,v2,v3 = a,b,c
    maior = v1
    if v2 > maior:
        maior = v2
        v2 = a
    if v3 > maior:
        maior = v3
        v2 = b
        v3 = a    
    
    return (maior,v2,v3)
    
def main():
    a,b,c = map(float, input().split())
    valores = maior3(a,b,c)
    verificar_triangulo(valores[0], valores[1], valores[2])
    


main()