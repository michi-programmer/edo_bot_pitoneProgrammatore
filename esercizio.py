prezzo_drink = 5.5
sconto = 1
cliente_preferito = "Giacomino"

print("Come ti chiami?")
nome_cliente = input()
print("Quanti anni hai?")
anni_cliente = int(input())
if nome_cliente == cliente_preferito and anni_cliente > 25:
    print("Il prezzo del drink sara " + str(prezzo_drink-sconto))
else:
    print("Il prezzo del drink sara " + str(prezzo_drink))
