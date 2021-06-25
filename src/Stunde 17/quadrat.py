from geo_form import GeoForm

class Quadrat(GeoForm):
    def __init__(self, laenge):
        GeoForm.__init__(self)
        self.laenge = laenge

    def flaeche(self):
        return self.laenge * self.laenge

    def umfang(self):
        return 4 * self.laenge