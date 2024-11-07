# Name: Arbeidskrav 1, PY1010
# Author: Benedikte Kristiansen
# Date: 06.11.2024

##################################################

D = 10000   # Distanse i km/år
Fe = 5000   # Forsikring elbil pr år
Fb = 7500   # Forsikring bensinbil pr år
Tfa = 8.38*365  # Trafikkforsikringsavgift pr år
Dfe = 0.2   # Drivstoff forbruk for Elbil i kWh/km
S=2         # Pris strøm i kr/kWh
Dfb = 1     # Drivstoff forbruk for bensinbil i kr/km
Be = 0.1    # Bomavgift elbil i kr pr km
Bb = 0.3    # Bomavgift bensinbi i kr pr km

DFE = S*Dfe*D  # Kalkyle drivstoff forbruk Elbil pr år
DFB = Dfb*D    # Kalkyle drivstoff forbruk Bensinbil pr år

BE = D*Be  # Kalkyle bomavgift elbil pr D km
BB = D*Bb  # Kalkye bomavgift bensinbil pr D km

UBB = BB + DFB + Tfa + Fb  # Totale Utgifter Bensin Bil

UEB = BE + DFE + Tfa + Fe  # Totale Utgifter El Bil


print("Forsikring:")
print("Elbil:",Fe)
print("Bensinbil:",Fb)
print("Elbil er", Fb-Fe, "Kr billigere pr år")
print()
print("Drivstoff:")
print("Elbil:",DFE)
print("Bensinbil:",DFB)
print("Elbil er",DFB-DFE, "Kr billigere pr", D, "Km kjørt pr år" )
print()
print("Bom:")
print("Elbil:",BE)
print("Bensinbil:",BB)
print("Elbil er",BB-BE, "Kr billigere i bom pr", D, "Km kjørt pr år" )
print()
print("Trafikkforsikringsavgift begge:", Tfa*365)


print("Årlig totalkostnad:")
print("Elbil: ", UEB)
print("Bensinbil:" ,UBB)
print("Elbil er", UBB-UEB,"kr billigere i drift pr år ved", D,"Kjørte km")