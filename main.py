import tkinter as tk
import requests as r
from tkinter import ttk
import customtkinter as ctk

class Weather_App(tk.Tk):
    #Initialize the window
    def __init__(self):
        super().__init__()
        self.title("Welcome to the weather app")
        self.config(padx=3, pady=3)

        self.canvas = tk.Canvas(self, bg="#bcd3d4", height=500, width=500)
        self.canvas.grid(row=0, column=0, rowspan=6, columnspan=5, sticky="nsew")
        
        self.get_weather_data_button = ctk.CTkButton(self, text="Show Forecast", fg_color="#817fa0", hover_color="#9A98B8", text_color="#2B2B2F", 
                                                     font=("Times New Roman", 20, "italic"), border_width=1, border_color="#2B2B2F", anchor="center")
        self.get_weather_data_button.grid(row=1, column=4)

        self.exit_button = ctk.CTkButton(self, text="Exit Application", fg_color="#8c5f6a", hover_color="#b07d88", text_color="#2B2B2F",
                                         font=("Times New Roman", 20, "italic"), border_width=1, border_color="#2B2B2F", anchor="center")
        self.exit_button.grid(row=0, column=4)

app = Weather_App()
app.mainloop()