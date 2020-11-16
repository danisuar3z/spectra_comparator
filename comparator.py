# -*- coding: utf-8 -*-

# comparator.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Spectra comparator

import os

import matplotlib.pyplot as plt
import pandas as pd


def find_peaks(x, y, n=50):
    """
    Not a good peak finder but it is what I quickly made.
    The 'n' parameter is the number of points to check to both sides
    to tell if a point is a peak or not so it doesn\'t work well if
    you have a peak near the edge of the spectra.
    Returns a tuple with xy of the absolute max and a list with xy
    for the local maximums, if there is any.
    """
    abs_max_y = max(y)
    abs_max_x = x[y.index(abs_max_y)]
    abs_max = (abs_max_x, abs_max_y)
    ind = list(range(len(x)))

    loc_max = []
    for i, xi, yi in zip(ind, x, y):
        if xi == abs_max_x or i in ind[:n+1] or i in ind[-n-1:]:
            pass
        else:
            if (xi, yi) in loc_max:
                continue
            elif (yi > max(y[i-n:i]) and yi > max(y[i+1:i+n])):
                # print('\nDEBUG:', xi, yi, y[i-10:i+10], '\n')
                loc_max.append((xi, yi))
    # print('DEBUG:', loc_max)
    return abs_max, loc_max


def find_files(folder):
    archivos = []
    for root, dirs, files in os.walk(folder):
        for name in files:
            if not name.endswith(".txt") or name == "nombres.txt":
                continue
            archivos.append(os.path.join(root, name))
    return archivos


def read_names(file):
    """
    Needs a text file with the same amount of lines as files
    with the data label in each line.
    """
    with open(file, "rt") as f:
        nombres = [i.strip() for i in f.readlines()]
    return nombres


def create_dfs(archivos, nombres):
    dfs = []
    for i, archivo in enumerate(archivos):
        df = pd.read_table(archivo, names=["x", "y"])
        # df.name = archivo.split("\\")[-1].split(".")[0].replace("a", "a ")
        df.name = nombres[i]
        dfs.append(df)
    return dfs


def plot_all(dfs, nombres):
    # global nombres
    plt.title("Un lindo quilombo")
    plt.xlabel("Longitud de onda / $nm$")
    plt.ylabel("Intensidad / $ua$")
    for df in dfs:
        plt.plot(df.x, df.y)
        plt.legend(nombres, loc="upper right", ncol=2)
    figure = plt.gcf()
    figure.set_size_inches(12, 6)
    plt.show()


def plot_i(i, dfs):
    df = dfs[i-1]
    plt.plot(df.x, df.y)


def compare(medidas, dfs, nombres, peaks=True, loc="best",
             title="Comparación medidas", xlim=[], ylim=[], legend=[]):
    # nonlocal dfs
    # medidas = input("Ingresá los números de medidas separados por comas"
                    # "\nEjemplo: 1,4,5\n--> ")
    # medidas = [i for i in map(int, medidas.split(","))]
    # plt.style.use("tableau-colorblind10")
    # plt.tight_layout()
    for i in medidas:
        plt.title(title)
        plt.xlabel("Longitud de onda / $nm$")
        plt.ylabel("Intensidad / $ua$")
        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(ylim)
        plt.grid(True, axis="both", linestyle="--")
        plot_i(i, dfs)
        if peaks:
            max_, locs = find_peaks(dfs[i-1].x.to_list(), dfs[i-1].y.to_list(), 30)
            plt.annotate(str(max_[0]), (max_[0], max_[1]))
            if locs:
                for loc in locs:
                    plt.annotate(str(loc[0]), (loc[0] + 1, loc[1]))
        if legend:
            plt.legend(legend, loc=loc, framealpha=0.9)
        else:
            noms = [nombres[i-1] for i in medidas]
            # print(noms)
            plt.legend(noms, loc=loc, framealpha=0.9)


    plt.show()
