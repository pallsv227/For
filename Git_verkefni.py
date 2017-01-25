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
print ("í þessum texta eru",(sum(1 for c in texti if c.isupper())), "Hástafir og", sum(1 for c in texti if c.islower()), "lágstafir")