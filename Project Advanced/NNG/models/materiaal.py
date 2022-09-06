from gebeurtenis import Gebeurtenis
from onderhoud import Onderhoud

class Materiaal:

    def __init__(self, naam, omschrijving, atacode, soort, partnummer, serienummer, positie):
        self.naam = naam
        self.omschrijving = omschrijving
        self.atacode = atacode
        self.type = soort
        self.partnummer = partnummer
        self.serienummer = serienummer
        self.positie = positie
        self.gebeurtenissen = []
        self.onderhoudsbeurten = []

    def __repr__(self):
        return ' - '.join(map(str, self.__dict__.values()))

    def add_gebeurtenis(self, gebeurtenis):
        self.gebeurtenissen.append(gebeurtenis)

    def add_onderhoudsbeurt(self, onderhoudsbeurt):
        self.gebeurtenissen.append(onderhoudsbeurt)

# --------------------------------------------------------------------

if __name__ == '__main__':

    materieel = []

    materieel.append( Materiaal('Landingsgestel F16', 'Neuswiellandingsgestel', '0023', 'landingsgestel', 'LG893427', '374589-324678', 'front') )
    materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel RA', '0023', 'landingsgestel', 'LG893428', '374589-324786', 'rechtsachter') )
    materieel.append( Materiaal('Landingsgestel F16', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893429', '374589-324782', 'linksachter') )
    materieel.append( Materiaal('Landingsgestel F35', 'Hoofdlandingsgestel LA', '0023', 'landingsgestel', 'LG893129', '474589-324782', 'front') )

    for materiaal in materieel:
        if 'F16' in materiaal.naam:
            print(materiaal)

    for materiaal in materieel:
        if materiaal.serienummer == '374589-324678':
            found_materiaal = materiaal
            break

    found_materiaal.add_gebeurtenis( Gebeurtenis('**', '2022-09-05', 'Peter', 'Harde landing', 'Soesterberg', 'windkracht 7 zijwaarts') )
    found_materiaal.add_gebeurtenis( Gebeurtenis('***', '2022-09-06', 'Peter', 'Zeer harde landing', 'Soesterberg', 'windkracht 7 frontaal') )

    print(found_materiaal)