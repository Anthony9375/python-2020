from geo_form import GeoForm

class Dreieck(GeoForm):
    def __init__(self, grundflaeche, hoehe, a, b, c):
        GeoForm.__init__(self)
        self.grundflaeche = grundflaeche
        self.hoehe = hoehe
        self.a = a
        self.b = b
        self.c = c

    def flaeche(self):
        return self.grundflaeche * self.hoehe / 2

    def umfang(self):
        return self.a + self.b + self.c