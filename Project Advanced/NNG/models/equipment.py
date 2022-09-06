from materiaal import Materiaal

# Niet goed

class Equipment:

    def __init__(self):
        self.equipment = []

    def add_materiaal(self, materiaal):
        self.equipment.append(materiaal)

    def get_materiaal(self, serienummer):
        for materiaal in self.equipment:
            if materiaal.serienummer == serienummer:
                return materiaal


# ----------------------------

if __name__ == '__main__':

    equipment = Equipment()

    equipment.add_materiaal(Materiaal('Landingsgestel F16',
                                      'Neuswiellandingsgestel',
                                      '0023',
                                      'landingsgestel',
                                      'LG893427',
                                      '374589-324678',
                                      'front'))

    equipment.add_materiaal(Materiaal('Landingsgestel F16',
                                      'Hoofdlandingsgestel RA',
                                      '0023',
                                      'landingsgestel',
                                      'LG893428',
                                      '374589-324786',
                                      'rechtsachter'))

    equipment.add_materiaal(Materiaal('Landingsgestel F16',
                                      'Hoofdlandingsgestel LA',
                                      '0023',
                                      'landingsgestel',
                                      'LG893429',
                                      '374589-324782',
                                      'linksachter'))

    equipment.add_materiaal(Materiaal('Landingsgestel F35',
                                      'Hoofdlandingsgestel LA',
                                      '0023',
                                      'landingsgestel',
                                      'LG893129',
                                      '474589-324782',
                                      'front'))