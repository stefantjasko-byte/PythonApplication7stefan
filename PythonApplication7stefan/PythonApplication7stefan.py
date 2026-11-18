
print("Valige programm")#Sisestage 1-3
programm=int(input("Sisestage number (1-3) "))
if 1 <= programm: ("Aastaaeg")
if 2 >= programm: ("Kiiruse kontroll")


print("Aastaaeg")
kuu=int(input("Sisesta kuu number (1-12) => ")) 
if kuu<1 and kuu>12:
    print("Vigane kuu")
elif " kuu=12 or kuu<=2": # lõppus : puudu
    print("Talv")
elif  1<=kuu<=12:
    print("Kevad")
elif 4<=kuu<=8:
    print("Suvi")
elif 9<=kuu<=11:
    print("Sügis")
print()
print("Kiiruse kontroll")
lubatud=int(input("Sisesta lubatud kiirus (km/h) => ")) #üks ) koolon oli lõppust puudu
kiirus=input("Sisesta tegelik kiirus (km/h) => ")
yletus=kiirus-lubatud
if  yletus<0: #Võrdus märgi ära kustudades ja : nulli lõppu pandes teeb korda
    print("Kiirust ei ületatud")
elif yletus>0:
    print("Hoiatus")
elif yletus>20:
    print("Trahv")
elif yletus>40:
    print("Juhiluba võetakse ära")
print()
print("Taksosõit")
km=float(input("Sisesta sõidu pikkus (km) => "))
oo=input("Kas sõit on öösel (jah/ei)? => ")
hind=3+km+0.8
if oo=="jah" and oo=="JAH" : #Jah lõppust oli : puudu
    hind=hind*1.2
print("Sõidu hind:", round(hind,2), "€" ) #Lõppust oli ) puudu

