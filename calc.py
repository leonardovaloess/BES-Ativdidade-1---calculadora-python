while True:
    operacao = input(f"Qual operação deseja fazer?\n 1 - somar \n 2 - subtrair \n 3 - multiplicar \n 4 - dividir \n 5 - sair\n")

    if operacao == '1' or operacao == '2' or operacao == '3' or operacao == '4':
        a = float(input("Informe o valor de a: "))
        b = float(input("Informe o valor de b: "))

        if operacao == '1':
            print(f"{a} + {b} = {a + b}")
        elif operacao == '2':
            print(f"{a} - {b} = {a - b}")
        elif operacao == '3':
            print(f"{a} x {b} = {a * b}")
        elif operacao == '4':
            print(f"{a} : {b} = {a / b}")
    elif operacao == '5':
        print("saindo")
        break
    else:
        print("Inválido")
        

