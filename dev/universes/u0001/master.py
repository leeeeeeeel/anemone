from .particles import Nulla, GravionUnum, VestionUnum, CompletionUnum

class Universe():
    """ Universe 0001

    first universe to ever be."""

    def __init__(self, particles):
        self.steps = 0
        self.particles = particles
        self.particle_count = len(self.particles)

    def walk(self, step=1):
        for i in range(step):
            for j in range(self.particle_count):
                particle = self.particles[j]
                particle.update(self.particles[j + 1:])
            self.steps += 1

particle_list = [
    CompletionUnum({
        'x': 12,
        'y': 43
    }),
    CompletionUnum({
        'x': 2,
        'y': 43
    }),
    CompletionUnum({
        'x': 23,
        'y': 1
    }),
    CompletionUnum({
        'x': 9,
        'y': 12
    }),
    CompletionUnum({
        'x': 23,
        'y': 43
    }),
    CompletionUnum({
        'x': 57,
        'y': 123
    }),
    CompletionUnum({
        'x': 4,
        'y': 234
    }),
    CompletionUnum({
        'x': 4,
        'y': 43
    }),
]
