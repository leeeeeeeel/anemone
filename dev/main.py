import sys
import getopt
from core.apps import Eye
import core.help as h

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],'hu:',["help","universe="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    uname = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ('test.py -s <size> -u <universe name>')
            sys.exit()
        elif opt in ("-u", "--universe"):
            uname = arg

    try:
        universe = h.universe_selector(uname)
    except h.UnkownUniverseException as err:
        print(err)
        sys.exit(2)

    app = Eye()
    app.watch(universe)
    app.mainloop()

if __name__ == '__main__':
    main()
