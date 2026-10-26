from mylib import Episodio, Personaggio, Scena, Effetto

#print(Personaggio.getName(-1))
#exit()
EP = Episodio("avengers pt.4")

ironman = Personaggio(EP, 1)
visione = Personaggio(EP, 2)
batman = Personaggio(EP, 5)
hulk = Personaggio(EP, 3)
thor = Personaggio(EP,4)
tonyCazzo = Personaggio(EP, 0, customName="TonyCazzo")
jarvis=Personaggio(EP, 0, customName="Jova")

cattivo1 = Personaggio(EP, 0, False, "Scagniozzo_1")
cattivo2 = Personaggio(EP, 0, False, "Scagniozzo_2")
gianfranca = Personaggio(EP, 1, False)
sangiorgi = Personaggio(EP, 2, False)

eff = Effetto(EP)


#*SCENA 1
Scena(EP, "LOTTA FACILE").descrizione([
    "SOTTOFONDO: guerra (spari e bombe)",
    "MUSICA: ",
])
ironman.disse(["(fsss) Hey coglione (fsss) vieni a comprirmi (fsss) (fsss)."])
visione.disse(["Finisco qui e arrivo"])
cattivo1.disse(["Ahh"], spazio=True)

visione.disse(["Finisco qui e arrivo"])
cattivo2.disse(["Non l'avrai vinta, pezzo di sterco"])
visione.disse(["Ah no? ah no? ahahaha stupido idiota, POTERE DEL TRIP AT ADVISORES!"])
cattivo2.disse(["Ah"])

ironman.disse(["Hey Hulk, rompi un po st'asfalto che sento una puzza strana"])
hulk.disse(["HULK ROMPE ASFALTO ORA !!!"])
ironman.disse(["Bravo ragazzo, hahaha"], spazio=True)
eff.type(0, "suono di qualcosa che si rompe")
visione.disse(["Oh Porco Cazzo, che cosa c'è scritto"])
ironman.disse(["\"Ex Ilva, inchiesta inquinamento: chiesti i domiciliari per Morselli e altri due\""])
visione.disse(["tutto sto spazio per un pezzo di carta? ma perchè?, mmmm"])
hulk.disse(["Hulk è preplesso."])
thor.disse([
    "Hey Guys, m'avete visto com'erano vestiti sti masculi.",
    "c'è rosa su verde cioè, c'è sta proprio male (uffff), non ci voglio pensare. (blue)"
])


#*SCENA 2
Scena(EP, "AL QUARTIER GENERALE").descrizione([
    "MUSICA: stacco iniziale con batmanTransition; "
])
eff.type(0, "batmanTransition")
ironman.disse(["jova dov'è BarbioBat?, chiamamelo"])
jarvis.disse(["Agli ordini, signore."])
eff.type(0, "squillo telefono")
batman.disse(["hey ragazzi accendetemi il computer, sto arrivando..."])
ironman.disse([
    "Si tranquillo tanto ho una tua impronta digitale dentro la tasca, GUARDA!!! coglione...", 
    "Sbrigati e non intallarti software del cazzo con cloude, maiale",
], spazio=True)
eff.type(0, "squilla il telefono")
visione.disse(["Regaz, Sconosciuto Rispondo io, eh"])
tonyCazzo.disse(["-risponde-"])
visione.disse(["oh ma checazzo vuoi?!? coglioni siamo profesionisti noi"])
eff.type(0, "Visione sbatte il telefono")

#*SCENA 3
Scena(EP, "Sangiorgi e gianfranca cercano un luogo corretto").descrizione([
    "DESCRIZIONE: gianfranca melmoni e sangiorgio oresetti stanno cercando di piazzare qualche bomba",
])
gianfranca.disse(["Hai trovatoun luogoper mettereste cariche?, essere inutile?"])
sangiorgi.disse(["Ma signora del male perche mi tratta male?, sto fancendo del mio meglio."])


EP.save()
