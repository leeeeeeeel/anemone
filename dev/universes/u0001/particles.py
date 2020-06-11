from .forces import Gravitatis, Vestibulum

# Particle
class Particle():
    forces = []
    atributes = {}
    variables = {}
    results = {}

    def __init__(self,variables_state):
        self.variables = variables_state
        self.results = dict.fromkeys(variables_state.keys(),0)

    def update(self, targets):
        for target in targets:
            for force in self.forces:
                if force in target.forces:
                    force.interact(force, self, target)
        for key, result in self.results.items():
            self.variables[key] += result

# Root Particles
class Nulla(Particle):
    pass
class Gravion(Particle):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.forces = [
            Gravitatis
        ]
class Vestion(Particle):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.forces = [
            Vestibulum
        ]
class Completion(Particle):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.forces = [
            Gravitatis,
            Vestibulum
        ]

# Gravions
class GravionUnum(Gravion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 1
        }
class GravionDuo(Gravion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 2
        }
class GravionTres(Gravion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 4
        }
class GravionQuattuor(Gravion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 16
        }

# Vestions
class VestionUnum(Vestion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "charge" : 1
        }
class VestionDuo(Vestion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "charge" : 2
        }
class VestionTres(Vestion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "charge" : 4
        }
class VestionQuattuor(Vestion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "charge" : 16
        }

# Completions
class CompletionUnum(Completion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 1,
            "charge" : 1
        }
class CompletionDuo(Completion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 2,
            "charge" : 2
        }
class CompletionTres(Completion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 4,
            "charge" : 4
        }
class CompletionQuattuor(Completion):
    def __init__(self, variables_state):
        super().__init__(variables_state)
        self.atributes = {
            "mass" : 16,
            "charge" : 16
        }
