nomes = [" "," "," "," "," "]
for x in range(len(nomes)):
    nomes[x]= input(f"digite o nome {x+1}: ")

nome = input("Digite um nome para pesquisar: ")
for y in range(len(nomes)):
    if nome == nomes[y]:
        print(f"Achei {nome} na posição {y}")
    else:
        print("Não existe")
    