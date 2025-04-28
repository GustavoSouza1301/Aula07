notas = [" "," "," "," "," "]
somaSala = 0
cont = 0

for x in range(len(notas)):
    notas [x]=float(input("Digite a primeira nota: "))

for y in range(len(notas)):
    somaSala  +=  notas[y]
mediaSala = somaSala / len(notas)

for z in range(len(notas)):
    if notas[z] > mediaSala :
        cont += 1

print(f"A média da sala é {mediaSala} e a quantidade de alunos que estão acima da média é {cont}")