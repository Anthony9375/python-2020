class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        return self.breite * self.laenge

    def umfang(self):
        return  2* (self.breite * self.laenge)