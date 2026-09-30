lista_mista = [42, 7, 1.5, True, "Um texto", "77"]

lista_mista.append("Outro valor")
lista_mista.append(7.8)

for lista in lista_mista:
    print(f"{lista} é do tipo {type(lista)}")