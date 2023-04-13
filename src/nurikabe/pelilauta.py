class Pelilauta:
    def __init__(self, nurikabe: list=None) -> None:

        # kaikki numerot > 0 ovat pulman alkutila:
        # 0: tyhjä solu
        # 1-: numero / "saaren koko"
        # 
        # < 0 ovat pelaajan tekemiä merkintöjä:
        # -2: piste / merkintä
        # -1: musta solu / "vettä"

        if nurikabe:
            self.nurikabe = nurikabe
            self.leveys = len(self.nurikabe[0])
            self.korkeus = len(self.nurikabe)
        else:
            self.leveys, self.korkeus = 6,6
            self.nurikabe = [[0 for b in range(self.korkeus)] for a in range(self.leveys)]

    # palauttaa tietyn solun arvon
    # koordinaatit muodossa (x,y):
        # ylävasen = (0,0)
        # yläoikea = (self.leveys,0)
        # alavasen = (0,self.korkeus)
        # alaoikea = (self.leveys,self.korkeus)
    def solu(self, koordinaatti:tuple):
        return self.nurikabe[koordinaatti[1]][koordinaatti[0]]

    # sallii yksittäisen muokkauksen teon laudalle
    def muokkaa_lautaa(self, koordinaatti: tuple, muokkaus: int):
        self.nurikabe[koordinaatti[1]][koordinaatti[0]] = muokkaus

    # testaa laittomia 2x2 vesistöjä ja palauttaa koordinaatin jos löytyy, True jos ei löydy
    # palautettu koordinaatti on laittoman 2x2 alueen ylävasemman kulman koordinaatti
    # riittää testata laudan leveys ja korkeus -1, reunalla ei voi muodostaa 2x2 aluetta
    def laillinen_vesi(self):
        laittomat = []

        for y in range(self.korkeus-1):
            for x in range(self.leveys-1):
                if self.solu((x,y)) == -1 and self.solu((x+1,y)) == -1 and self.solu((x,y+1)) == -1 and self.solu((x+1,y+1)) == -1:
                    laittomat.append((x,y))
        
        return laittomat if len(laittomat) > 0 else True

    # pelilaudan tulostus printillä
    def __str__(self) -> str:
        return "Nykyinen pelilauta:\n" + "\n".join([str(a) for a in self.nurikabe])

# testausta

""" peli = Pelilauta()
print(peli)

peli.muokkaa_lautaa((1,2),-1)
print(peli)

# virhe pitäisi havaita koordinaatissa (1,2)
testilauta1 = [
    [-1,0,0,0,-1,-1],
    [0,0,0,0,-1,0],
    [0,-1,-1,0,0,0],
    [0,-1,-1,0,0,0],
    [-1,0,0,0,-1,-1],
    [-1,0,0,0,-1,-1]
]

peli2 = Pelilauta(testilauta1)
print(f"peli2: {peli2}")

print(peli.laillinen_vesi())
print(peli2.laillinen_vesi())

testilauta2 = [
    [-1,0,0,0,-1,-1],
    [0,0,0,0,-1,0],
    [0,-1,-1,-1,0,0],
    [0,-1,-1,-1,0,0],
    [-1,0,-1,-1,-1,-1],
    [-1,0,0,0,-1,-1]
]

peli3 = Pelilauta(testilauta2)
print(peli3.laillinen_vesi()) """