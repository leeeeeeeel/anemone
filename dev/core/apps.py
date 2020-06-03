import tkinter as tk

class Eye(tk.Tk):

    def __init__(self,
                 *args,
                 **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('anemone simulator')

        c = tk.Canvas(self,
                      bg='black',
                      bd=0,
                      highlightthickness=0,
                      cursor='tcross')
        c.pack(fill=tk.BOTH, expand=True)

    def watch(self,
              universe):
        self.title('anemone simulator')
        universe.printa()
        pass
