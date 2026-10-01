def menu():
    print("===  CALCULADORA ===")
    print("" \
    "1 - Adição \n" \
    "2 - Subtração \n" \
    "3 - Multiplicação \n" \
    "4 - Divisão \n")

continuar = "s"
while continuar == "s":
    menu()
    opc = int(input("Digite o número da operação que desja realizar: "))
    

    primeiro_valor = int(input("Digite o primeiro número: "))
    segundo_valor = int(input("Digite o segundo valor número: "))
    print("")
    match opc:
        case 1:
            print("Adição - a opção atual \n")
            print(f"{primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor} ")
            print("")
        case 2:
            print("Subtração - a opção atual \n")
            print(f"{primeiro_valor} - {segundo_valor} = {primeiro_valor - segundo_valor} ")
            print("")
        case 3:
            print("Multiplicação - a opção atual \n")
            print(f"{primeiro_valor} x  {segundo_valor} = {primeiro_valor * segundo_valor} ")
            print("")
        case 4:
            print("Divisão - a opção atual \n")
            if segundo_valor == 0:
                print("Não é possível dividir por zero. \n")
            else:
                print(f"{primeiro_valor} ÷ {segundo_valor} = {primeiro_valor / segundo_valor} ")
                print("")
        case _:
            print("Operação inválida.")

    continuar = input("Deseja continuar? (Deseja realizar outra operação? (s/n))").lower()
    if continuar == "n":
        print("Calculadora encerrada.")
    

    