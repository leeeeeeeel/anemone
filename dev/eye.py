import sys
import tkinter as tk
import getopt as opt
import .universes.catalog as cat

def create_canvas(height=300, width=300, bg='black'):
    root = Tk()
    root.geometry('300x300')

    c = Canvas(root, height=height, width=width, bg=bg)
    c.pack()

    return root

def main(opts):
    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

    root = create_canvas()
    uni = cat.U0001()
    root.watch(uni)

if __name__ == '__main__':
    try:
      opts, args = opt.getopt(argv,'hu:h:w:',["help","universe=","height=","width="])
    except getopt.GetoptError:
      print('Unexpected arguments.')
      sys.exit(2)

    main(opts)
