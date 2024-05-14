
#voi avea nevoie de trei categorii:
#tranzitii de tipul stare litera cheie
#tranzitii de tipul cheie litera cheie
#tranzitii de tipul cheie litera stare
def ScoateStare(cheie_scoasa, graf):
    intru = []
    sunt = []
    ies = []
    for cheie in graf:
        for tuplu in graf[cheie]:
            if  str(cheie) == str(cheie_scoasa):
                if tuplu[1] == cheie:
                    sunt.append((cheie, tuplu[0], tuplu[1]))
                else:
                    ies.append((cheie, tuplu[0], tuplu[1]))
            elif str(tuplu[1]) == str(cheie_scoasa):
                intru.append((cheie, tuplu[0], tuplu[1]))
                graf[cheie] = [t if t != tuplu else 0 for t in graf[cheie]]
        graf[cheie] = [t for t in graf[cheie] if t != 0]

    del graf[cheie_scoasa]

    # print(intru)
    # print(sunt)
    # print(ies)
    # print()

    if intru != [] and ies != []:
          for i in intru:
                    for k in ies:
                        sir = i[1]
                        if len(sunt)!=0:
                            sir2 = "|".join([o[1] for o in sunt])
                            sir = sir + '(' + sir2 + ')' + '*'
                        sir = sir + k[1]
                        sir="".join([c for c in sir if c != '.'])
                        # print(sir)
                        if sir != "":
                            graf[i[0]].append((sir,k[2]))
                        else:
                            graf[i[0]].append(('.',k[2]))
    # print()




f = open("fisier1.in")
nr_stari = int(f.readline().strip())
graf = {}
stare_finala_noua = None
stare_initiala_noua = None

#cream dictionarul
for nod in f.readline().strip().split():
    graf[nod] = []
#citim alfabetul
nr_litere=int(f.readline().strip())
alfabet = []
for litera in f.readline().strip().split():
    alfabet.append(litera)
#citim starea initiala
stare_initiala = f.readline().strip()
#citim starile finale
nr_stari_finale = int(f.readline().strip())
stari_finale = []
for s in f.readline().strip().split():
    stari_finale.append(s)
#verificam daca este nevoie sa adaugam stare finala sau initiala noua
if len(stari_finale) > 1:
    stare_finala_noua = -1
if stare_initiala in stari_finale:
    stare_initiala_noua = 0
#citim tranzitiile si nu uitam sa le verificam si pe ele
tranzitii=int(f.readline().strip())
for i in range(tranzitii):
    cheie,litera,destinatie = f.readline().strip().split()
    #celelalte doua conditii care daca nu sunt indeplinite rezulta in adaugarea unei stari finale sau initiale noi
    if cheie in stari_finale:
        stare_finala_noua = -1  #in cazul in care starile nu sunt numere de la 1 la n
    if destinatie == stare_initiala:
        stare_initiala_noua = 0
    #verificam ca litera sa se afle in alfabet
    if litera in alfabet:
        graf[cheie].append((litera,destinatie))

#adaugam starea finala si initiala daca este cazul si facem modificarile necesare
if stare_initiala_noua is not None:
    #adaugam o cheie noua in dictionar adica starea 0 si facem muchie cu lambda catre starea initiala\
    graf[0] = [('.', stare_initiala)]
    stare_initiala = stare_initiala_noua
if stare_finala_noua is not None:
    for stare in stari_finale:
        graf[stare].append(('.', stare_finala_noua)) #adaugam muchii cu lambda de la fostele stari finale la noua stare finala
    graf[stare_finala_noua] = []
if stare_finala_noua is None: #nu sunt nici mai multe stari finale si nici nu pleaca muchii din cea finala inseamna ca avem o stare unica finala
    stare_finala_noua = stari_finale[0]


#INCEPEM ALGORITMUL DE SCOATERE AL MUCHIILOR
while len(graf) > 2: #pana nu ramane doar cu starea initiala si finala
    stare = None
    for cheie in graf:
        if str(cheie) != str(stare_finala_noua) and str(cheie) != str(stare_initiala): #inseamna ca putem scoate acea stare
            stare = cheie
            break
    ScoateStare(stare, graf)
#AFISAM EXPRESIA OBTINUTA
for cheie in graf:
    if str(cheie) == str(stare_initiala):
        for i in range(len(graf[cheie])):
            if i!=len(graf[cheie]) - 1:
                print(graf[cheie][i][0]+'|', end = "")
            else:
                print(graf[cheie][i][0])
