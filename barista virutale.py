#Dichiarazione Variabili
nome_barman = "EdoBot"
drink_speciale = "DigitalVodka"
prezzo_drink = 5.5
alcolici = ["Mojito", "White russian", "Caipirinha"]
analcolici = ["Limonata","Gazosa"] 

#Inizio del programma
print("Benvenuto al Pub Drink&Codici")
print("Mi chiamo " + nome_barman + " ...e sono pronto a servirti =)")


print("Il drink più cool del nostro pub è: "+str(drink_speciale))
print("Provalo subito, al modico prezzo di "+str(prezzo_drink))
print("\nI drink alcolici sono "+str(len(alcolici)))
print("\nI drink analcolici sono "+str(len(analcolici)))
print("\nInserisci il tuo anno di nascita")
anno_nascita = int(input())
anni_cliente = 2021 - anno_nascita
print("Hai "+str(anni_cliente)+" anni")
drink_disponibili = []
if anni_cliente < 18:
    print("\nSei minorenne puoi ordinare solo analcolici")
    drink_disponibili += analcolici
else:
    print("\nSei maggiorenne puoi ordinare analcolici e alcolici")
    drink_disponibili = analcolici+alcolici
while True:
    print("Ecco i drink disponibili per te:")
    for drink_dsponibile in drink_disponibili:
        print(drink_dsponibile)
    drink_scelto = input()
    if drink_scelto in drink_disponibili:
        print("Hai scelto "+drink_scelto+". Buon aperitivo!")
        break
    else:
        print("Mi spiace, il drink "+drink_scelto+" non è disponibile =(")

