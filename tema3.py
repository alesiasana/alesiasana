meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
nr_tavi1= []
pret_mic= []

while studenti:
    print(studenti[0]+" "+"a comandat"+" "+comenzi[0])
    istoric_comenzi.append(comenzi[0])
    studenti.pop(0)
    comenzi.pop(0)
    meniu.pop(0)
    nr_tavi1.append(tavi[0])
    tavi.pop(0)

nr_papanasi=istoric_comenzi.count("papanasi")
nr_ceafa=istoric_comenzi.count("ceafa")
nr_guias=istoric_comenzi.count("guias")
nr_tavi=nr_tavi1.count("tava")

print("S-au comandat"+" "+str(nr_papanasi)+" "+"papanasi,"+" "+str(nr_ceafa)+" "+"ceafa,"+" "+str(nr_guias)+" "+"guias.")
print("Au mai ramas"+" "+ str(nr_tavi)+" "+"tavi.")


meniu_papanasi=meniu.count("papanasi")-nr_papanasi
if meniu_papanasi:
    print("Mai sunt papanasi: True")
else: print("Mai sunt papanasi: False")

meniu_ceafa=meniu.count("ceafa")-nr_ceafa
if meniu_ceafa:
    print("Mai este ceafa: True")
else: print("Mai este ceafa: False")

meniu_guias=meniu.count("guias")-nr_guias
if meniu_guias:
    print("Mai este guias: True")
else: print("Mai este guias: False")


incasari=nr_papanasi*preturi[0][1]+nr_guias*preturi[2][1]+nr_ceafa*preturi[1][1]
print(f"Cantina a incasat:{incasari} lei")


if preturi[0][1]<=7:
        pret_mic.append(preturi[0])
if preturi[1][1]<=7:
        pret_mic.append(preturi[1])
if preturi[2][1]<=7:
        pret_mic.append(preturi[2])

print(f"Produse care costa cel mult 7 lei:{pret_mic}")

