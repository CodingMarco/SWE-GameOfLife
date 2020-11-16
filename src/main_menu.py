import tkinter as tk
import presets


class MainMenu:
    def __init__(self):
        self.exit = False
        self.preset_chosen: str = ""

        self._tk_app = tk.Tk()
        self._hide_tk_window()
        self._tk_app.title("Conway's Game of Life")
        self._tk_app.protocol("WM_DELETE_WINDOW", self._on_close_clicked)

        self._mainframe = tk.Frame(self._tk_app)
        self._init_mainframe()

        preset_names = list(presets.presets_dict.keys())

        self._preset_chosen_tk_var = tk.StringVar(self._tk_app)
        self._preset_chosen_tk_var.set(preset_names[0])

        tk.Label(self._mainframe, text="Choose a preset:").grid(row=0, column=0, columnspan=2)
        tk.OptionMenu(self._mainframe, self._preset_chosen_tk_var, *preset_names).grid(row=1, column=0, columnspan=2)
        tk.Button(self._mainframe, text=" Exit ", command=self._on_close_clicked).grid(row=2, column=0)
        tk.Button(self._mainframe, text="  Ok  ", command=self._on_ok_clicked).grid(row=2, column=1)

    def show(self):
        self._show_tk_window()
        self._tk_app.mainloop()

    def _init_mainframe(self):
        self._mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self._mainframe.columnconfigure(1, weight=1, minsize=100)
        self._mainframe.rowconfigure(1, weight=1, minsize=60)
        self._mainframe.rowconfigure(2, weight=1, minsize=100)
        self._mainframe.pack(pady=100, padx=200)

    def _show_tk_window(self):
        self._tk_app.deiconify()

    def _hide_tk_window(self):
        self._tk_app.withdraw()

    def _on_close_clicked(self):
        self.exit = True
        self._tk_app.destroy()

    def _on_ok_clicked(self):
        self.preset_chosen = self._preset_chosen_tk_var.get()
        self._hide_tk_window()
        self._tk_app.quit()
