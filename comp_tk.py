# -*- coding: utf-8 -*-

# comp_tk.py
# Dani Suarez - suarezdanieltomas@gmail.com
# GUI spectra comparator with tkinter

import os
import tkinter
from tkinter import filedialog

from comparator import read_names, find_files, create_dfs, compare, plot_all

home = os.path.expanduser('~/Documents')
font_M = "Arial 12"
fc = "white"
bg = "#154569"
dfs = []
show_peaks = True
xlim = None


def opendir():
    global data_folder
    data_folder = filedialog.askdirectory(initialdir=home)
    entry1.delete(0, 50)
    entry1.insert(0, data_folder)


def load():
    global dfs
    global archivos
    global nombres
    nom_path = ""
    for root_, dirs, files in os.walk(f"{os.path.join(data_folder, '..')}"):
        for name in files:
            if name == "nombres.txt":
                nom_path = os.path.join(root_, name)

    archivos = find_files(data_folder)
    if not nom_path:
        nombres = [i for i in range(len(archivos))]
    else:
        nombres = read_names(nom_path)
    dfs = create_dfs(archivos, nombres)


def refresh():
    global show_peaks
    global xlim
    if not lmin_entry.get() or not lmax_entry.get():
        xlim=None
    if show_peaks_entry.get() != "0":
        show_peaks = True


def graph():
    global xlim
    global show_peaks
    refresh()
    if show_peaks_entry.get() == "0":
        show_peaks = 0
    if not dfs:
        load()
    if lmin_entry.get() and lmax_entry.get():
        xlim = [int(lmin_entry.get()), int(lmax_entry.get())]
    
    meds = entry2.get().split(",")
    meds = [int(i) for i in meds]  
    if title_entry.get():
        compare(meds, dfs, nombres, title=title_entry.get(), xlim=xlim, peaks=int(show_peaks))
    else:
        compare(meds, dfs, nombres, xlim=xlim, peaks=int(show_peaks))


def quilombo():
    if not dfs:
        load()
    plot_all(dfs, nombres)


def enter_key(event):
    graph()


root = tkinter.Tk()
root.geometry("650x500")
root.iconbitmap("pokeball.ico")
root.title("Comparador de espectros")  # Spectra comparator
root.configure(bg=bg)

root.grid_columnconfigure((0, 1), weight=1)

# Choose folder dialog
lab_title = tkinter.Label(root, text="Comparador de espectros",
                          font="Arial 18 bold", bg=bg, fg=fc)
lab_title.grid(row=0, column=0, pady=5, columnspan=2)

butt_open = tkinter.Button(root, text="Choose Folder", command=opendir,
                           font=font_M)
butt_open.grid(row=1, column=0, pady=5, sticky="e")

entry1 = tkinter.Entry(root, bd=3, font="Arial 10", width=60)
entry1.grid(row=1, column=1, pady=5)


# Prompt text indicating the input format
prompt = tkinter.Label(root, text="Ingresá los números de las mediciones separados por comas", font="Arial 12", bg=bg, fg=fc, bd=0, width=50)
prompt.grid(row=3, columnspan=2, pady=10)

entry2 = tkinter.Entry(root, bd=3, font=font_M, width=15)
entry2.grid(row=4, columnspan=2)


butt_graph = tkinter.Button(root, text="Graficar", font=font_M, command=graph)
butt_graph.grid(row=5, columnspan=2, pady=5)


# Graph with enter key
root.bind("<Return>", enter_key)


# Aditional settings
cfg_lab = tkinter.Label(root, text="-"*100+"\nConfiguración adicional "
                        "(opcional)\nDejar vacío para usar valores automáticos",
                        font=font_M, bg=bg, bd=0, width=100, fg=fc)
cfg_lab.grid(row=6, columnspan=2, pady=20)

title_lab = tkinter.Label(root, text="Título del gráfico", font=font_M, bg=bg,
                          bd=3, fg=fc)
title_lab.grid(row=7, column=0, sticky="e")

title_entry = tkinter.Entry(root, bd=3, font=font_M, width=40)
title_entry.grid(row=7, column=1, sticky="w", padx=10)

lmin_lab = tkinter.Label(root, text=f"{chr(955)} mín", font=font_M, bg=bg,
                         fg=fc)
lmin_lab.grid(row=8, column=0, pady=5, sticky="e")

lmin_entry = tkinter.Entry(root, bd=3, font=font_M, width=40)
lmin_entry.grid(row=8, column=1, sticky="w", padx=10)

lmax_lab = tkinter.Label(root, text=f"{chr(955)} máx", font=font_M, bg=bg,
                         fg=fc)
lmax_lab.grid(row=9, column=0, sticky="e")

lmax_entry = tkinter.Entry(root, bd=3, font=font_M, width=40)
lmax_entry.grid(row=9, column=1, sticky="w", padx=10)

show_peaks_lab = tkinter.Label(root, text=f"{chr(955)} en picos (0/1)",
                               font=font_M, bg=bg, fg=fc)
show_peaks_lab.grid(row=10, column=0, sticky="e")

show_peaks_entry = tkinter.Entry(root, bd=3, font=font_M, width=40)
show_peaks_entry.grid(row=10, column=1, pady=5, sticky="w", padx=10)

no_tocar = tkinter.Button(root, text="No tocar (o sí)", font="Times 8",
                          command=quilombo)  # Plot all
no_tocar.grid(row=11, columnspan=2, pady=20)


sign = tkinter.Label(root, text="Dani Suarez / suarezdanieltomas@gmail.com",
                     font="Calibri 10", bg=bg, fg=fc)
sign.grid(row=12, column=1, pady=1, sticky="e", padx=1)


root.mainloop()
