def main():
    p1, p2 = map(float, input().split())
    porcentagem = 100
    porcentagem += p1*porcentagem/100
    porcentagem += (p2*porcentagem/100)-100
    
    print(f'{porcentagem:.6f}')
    
main()
