
#1- liste si dictionare
from random import randrange

import pandas

categorii=[]
produseElectrocasniceMari=[]
produseElectrocasniceMari.append("Aparate frigorifice")
produseElectrocasniceMari.append("Aparate incorporabile")
produseElectrocasniceMari.append("Masini de spalat vase")
produseElectrocasniceMari.append("Hote")
produseElectrocasniceMari.append("Aragazuri")

categorii.append(produseElectrocasniceMari)

produseTelefoaneTablete=[]
produseTelefoaneTablete.append("Smartphone")
produseTelefoaneTablete.append("Accesorii Smartphone")
produseTelefoaneTablete.append("Smartwatch si Smartbrand")
produseTelefoaneTablete.append("Tablete")
produseTelefoaneTablete.append("Periferice mobile")
produseTelefoaneTablete.append("Telefoane")

categorii.append(produseTelefoaneTablete)

produseTVAudioVideoFoto=[]
produseTVAudioVideoFoto.append("Televizoare")
produseTVAudioVideoFoto.append("Portabile auto")
produseTVAudioVideoFoto.append("Foto-Video")
produseTVAudioVideoFoto.append("Audio Hi-Fi")
produseTVAudioVideoFoto.append("Accesorii Foto-Video")
produseTVAudioVideoFoto.append("Home Cinema")
produseTVAudioVideoFoto.append("Videoproiectoare si Accesorii")
produseTVAudioVideoFoto.append("Periferice si Accesorii TV-Audio")

categorii.append(produseTVAudioVideoFoto)

produseLaptopIT=[]
produseLaptopIT.append("Laptop")
produseLaptopIT.append("Desktop PC si Monitoare")
produseLaptopIT.append("Componente")
produseLaptopIT.append("Accesorii laptop")
produseLaptopIT.append("Periferice")
produseLaptopIT.append("Retelistice")
produseLaptopIT.append("Stocare date")
produseLaptopIT.append("Imprimante si consumabile")
produseLaptopIT.append("Software")

categorii.append(produseLaptopIT)

produseClimatizareIngrijire=[]
produseClimatizareIngrijire.append("Ingrijire locuinta")
produseClimatizareIngrijire.append("Ingrijire tesaturi")
produseClimatizareIngrijire.append("Climatizare")

categorii.append(produseClimatizareIngrijire)

produseElectrocasniceBucatarie=[]
produseElectrocasniceBucatarie.append("Preparare Cafea si Bauturi")
produseElectrocasniceBucatarie.append("Prepare Paine")
produseElectrocasniceBucatarie.append("Articole menaj")
produseElectrocasniceBucatarie.append("Preparate alimente")
produseElectrocasniceBucatarie.append("Cuptoare Microunde si Electrocasnice")
produseElectrocasniceBucatarie.append("Procesare Alimente")

categorii.append(produseElectrocasniceBucatarie)
#print(categorii)

#set + metoda set
numeCategorii=set()
numeCategorii.add("Electrocasnice Mari")
numeCategorii.add("TV, Audio-Video, Foto")
numeCategorii.add("Laptop, IT")
numeCategorii.add("Climatizare, Ingrijire, Locuinta si Tesaturi")
numeCategorii.add("Electrocasnice bucatarie")

#print(numeCategorii)

#structuri repetitive

#dictionar + metoda dictionar
dictionar={}
listaDictionare=[]
for categorie, numeCategorie in zip(categorii, numeCategorii):
    dictionar ["Categorie"]= numeCategorie;
    for tipProdus in categorie:
        dictionar["Tip produse"]=tipProdus;
        #print(dictionar)
        copie=dict.copy(dictionar)
        listaDictionare.append(copie)

#print(listaDictionare)

# structuri conditionale

for element in listaDictionare:
    if element['Categorie']=="Laptop, IT":
        element['Cantitate']=randrange(50,200)
    else:
        element['Cantitate']=randrange(50)
#print(listaDictionare)


#definire si apelare functii

#elimina produsele de preparare
def eliminareProduseDePreparare(listaProduse):
    for produs in listaProduse:
        if(produs['Tip produse'].find("Preparare")!=-1):
            listaProduse.remove(produs)
    return listaProduse


lista=eliminareProduseDePreparare(listaDictionare)
#print(lista)

#tuplu si metoda specifica
#tuplu cu pozitiile produselor comandate dintr-o lista; afisare produse si numarul de comenzi realizate pentru fiecare tip de produs

comenzi=(12,21,12,23,24,12,12,23)
def afisareProduseComandate(comenzi,listaProduse):
    comenziFaraDuplicate=[]
    for i in comenzi:
        if (i not in comenziFaraDuplicate):
            comenziFaraDuplicate.append(i)
            #print("S-au comandat "+comenzi.count(i).__str__()+" produse de tip "+listaProduse[i].get('Tip produse'))

afisareProduseComandate(comenzi,listaDictionare)

# import fisier csv in pachetul pandas
produse=pandas.read_csv('produse.csv')
#print(produse)

#accesare date cu loc si iloc
#informatii despre al 5-lea produs
#print(produse.loc[4])
# afisare cantitate si pret mediu al tuturor produselor
#print(produse.iloc[:,2:4])
#afisare categorie produse cu pret mediu>1000
#print(produse.loc[(produse['Pret mediu']>1000),['Categorie','Pret mediu']])

#stergerea de coloane si inregistrari

#stergere coloana "Venit brut"
produse=produse.drop(columns="Venit brut")
#print(produse)

#stergere inregistrari
#flanco renunta la vanzarea produselor smart

#print(produse.loc[produse['Tip produse'].str.contains("Smart")==0,'Tip produse'])
produse=produse.set_index('Tip produse')
produse=produse.drop(["Smartphone","Accesorii Smartphone","Smartwatch si Smartbrand"],axis=0)
#print(produse)

#utilizare functii de grup
#cantitatea totala de produse vandute din categoria data
produse=pandas.read_csv('produse.csv',usecols=['Cantitate','Categorie'])
rows=[]
for row in produse.iterrows():
    if(row[1].get('Categorie')=="Climatizare,Ingrijire, Locuinta si Tesaturi"):
        rows.append(row[0])
newRows=produse.iloc[rows]
print(newRows['Cantitate'].sum())

#prelucrari statistice
#grupare si agregare date
produse=pandas.read_csv("produse.csv")

print(produse.groupby(['Categorie']).agg({
    "Venit brut":sum,
    "Tip produse":"count",
    'Pret mediu':"median"
}))

#afisare grafic- ordinea descrescatoare a veniturilor brute totale obtinute pe fiecare categorie
import matplotlib.pyplot as plt
plot_data=produse.groupby('Categorie')['Venit brut'].sum()
plot_data.sort_values(ascending=False).plot(kind='bar')
plt.show()


#merge, join
produse = pandas.read_csv('produse.csv')
produse1 = pandas.read_csv('produse1.csv')

#afisare produse fara discount
#produse1- fisier cu acele tipuri de produse pentru care s-a setet un discount
result = pandas.merge(produse,
                  produse1[['Tip produse','Discount']],
                  on='Tip produse',
                      how='left')
#print(result)

#seteaza valoarea 0 unde nu a fost setat discountul
print(result['Discount'].fillna(value=0))










