def eh_multiplo(x,y):
    return x%y == 0 or y%x == 0



def main():
    x, y = map(int,input().split())
    
    if eh_multiplo(x,y):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
      
        
main()