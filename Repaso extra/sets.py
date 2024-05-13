#No tiene orden y no se repite so unicos
set1 = {2,3,5,7}
set2 = set([2,3,5,7])

nombres = {"Elena","Juan","Elena","Pablo"}
print(nombres)

for nombre in nombres:
    print(nombre)

print("Pedro" in nombres)

nombres.add("Pedro")
print(nombres)

nombres.remove("Elena")
print(nombres)


nombres.pop()
print(nombres)
