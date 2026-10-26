from datetime import datetime

PERSONAGGI = {
    "buoni": [
        "Buono Generico", #Utilizzato per il nome custom
        "IronMan",
        "Visione",
        "Hulk",
        "Thor",
        "BarbioBat",
        "Harry Potter",
        "Ron",
        "Hermione",
        "Silente"
    ],
    "cattivi": [
        "Cattivo Generico", #Utilizzato per il nome custom
        "Granfranca Melmoni",
        "Sangiorgio Orsetti",
        "Ricciardo Vaccino",
        "Argus Puzzi Cazzi Gazza",
        "Vachemord"
    ]
}

EFFETTO = [
    "customName", "BOMBA", "SPARI",
]

class Episodio():
    def __init__(self, title:str):
        self.title = title
        self.text = f"""{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

{title.upper()}
"""
        self.personaggi = []
        self.scene = []

    def save(self):
        with open(self.title+".txt", "w") as f:
            f.write(self.text)
            f.write("\n\nFINE")

class Scena():
    def __init__(self, ep:Episodio, name:str):
        self.name = name
        self.ep = ep
        self.ep.scene.append(self.name)
        self.ep.text += f"\n\n==================== {self.name} ====================\n\n"

    def descrizione(self, text:list[str]):
        for t in text:
            self.ep.text += f"--- {t}\n"
        self.ep.text += "\n\n\n"
        

class Effetto():
    def __init__(self, ep:Episodio):
        self.ep = ep
    
    def type(self, id:int, customName:str=""):
        if id == 0: self.ep.text += f"[ {customName} ]\n"
        elif id < len(EFFETTO): self.ep.text += f"[ {EFFETTO[id]} ]\n"

class Personaggio():
    def __init__(self, ep:Episodio, id:int, isHero:bool=True, customName:str=""):
        self.name = Personaggio.getName(id, isHero, customName)
        self.ep = ep
        self.ep.personaggi.append(self.name)
        self.isHero = isHero

    def disse(self, text:list[str], spazio:bool=False):
        self.ep.text += f"* {self.name}: "
        for i, t in enumerate(text):
            if i==0:
                self.ep.text += f"{t}\n"
            else:
                self.ep.text += f"\t\t{t}\n"
        
        self.ep.text += "\n" if spazio else ""

    

    @staticmethod
    def getName(id:int, isHero:bool=True, customName:str="") -> str:
        if id==-1:
            buoni = [f"{i}={n}; " for i, n in enumerate(PERSONAGGI["buoni"])]
            cattivi = [f"{i}={n}; " for i, n in enumerate(PERSONAGGI["cattivi"])]
            return "".join(buoni) +"\n"+"".join(cattivi)

        if id==0: return customName

        key = "buoni" if isHero else "cattivi"
        if key in PERSONAGGI and id < len(PERSONAGGI[key]): return PERSONAGGI[key][id]

        return "non trovato"

