matriz = [
    [1,2,3,4,5,6],
    [3,4,5,6,7,8],
    [2,3,2,1,6,9]
]

print(matriz[2])
print(matriz[2][0])
print("____")
#Recorrer matriz1s
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
    print()
print("____")

for i in range(0,len(matriz)):
    for j in range(0,len(matriz[i])):
        print(matriz[i][j],end=" ")
    print()

