drink_speciale = "DigitalVodka"
print(drink_speciale)
drink_speciale = "TechnoWhiskey"
print(drink_speciale)
quantità_drink_speciale  = 28
print(quantità_drink_speciale)
prezzo_drink = 5.50
print(prezzo_drink)
pub_aperto = True
print(pub_aperto)
print("Giacomino")
stringa_inserita = input()
print(stringa_inserita)
drink_disponibili = 3+2
print(drink_disponibili)
alcolici = 3
analcolici = 2
drink_disponibili = alcolici+analcolici
print(drink_disponibili)
drink_disponibili = 5
print(drink_disponibili)
drink_disponibili += 2
print(drink_disponibili)
prezzo_drink = 4.25
sconto_fedelta = 1.50
prezzo_scontato = prezzo_drink-sconto_fedelta
print(prezzo_scontato)
print(prezzo_drink-sconto_fedelta)
nome_barman = "Edo" + "Bot"
print(nome_barman)
print("Ciao, mi chiamo "+"EdoBot")
print("Ciao, mi chiamo "+nome_barman)
a = 3
b = "2"
c = a + int(b)
print(c)
a = 3
b = "2"
c = str(a) + b
print(c)
anni_cliente = 85
if anni_cliente < 18:
    print("Sei minorenne: puoi ordinare solo analcolici")
elif anni_cliente > 80:
    print("Puoi ordinare alcolici ma vacci piano nonno")
else:
    print("Sei maggiorenne: puoi ordinare alcolici e analcolici")
nome_cliente = "Giacomino"
if nome_cliente == "Giacomino":
    print("Ciao giacomino, che piacere rivederti! <3")
pub_aperto = False
cons_dom_attiva = True
if pub_aperto or cons_dom_attiva:
    print("Siamo pronti a servirti!")
alcolici = ["Mojito", "White russian", "Caipirinha"]
print(alcolici)
print(alcolici[0])
quantita_alcolici = len(alcolici)
print(quantita_alcolici)
alcolici.append("Daiquiri")
print(alcolici)
alcolici.insert(0, "Martini")    
print(alcolici)
alcolici.remove("Daiquiri")
print(alcolici)
alcolici.pop(0)
print(alcolici)
alcolici[2] = "Caipiroska"
print(alcolici) 
print(alcolici)
analcolici = ["Limonata","Gazosa"]
menu_drink = analcolici+alcolici
print(menu_drink)
if "Mojto" in alcolici:
    print("La bevanda è disponibile")
print("Ecco i drink alcolici disponibili:")
print(alcolici)
print(alcolici[0])
print(alcolici[1])
print(alcolici[2])
for alcolico in alcolici:
    if alcolico == "White Russian":
        continue
    print(alcolico) 
for numero in range(1,19):
    print(numero)
a = 1
while a < 5:
    print(a)
    a += 1
while True:
    print("Che fa un uccellino dentro un computer?")
    risposta = input()
    if risposta == "chip":
        print("Risposta esatta!")
        break
    else:
        print("Ritenta\n")




