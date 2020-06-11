import tkinter as tk

class App(tk.Frame):
    speed = 1

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('anemone simulator')

        self.top = tk.Frame(self)
        self.bottom = tk.Frame(self)

        self.eye = Eye(self.top)
        self.speed_scale = tk.Scale(self.top, bg='red', from_=1, to=500, bd=0, width=10,
            troughcolor='black', command=self.change_speed)
        self.walk_button = tk.Button(self, bg='green', bd=0, command=self.walk)
        self.pause_button = tk.Button(self, bg='red', bd=0, command=self.pause)
        self.speed_scale.set(self.speed)

        self.pack(fill=tk.BOTH, expand=True)
        self.top.pack(fill=tk.BOTH, expand=True)
        self.bottom.pack(fill=tk.X)
        self.walk_button.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.pause_button.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        self.speed_scale.pack(side=tk.RIGHT, fill=tk.BOTH)

    def watch(self, universe):
        self.universe = universe
        self.paused = False
        self.pivot = universe.particles[0]
        self.after(self.speed, self.run)

    def pause(self):
        self.paused = not self.paused
        if not self.paused:
            self.after(self.speed, self.run)

    def run(self):
        if not self.paused:
            self.universe.walk()
            self.eye.paint(self.universe)
            self.after(self.speed, self.run)

    def walk(self, step=1):
        self.universe.walk(step)
        self.eye.paint(self.universe)

    def change_speed(self, speed):
        self.speed = speed

class Eye(tk.Canvas):
    def __init__(self, root):
        super().__init__(root,
            bg='black',
            bd=0,
            highlightthickness=0,
            cursor='tcross'
        )
        self.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def get_center(self):
        x = self.winfo_width() / 2
        y = self.winfo_height() / 2
        return (x, y)

    def get_relative_position(self, center, pivot, particle):
        x = center[0] + (particle.variables['x'] - pivot[0])
        y = center[1] + (particle.variables['y'] - pivot[1])
        return (x, y)

    def paint(self, universe, pivot=(0, 0)):
        self.delete('all')
        center = self.get_center()
        for particle in universe.particles:
            x, y = self.get_relative_position(center, pivot, particle)
            self.create_oval(x+2, y+2, x-2, y-2, fill='red')
