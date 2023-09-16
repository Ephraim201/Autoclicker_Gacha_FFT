from tkinter import *
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')


root = Tk()
root.geometry("500x500")

TresEstrellas = ["Juan", "Pedro", "María", "Luisa"]
CuatroEstrellas = ["Manoo", "Jose", "Maríana", "Ano"]
CincoEstrellas = ["JohnCena", "Chuk", "Simpsom", "Obama"]


def print_text():
    os.system('cls' if os.name == 'nt' else 'clear')

    numero = random.randint(1, 100)
    if numero in range(0, 6):
        Cinco_aleatorio = random.choice(CincoEstrellas)
        print(Cinco_aleatorio)
        print("Cinco estrellas")
    
    if numero in range(6, 46):
        Cuatro_aleatorio = random.choice(CuatroEstrellas)
        print(Cuatro_aleatorio)
        print("Cuatro estrellas")
    
    if numero in range(46, 101):
        Tres_aleatorio = random.choice(TresEstrellas)
        print(Tres_aleatorio)
        print("Tres estrellas")
   
    print(numero)

button = Button(root, text="Imprimir", command=print_text)
button.pack()

root.mainloop()