import tkinter as tk

from tkinter import messagebox

class nfcGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message", command=self.show_massage)
        self.actionmenu.add_command(label="Configure Tegninger", command=self.show_massage)

        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")

        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text="MatemaTegninger", font=('Times New Roman', 20))
        self.label.pack(padx=100,pady=10)

        self.check_state = tk.IntVar()

        self.button = tk.Button(self.root, text="Show Problem", font=('Times New Roman', 18), command=self.show_massage)
        self.button.pack(padx=100, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_massage(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

nfcGUI()