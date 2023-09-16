import tkinter as tk
from tkinter import *
from tkinter.font import nametofont
from PIL import ImageTk, Image
import random
import time
import threading
from playsound import playsound
import os
import units
import pygame


root = tk.Tk()
barra_menus = tk.Menu()
icon = PhotoImage(file='img/icoCloud.png')
root.iconphoto(False, icon)
root.title(" GIVE ME MONEY!")
root.geometry("485x700")
root.configure(background="#f0f0f0")
#root.attributes('-alpha',0.8)
root.resizable(False, False)
app = tk.Frame(root)
app.pack()

#Ya nse brother

#---------------------- Otros ---------------
#Variables globales
contador = 0 
MONEY = int(1)
CLONCE = int(100)
UpgradeCost = int(50)
BuyCost = int(100)

#Gacha
Summoned = None
Suerte = int(1) # Recuadro Random Boost

#Tipografia
font_obj = nametofont("TkDefaultFont")
font_obj.configure(family="Monocraft")
font_obj.configure(size=20)

#sonido1 = os.path.join("sounds\\coin.wav")

# sounds


def playCash_sound():
    playsound("sound\\cash.mp3")
def playCoin_sound():
    playsound("sound\\coin.mp3")
def playUpgrade_sound():
    playsound("sound\\Nom.mp3")
"""
def playPoor_sound():
    playsound("sound\\pipe.mp3")
"""
sonido = pygame.mixer.Sound("sound\\LVUp.wav")

# Función para reproducir el sonido en segundo plano
def playPoor_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sound\\LVUp.wav")
    pygame.mixer.music.play()


#--------------------- FUNCIONES ---------------------
def cambia_puntero(event):
    event.widget.configure(cursor="hand2")
def coolthread2():
    a = threading.Thread(target=playCoin_sound)
    a.daemon = True
    a.start()

def aumentar_contador():
    global contador
    contador += MONEY
    moneyText.config(text=str(contador) + "€")
    coolthread2()
    #root.after(1000, aumentar_contador)

def Visible():
    Label1.place(x = random.randint(1, 500), y = random.randint(1, 500))
    root.after(3000, Invisible)

def Invisible():
    Label1.place(x = 1000, y = 2000)

#---- GACHA FUNCION/CLASSE ----------
 
TresEstrellas = ["Cloud Nerd ", "Cloud Cool"]
CuatroEstrellas = ["Cloud Blue", "Cloud Red", "Cloud Green"]
CincoEstrellas = ["Drip AleDevO", "Drip ForkE"]

personajes = [
    units.Summon_All(1,"AleDriv", "⭐⭐⭐⭐⭐", "GACHA\\AleDriv.png"),
    units.Summon_All(2,"Cloud Blue", "⭐⭐⭐", "GACHA\\CB.png"),
    units.Summon_All(3,"Cloud Red", "⭐⭐⭐", "GACHA\\CG.png"),
    units.Summon_All(4,"Cloud Grenn", "⭐⭐⭐", "GACHA\\CR.png"),
    units.Summon_All(5,"ForkDriv", "⭐⭐⭐⭐⭐", "GACHA\\Fork.png"),
    units.Summon_All(6,"Cloud Nerd", "⭐⭐⭐⭐", "GACHA\\gafasnerd.png"),
    units.Summon_All(7,"Cloud Chad", "⭐⭐⭐⭐", "GACHA\\gafasSol.png"),
    units.Summon_All(8,"Killer Kirbe", "⭐⭐⭐⭐", "GACHA\\KirbyKiller.png"),
    units.Summon_All(9,"Cool Kirbe", "⭐⭐⭐", "GACHA\\KirbyGorra.png")
]



def SUMMON():
    #os.system('cls' if os.name == 'nt' else 'clear')
    global CLONCE

    if CLONCE >= 1:
        CLONCE -= 1
        numero = random.randint(1, 100)
        if numero in range(0, 6):
            Cinco_aleatorio = random.choice(CincoEstrellas)
            print(Cinco_aleatorio)
            print("Cinco estrellas")
            N_SUMMON_Text.config(text= str(Cinco_aleatorio), bg= "#f0f0f0")
            ThreeStarsText.place(x=1000, y=1000)
            FourStarsText.place(x=1000, y=1000)
            FiveStarsText.place(x=152, y=400)


        if numero in range(6, 46):
            Cuatro_aleatorio = random.choice(CuatroEstrellas)
            print(Cuatro_aleatorio)
            print("Cuatro estrellas")    
            N_SUMMON_Text.config(text= str(Cuatro_aleatorio), bg= "#f0f0f0") 
            ThreeStarsText.place(x=1000, y=1000)
            FiveStarsText.place(x=1000, y=1000)
            FourStarsText.place(x=170, y=400)


        if numero in range(46, 101):
            Tres_aleatorio = random.choice(TresEstrellas)
            print(Tres_aleatorio)
            print("Tres estrellas")
            N_SUMMON_Text.config(text= str(Tres_aleatorio), bg= "#f0f0f0")
            ThreeStarsText.place(x=187, y=400)
            FourStarsText.place(x=1000, y=1000)
            FiveStarsText.place(x=1000, y=1000)
    
        clonceText.config(text=str(CLONCE) + "💰")
        print(numero)

    
    
    else:
        print("NO TIENES CLOCES SUFICIENTES!")

