# Name: Arbeidskrav 2, PY1010
# Author: Benedikte Kristiansen
# Date: 
# Notes: Velger å importere moduler i hver oppgave slik at de kan kjøres individuelt
#################################################


#Oppgave 1
print('Hvilket år er du født?')
aar = int(input(''))
alder = 2025-aar
print('Du fyller', alder, 'i løpet av 2024')

#Oppgave 2
import math

antall_elever = int(input('Skriv inn antall elever: ' ))
pizza = math.ceil(antall_elever/4)
print('Dere trenger',pizza,'pizzaer til festen')

#Oppgave 3
import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180
print(f'{v_grad} grader tilsvarer {v_rad:.4f} radianer')

#Oppgave 4a,b
data = {
        'Norge': ['Oslo', 0.634],
        'England': ['London',  8.982],
        'Frankrike': ['Paris', 2.161],
        'Italia': ['Roma', 2.873]
        }

land = input('Skriv inn ett land : ')

if land in data:
    hovedstad, befolkning = data[land] 
    print(f'Hovedstaden i {land} er {hovedstad} og har en befolkning på {befolkning} millioner.') 
    
else: 
    print(f'{land} finnes ikke i databasen.')
    
#Oppgave 4c
data = {
        'Norge': ['Oslo', 0.634],
        'England': ['London',  8.982],
        'Frankrike': ['Paris', 2.161],
        'Italia': ['Roma', 2.873]
        }

land = input('Skriv inn ett nytt land : ')

while land in data:
    print(f'{land} finnes allerede i databasen.')
    land = input('Skriv inn ett nytt land: ')
    
hovedstad = input(f'Skriv inn hovedstaden i {land}')
befolkning = float(input(f'skriv inn anntall innbyggere i {hovedstad} (i millioner): '))

data[land] = [hovedstad, befolkning]

print('\nOppdatert database:')
for key, value in data.items():
    print(f'{key}: Hovedstad - {value[0]}, Befolkning - {value[1]} millioner')
    
#Oppgave 5
import math 

#Henter inn verdiene a og b i en rettvinklet trekant og regner ut hypotenusen
a = float(input('Skriv inn lengden på side A i trekanten: '))
b = float(input('Skriv inn lengden på side B i trekanten: '))
c = math.sqrt(a**2 + b**2)

#regner ut arealet og omkretsen av figurens komponenter
arealTrekant = 0.5*a*b
arealSirkel = math.pi*a**2
omkretsSirkel = 2*math.pi*a

#regner ut omkrets og areal av figuren
ArealFigur = arealTrekant + 0.5*arealSirkel
OmkretsFigur = b + c + 0.5*omkretsSirkel

#printer den utregnede omkretsen samt variablene som er brukt i regnestykket
print(f'Figuren i oppgaven har omkrets {OmkretsFigur:.2f}, regnet ut av halve sirkelen med r = {a}, b = {b} og hypotenusen til trekanten = {c:.2f}')
print(f'Figuren i oppgaven har areal {ArealFigur:.2f}, regnet ut fra halve arealet til sirkelen med r = {a}, og trekanten med sidene a = {a} og b = {b}')


#Oppgave 6
import numpy as np 
import matplotlib.pyplot as plt

#definerer intervallet
x = np.linspace(-10, 10, 200)

#definerer funksjonen
y = -x**2 - 5

#plotter
plt.plot(x,y) 
plt.title('Plot av funksjonen f(x) -x^2 - 5')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
