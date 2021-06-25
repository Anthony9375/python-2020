from geo_form import GeoForm

class Rechteck(GeoForm):
    def __init__(self, laenge, breite):
        GeoForm.__init__(self)
        self.laenge = laenge
        self.breite = breite

    def flaeche(self):
        return self.breite * self.laenge

    def umfang(self):
        return  2* (self.breite * self.laenge)