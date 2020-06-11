import os, importlib

class UnkownUniverseException(Exception):
    pass

def universe_selector(uname):
    if not uname:
        uname = 'u0001'

    root = './universes'
    dirlist = [item for item in os.listdir(root)]

    if uname not in dirlist:
        raise UnkownUniverseException("universe {0} not recognized".format(uname))

    package = "universes.{0}".format(uname)
    module = importlib.import_module('.master', package)

    return module.Universe(module.particle_list)
