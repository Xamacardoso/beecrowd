def main():
    n = str(input())
    ultimo = 0
    malasuerte = False
    for item in n:
        if ultimo == '1' and item == '3':
            print(f'{n} es de Mala Suerte')
            malasuerte = True
            break
        else:
            ultimo = item
    
    if malasuerte == False:
        print(f'{n} NO es de Mala Suerte')
        
    
main()
