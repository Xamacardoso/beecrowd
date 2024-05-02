def main():
    valores_positivos = 0
    for i in range(0,5):
        valor = int(input())
        if valor % 2 == 0:
            valores_pares+=1
    
    print(f'{valores_pares} valores positivos')
    


main()