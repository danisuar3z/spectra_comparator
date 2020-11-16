from comparator import find_peaks, find_files, read_names, create_dfs, plot_i, compare

archivos = find_files(R"C:\Users\Daniel\Documents\Facultad\Facu\Instrumental\Modulo biologico\1- Fluorescencia\datos")
nombres = read_names(R"C:\Users\Daniel\Documents\Facultad\Facu\Instrumental\Modulo biologico\1- Fluorescencia\nombres.txt")
dfs = create_dfs(archivos, nombres)

medidas = [11,17,18,19,21]
titulo = "Control Dansilo"
peaks = 1
loc = "center left"
ylim = []
compare(medidas, dfs, nombres, peaks=peaks, loc=loc, title=titulo, ylim=ylim)

# M11: BSA-DS en Tris   emisión 339nm
# M17: BSA-DS en GdmCl emisión 339nm
# M18: DS en Tris     emisión  295nm
# M19: DS en Tris     emisión  339nm
# M21: DS en GdmCl    emisión  339nm
