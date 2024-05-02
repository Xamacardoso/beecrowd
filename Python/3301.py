def main():
    h,z,l = list(map(int, input().split()))
    listapura = [h,z,l]
    lista = sorted([h,z,l])
    meio = lista[1]
    if listapura[0] == meio:
        print('huguinho')
    elif listapura[1] == meio:
        print('zezinho')
    elif listapura[2] == meio:
        print('luisinho')
        
        
        
main()