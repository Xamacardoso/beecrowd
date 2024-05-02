def main():
    n = int(input())
    lista = []
    for i in range(0,n):
        num = int(input())
        lista.append(num)
    
    for item in range(len(lista)):
        print(f'resposta {item+1}: {lista[item]}')
    
main()