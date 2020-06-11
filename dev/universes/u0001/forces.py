import math

class Particle():
    def interact(self):
        print ('a')


class Gravitatis():
    def strenght_decay(self, distance):
        if distance == 0:
            return 1
        return 1/(distance**2)

    def interact(self, p1, p2):
        distance = math.sqrt((p1.variables['x'] - p2.variables['x']) ** 2 +
            (p1.variables['y'] - p2.variables['y']) ** 2)

        scale_factor = p1.atributes['mass'] * p2.atributes['mass']
        strenght_decay = self.strenght_decay(self, distance)

        g = scale_factor * strenght_decay

        p1.results['x'] += g
        p1.results['y'] += g

        p2.results['x'] += g * -1
        p2.results['y'] += g * -1

class Vestibulum():
    def strenght_decay(self, distance):
        if distance == 0:
            return 1
        return 1/(distance**4)

    def interact(self, p1, p2):
        distance = math.sqrt((p1.variables['x'] - p2.variables['x']) ** 2 +
            (p1.variables['y'] - p2.variables['y']) ** 2)

        scale_factor = p1.atributes['charge'] * p2.atributes['charge']
        strenght_decay = self.strenght_decay(self, distance)

        g = scale_factor * strenght_decay

        p1.results['x'] += g
        p1.results['y'] += g

        p2.results['x'] += g * -1
        p2.results['y'] += g * -1
