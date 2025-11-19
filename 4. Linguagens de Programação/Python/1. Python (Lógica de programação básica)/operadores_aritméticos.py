class operador:
    def __init__(self):
        pass

    def menu(self):
        while True:
            print("OPÇÕES")
            print("1) Calculando o preço total de produtos")
            print("2) Calculando a média de três notas")
            print("3) Convertendo minutos em horas")
            print("4) Exponenciação para crescimento")
            print("5) Sair")

            op = input("escolha uma opcão: (EX: 1,2,3,4)")

            if op == "1": 
                preco_unitario = float(input("Digite o preço unitario:"))
                quantidade = int(input("Qual a quantidade que deseja ?"))
                total = preco_unitario * quantidade
                print(f' O total é de: {total:.1f}')

            elif op == "2":
                nota1 = float(input("Digite a primeira nota:"))
                nota2 = float(input("Digite a Segunta nota:"))
                nota3 = float(input("Digite a terceira nota:"))
                media = (nota1 + nota2 + nota3) / 3
                print(f' A Sua média é de: {media:.1f}')

            elif op == "3":
                minutos = int(input("Digite a quantidade em minutos:")) 
                horas = minutos // 60  # divisão inteira
                resto_minutos = minutos % 60
                print(horas, "h", resto_minutos, "min")

            elif op == "4":
                base = 2
                expoente = 5
                resultado = base ** expoente
                print(resultado)  # 32

            elif op == "5":
                print("saindo...")
                break

            
if __name__ == "__main__":
    run = operador()
    run.menu()            