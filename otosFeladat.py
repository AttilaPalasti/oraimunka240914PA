import beolvas

# Tárolj el két számot egy-egy változóba! Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat!

szam1 = beolvas.tortszamSzamBeolvas()
szam2 = beolvas.tortszamSzamBeolvas()

#műveletek
osszeg = szam1+szam2
kulombseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1 / szam2
maradek = szam1%szam2
hatvany = szam1**szam2

# kiírás
print(osszeg)
print(kulombseg)
print(szorzat)
print(hanyados)
print(hatvany)
