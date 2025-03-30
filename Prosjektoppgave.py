# Name: Prosjektoppgave, PY1010
# Author: Benedikte Kristiansen
# Date: 30.03.2025
# Notes: Modulene importeres først
#        Velger å løse oppgaven som er foreslått
#################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

##############################################################
# del a)
##############################################################

# Les inn xlsx-filen
filnavn = "support_uke_24.xlsx"
data = pd.read_excel(filnavn)

# Lagre data fra de spesifikke kolonnene i arrays
u_dag = data.iloc[:, 0].to_numpy()  # Kolonne 1
kl_slett = data.iloc[:, 1].to_numpy()  # Kolonne 2
varighet = data.iloc[:, 2].to_numpy()  # Kolonne 3
tilfredshet = data.iloc[:, 3].to_numpy()  # Kolonne 4

# Print arrays for å bekrefte at data er lastet riktig
print("u_dag:", u_dag)
print("kl_slett:", kl_slett)
print("varighet:", varighet)
print("tilfredshet:", tilfredshet)

##############################################################
# del b)
##############################################################

# Lagre kolonne 1 som inneholder ukedager
u_dag = data.iloc[:, 0].to_numpy()  # Kolonne 1

# Telle antall henvendelser for hver ukedag
unik_dager, antall_henvendelser = np.unique(u_dag, return_counts=True)

# Definer ønsket rekkefølge for ukedagene
ordered_days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]

# Sorter ukedager og antall henvendelser basert på ønsket rekkefølge
sorted_indices = [ordered_days.index(day) for day in unik_dager]
unik_dager_sorted = [unik_dager[i] for i in np.argsort(sorted_indices)]
antall_henvendelser_sorted = [antall_henvendelser[i] for i in np.argsort(sorted_indices)]

# Visualiser med søylediagram
plt.bar(unik_dager_sorted, antall_henvendelser_sorted, color='skyblue')
plt.title("Antall henvendelser per ukedag")
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

##############################################################
# del c)
##############################################################

# Finn korteste og lengste samtaletid
korteste_varighet = np.min(varighet)  # Bruker NumPy
lengste_varighet = np.max(varighet)  # Bruker NumPy

# Print resultatene
print(f"Den korteste samtaletiden er: {korteste_varighet} minutter")
print(f"Den lengste samtaletiden er: {lengste_varighet} minutter")

##############################################################
# del d)
##############################################################

# Konverter tidsformat hh:mm:ss til total tid i minutter
def tidsformat_til_minutter(tid_str):
    h, m, s = map(int, tid_str.split(':'))
    return h * 60 + m + s / 60

# Konverter varighet til numeriske verdier i minutter
varighet_minutter = np.array([tidsformat_til_minutter(tid) for tid in varighet])

# Beregn gjennomsnittlig samtaletid
gjennomsnitt_varighet = np.mean(varighet_minutter)

# Print resultatet
print(f"Den gjennomsnittlige samtaletiden er: {gjennomsnitt_varighet:.2f} minutter")

##############################################################
# del e)
##############################################################

# Konverter kl_slett til timetall (antatt format 'HH:MM:SS')
def hent_timer(tid_str):
    return int(tid_str.split(":")[0])

# Ekstraher timeverdier
tid_timer = data.iloc[:, 1].apply(hent_timer)  # Kolonne 2 antas å være 'kl_slett'

# Definer tidsintervallene
bolker = {
    "08-10": (8, 10),
    "10-12": (10, 12),
    "12-14": (12, 14),
    "14-16": (14, 16)
}

# Tell antall henvendelser per tidsbolk
henvendelser_per_bolk = {}
for navn, (start, slutt) in bolker.items():
    henvendelser_per_bolk[navn] = ((tid_timer >= start) & (tid_timer < slutt)).sum()

# Visualiser resultatet som et sektordiagram
labels = henvendelser_per_bolk.keys()
values = henvendelser_per_bolk.values()

plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink'])
plt.title("Fordeling av supporthenvendelser per tidsbolk")
plt.axis('equal')  # Sikrer at diagrammet ser sirkulært ut
plt.show()

##############################################################
# del f)
##############################################################

# Fjern rader med manglende tilfredshet
data = data.dropna(subset=["Tilfredshet"])

# Klassifiser kunder basert på tilfredshet
score_ranges = {"Detractors": (1, 6), "Passives": (7, 8), "Promoters": (9, 10)}
categories = {key: data["Tilfredshet"].between(low, high).sum() for key, (low, high) in score_ranges.items()}

# Beregn prosentandeler for hver kategori
totale_kunder = sum(categories.values())
prosent = {key: (value / totale_kunder) * 100 for key, value in categories.items()}

# Data for NPS tabell
nps_table_data = [
    ["Detractors", categories["Detractors"], f"{prosent['Detractors']:.2f}%", "Total"],
    ["Passives", categories["Passives"], f"{prosent['Passives']:.2f}%", ""],
    ["Promoters", categories["Promoters"], f"{prosent['Promoters']:.2f}%", totale_kunder],
]

# Beregn NPS
nps = prosent["Promoters"] - prosent["Detractors"]
print(f"Net Promoter Score (NPS): {math.ceil(nps)}")

# Data for Score tabell
score_distribution = data["Tilfredshet"].value_counts().reindex(range(1, 11), fill_value=0)
horizontal_table_data = [
    list(score_distribution.values),  # Første rad: Antall
    list(range(1, 11)),               # Andre rad: Score
]

# Opprett figuren med to separate tabeller
fig, ax = plt.subplots(figsize=(10, 8)) 
ax.axis("tight")
ax.axis("off")

# Opprett Score tabell
horizontal_table = ax.table(cellText=horizontal_table_data, bbox=[0.1, 0.7, 0.8, 0.2], cellLoc="center")
horizontal_table.auto_set_font_size(False)
horizontal_table.set_fontsize(12)
horizontal_table.scale(1.2, 1.5)

# Fargelegg kolonner i Score tabell
for (row, col), cell in horizontal_table.get_celld().items():
    if 0 <= col <= 5:  # Kolonner 1-6 (rødt)
        cell.set_facecolor("lightcoral")
    elif 6 <= col <= 7:  # Kolonner 7-8 (gult)
        cell.set_facecolor("gold")
    elif 8 <= col <= 9:  # Kolonner 9-10 (grønt)
        cell.set_facecolor("lightgreen")
    

    if row == 1:
        cell.set_text_props(fontweight="bold")

# Opprett NPS tabell
vertical_table = ax.table(cellText=nps_table_data, bbox=[0.1, 0.1, 0.8, 0.5], cellLoc="center")
vertical_table.auto_set_font_size(False)
vertical_table.set_fontsize(12)
vertical_table.scale(1.2, 1.5)

# Fargelegg NPS tbell
for (row, col), cell in vertical_table.get_celld().items():
    if col == 3:  # Kolonne 4 (fjerner farge)
        cell.set_facecolor("white")
    elif row == 0:  # Detractors
        cell.set_facecolor("lightcoral")
    elif row == 1:  # Passives
        cell.set_facecolor("gold")
    elif row == 2:  # Promoters
        cell.set_facecolor("lightgreen")

# Tittel
fig.suptitle(f"Net Promoter Score: {math.ceil(nps)}", fontsize=16, fontweight="bold")

# Vis figuren
plt.show()