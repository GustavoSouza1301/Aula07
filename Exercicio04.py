a = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Digite um número: "))
m = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(a)):
    m[i] = a[i] * x
print(m)