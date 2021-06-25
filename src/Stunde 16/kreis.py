class Kreis:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def flaeche(self):
        return 2* self.radius * self.PI

    def umfang(self, radius):
        return 2 * self.PI * self.radius