def main():
    dic = {
        'zero':'0',
        'um': '1',
        'dois': '2',
        'tres': '3',
        'quatro': '4',
        'cinco': '5',
        'seis': '6',
        'sete': '7',
        'oito': '8',
        'nove': '9',
    }
    
    entrada = input()
    if len(entrada) == 1:
        for valor in dic.items():
            if entrada == valor[1]:
                print(valor[0])
                break
            
    else:
        for valor in dic.keys():
            if valor == entrada:
                print(dic[valor])
                break
        
    
main()
