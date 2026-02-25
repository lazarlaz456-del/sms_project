import tkinter as tk

class Weather_App(tk.Tk):
    #Initialize the window
    def __init__(self):
        super().__init__()
        self.title("Welcome to the weather app")
        self.config(padx=3, pady=3)

        self.canvas = tk.Canvas(self, bg="#D3D3D3", height=500, width=500)
        self.canvas.grid(row=0, column=0, rowspan=6, columnspan=5, sticky="nsew")

app = Weather_App()
app.mainloop()