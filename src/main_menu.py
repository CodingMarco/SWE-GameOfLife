import tkinter as tk
import presets


def show_main_menu():
    tk_app = tk.Tk()
    tk_app.title("Conway's Game of Life")

    mainframe = tk.Frame(tk_app)
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    preset_chosen = tk.StringVar(tk_app)
    preset_chosen.set(next(iter(presets.presets_dict.keys())))

    menu = tk.OptionMenu(mainframe, preset_chosen, *list(presets.presets_dict.keys()))
    tk.Label(mainframe, text="Choose a preset").grid(row=1, column=1)
    menu.grid(row=2, column=1)

    ok_button = tk.Button(mainframe, text="Ok")
    ok_button.grid(row=3, column=1)

    tk_app.mainloop()
    return preset_chosen.get()


