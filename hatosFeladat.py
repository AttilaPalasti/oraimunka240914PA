import beolvas

# 6.	Tárolj el két számot egy-egy változóba! Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat teljes műveleti sorrendben.
szam1 = beolvas.tortszamSzamBeolvas()
szam2 = beolvas.tortszamSzamBeolvas()
#műveletek
osszeg = szam1+szam2
kulombseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1 / szam2
maradek = szam1%szam2
hatvany1 = szam1**szam2
hatvany2 =szam2**szam1


# kiírás
print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1)+"-"+str(szam2)+"="+str(kulombseg))
print(str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print(str(szam1)+"/"+str(szam2)+"="+str(hanyados))
print(str(szam1)+"%"+str(szam2)+"="+str(maradek))
print(str(szam1)+"^"+str(szam2)+"="+str(hatvany1))
print(str(szam2)+"^"+str(szam1)+"="+str(hatvany2))