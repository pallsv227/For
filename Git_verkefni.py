#Páll Gunnar Svansson 25.1.17

#dæmi 1
tala_1 = int(input("sláðu inn eina tölu: "))
tala_2 = int(input("sláðu inn aðra tölu: "))
svar = ((tala_1)+(tala_2))
print ("útkoman af þessum tölum er ", svar)

#dæmi 2
fornafn = input("sláðu inn fornafnið þitt: ")
eftirnafn = input("sláðu inn eftirnafnið þitt: ")
print ("halló", fornafn, eftirnafn)

#dæmi 3
texti = str(input("sláðu inn texta: "))
hastafir = 0
lagstafir = 0
eftirHastafi = 0
for x in texti:
    if x.isupper():
        hastafir = hastafir +1
    if x.islower():
        lagstafir = lagstafir +1
for x in range(len(texti)):
    if texti[x].isupper():
        i= x+1
        if texti[i].lower():
            eftirHastafi = eftirHastafi +1
print ("í þessum texta eru", hastafir, "Hástafir,", lagstafir, "lágstafir og", eftirHastafi,"eftir stórum staf")