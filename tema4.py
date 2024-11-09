# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

#1
print(*progres)
#2
while "_" in progres and incercari_ramase > 0:
    litera= input("Introduceti o litera: ")

    if len(litera) == 1:
        pass
    else:
        print("Introdu o litera.")
        continue

     #verificam daca e litera

    if "a" <= litera<= "z":
        pass
    else :
        print("Introdu o litera.")
        continue

     #verificam litera in cuvant

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera

    else:
        incercari_ramase -= 1
        print(f"Litera '{litera}' nu este în cuvânt.")

#3
    print("Progresul curent: ", " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")

#4
if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul {cuvant_de_ghicit}!")

else: print(f"Ai pierdut! Cuvantul era: {cuvant_de_ghicit}!")