#--- CAMBIO DE PAGINA BARRA ---

def SHOW_CLICKER():
    print("aaa")
    #RESTABLECER
    ContadorText.place(x=190, y=530)
    GetMoneyButton.place(x=140, y=570)
    BuyText.place(x=30, y=530)
    BuyButton.place(x=30, y=570)
    UpgradeText.place(x=350, y=530)
    UpgradeButton.place(x=310, y=570)
    my_label.place(x=200, y=200)
    moneyText.place(x=200, y=100)
    #ESCONDER SUMMON
    button.place(x=1000, y=1000)
    button.place(x=1000, y=1000)
    ThreeStarsText.place(x=1000, y=1000)
    FourStarsText.place(x=1000, y=1000)
    FiveStarsText.place(x=1000, y=1000)
    N_SUMMON_Text.place(x=1000, y=1000, anchor='nw')
    #Cloud ROJO
    my_label1.place(x=1200, y=2100)


def SHOW_SUMMON():
    print("eeee")
    # ESCONDER
    ContadorText.place(x=1000, y=1000)
    GetMoneyButton.place(x=140, y=1000)
    BuyText.place(x=1000, y=1000)
    BuyButton.place(x=1000, y=1000)
    UpgradeText.place(x=1000, y=1000)
    UpgradeButton.place(x=1000, y=1000)
    my_label.place(x=2000, y=2000)
    moneyText.place(x=2000, y=1000)

    #ENSEÑAR SUMMON
    button.place(x=175, y=570)
    
    N_SUMMON_Text.place(x=205, y=150, anchor='nw')
    #Cloud ROJO
    my_label1.place(x=195, y=200)
    



#------------------------ COMPRAR -------------------------
def coolthread():
    t = threading.Thread(target=playCash_sound)
    t.daemon = True
    t.start()

def coolthread4():
    a = threading.Thread(target=playPoor_sound)
    a.daemon = True
    a.start()


def Comprar1():
    global contador
    global BuyCost
    global CLONCE
    if contador >= BuyCost:
        print("Compraste!")
        contador -= BuyCost
        BuyCost += 100
        BuyText.config(text=str(BuyCost) + "€")
        moneyText.config(text=str(contador) + "€")
        CLONCE += 1
        clonceText.config(text=str(CLONCE) + "💰")
        coolthread()
    else:
        print("eres pobre!")
        #coolthread4()
        sound_thread = threading.Thread(target=playPoor_sound())
        sound_thread.start()
        playPoor_sound()
        Visible()



#------------------------ UPGRADES ------------------------
def coolthread3():
    a = threading.Thread(target=playUpgrade_sound)
    a.daemon = True
    a.start()

def Upgrades():
    global contador
    global MONEY
    global UpgradeCost
    if contador >= UpgradeCost:
        print("Upgrade!")
        coolthread3()
        MONEY *= 2
        contador -= UpgradeCost
        UpgradeCost += UpgradeCost
        UpgradeText.config(text=str(UpgradeCost) + "€")
        ContadorText.config(text="x"+ str(MONEY))
        moneyText.config(text=str(contador) + "€")
        #Upgrade secreto
        RandomSuerte = random.randint(1, 100)
        if RandomSuerte == Suerte:
            print("LUCKY!")
            VisibleSecret()
            coolthread3()

    else:
        print("eres pobre!")
        #coolthread4()
        playPoor_sound()
        Visible()
            

def UpgradeClick():
    global MONEY
    print("AH!")
    MONEY += random.randint(1, 5)
    ContadorText.config(text="x"+ str(MONEY))



def VisibleSecret():
    SecretUpgradeButton.place(x=random.randint(1, 400), y=random.randint(1, 400))
    root.after(3000, InvisibleSecret)

