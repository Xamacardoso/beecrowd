def main():
    valores_positivos = 0
    for i in range(0,6):
        valor = float(input())
        if valor > 0:
            valores_positivos+=1
    
    print(f'{valores_positivos} valores positivos')
    


main()