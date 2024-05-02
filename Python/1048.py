def main():
    salario = float(input())
    if salario <= 400:
        percentual = 15
    elif salario <= 800:
        percentual = 12
    elif salario <= 1200:
        percentual = 10
    elif salario <= 2000:
        percentual = 7
    else:
        percentual = 4
        
    print(f'Novo salario: {(salario + (salario*(percentual/100))):.2f}')
    print(f'Reajuste ganho: {(salario*percentual/100):.2f}')
    print(f'Em percentual: {percentual} %')
    
    
main()