def InvisibleSecret():
    SecretUpgradeButton.place(x=random.randint(1, 5000), y=random.randint(1, 5000))



#----------------------- BOTONES ---------------------

# Parte baja Botones
lower_frame = Frame(root, bg= "black", width= 560, height= 150)
lower_frame.place(x=-20, y=520)

# CURRENCY (MONEYEEEEEAA)
moneyText = Label(root, text="0" + " €")
moneyText.place(x=200, y=100)

clonceText = Label(root, text="0" + "💰")
clonceText.place(x=20, y=470)

#-------- TRAJES/ BANNERS -------

#Cloud DEFAULT
my_img = ImageTk.PhotoImage(Image.open("img/ff8.png"))
my_label = Label(image=my_img)
my_label.place(x=200, y=200)


#Cloud ROJO
my_img1 = ImageTk.PhotoImage(Image.open("img/CR.png"))
my_label1 = Label(image=my_img1)
my_label1.place(x=1200, y=1200)

"""
#Cloud VERDE
my_img2 = ImageTk.PhotoImage(Image.open("img/CV.png"))
my_label2 = Label(image=my_img2)
my_label2.place(x=200, y=200)

#Cloud AZUL
my_img3 = ImageTk.PhotoImage(Image.open("img/CA.png"))
my_label3 = Label(image=my_img3)
my_label3.place(x=200, y=200)
"""




#------------------------------- Botones principales CLICKER -------------------------

#BOTON CLICK
ContadorText = Label(root, text= "x"+ str(MONEY), bg= "black")
ContadorText.config(fg="white")
ContadorText.place(x=190, y=530)
GetMoneyButton = tk.Button(root, text = "Money!", command= aumentar_contador , borderwidth=0, bg="green")
GetMoneyButton.place(x=140, y=570)

#BOTON BUY
BuyText = Label(root, text= str(BuyCost) + "€", bg= "black")
BuyText.config(fg="white")
BuyText.place(x=30, y=530)
BuyButton = tk.Button(root, text = "BUY", command= Comprar1 , borderwidth=0, bg="yellow")
BuyButton.place(x=30, y=570)

#BOTON UPGARDE
UpgradeText = Label(root, text= str(UpgradeCost) + "€", bg= "black")
UpgradeText.config(fg="white")
UpgradeText.place(x=350, y=530)
UpgradeButton = tk.Button(root, text = "UPGRADE", command= Upgrades , borderwidth=0, bg="blue")
UpgradeButton.place(x=310, y=570)

#SECRET BOTON UPGARDE
SecretUpgradeButton = tk.Button(root, text = "!!!", borderwidth=0, bg="red", command = UpgradeClick)
SecretUpgradeButton.config(fg="black")

#------------------------------- Botones principales SUMMON -------------------------

button = Button(root, text="SUMMON", command=SUMMON)
button.place(x=1000, y=1000)

ThreeStarsText = Label(root, text= "⭐⭐⭐", bg= "#f0f0f0",justify="center")
ThreeStarsText.config(fg="brown")
ThreeStarsText.place(x=1000, y=1000, anchor='nw')

FourStarsText = Label(root, text= "⭐⭐⭐⭐", bg= "#f0f0f0",justify="center")
FourStarsText.config(fg="silver")
FourStarsText.place(x=1000, y=1000, anchor='nw')

FiveStarsText = Label(root, text= "⭐⭐⭐⭐⭐", bg= "#f0f0f0",justify="center")
FiveStarsText.config(fg="gold")
FiveStarsText.place(x=1000, y=1000, anchor='nw')

N_SUMMON_Text = Label(root, text= Summoned, bg= "#f0f0f0",justify="center")
N_SUMMON_Text.config(fg="black")
N_SUMMON_Text.place(x=1000, y=1000, anchor='nw')



#---------------------- BARRA DE MENUS ---------------

archivo_menu = tk.Menu(barra_menus, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_command(label="Guardar")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

pagGacha = tk.Menu(barra_menus, tearoff=0)
pagGacha.add_command(label="CLICKER", command= SHOW_CLICKER)
pagGacha.add_command(label="SUMMON", command= SHOW_SUMMON)


barra_menus.add_cascade(label="Archivo", menu=archivo_menu)
barra_menus.add_cascade(label="SWAP", menu=pagGacha)

root.config(menu=barra_menus)

#------------------- EXTRAS ------------------------
Label1 = Label(root, text= "POBRE!")

#--------------------------------------------------
#crear_boton_aleatorio()
#Ejecucion
root.bind("<Enter>", cambia_puntero)
root.mainloop()