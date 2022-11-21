import os
import mysql.connector
from tkinter import *
from tkinter import filedialog
from facture import fact
import threading
from observateur import *



def show(c):
    listeVariableImportante = ["fichier"]
    fenetre = Tk()
    fenetre.geometry("800x600")
    fenetre.title("Facturas Serveur")
    serveurInterface(fenetre, c, listeVariableImportante)


    if (os.getcwd() == os.path.dirname(os.path.abspath(__file__))):
        w = Watcher("../simulation_reseau/requests")

    else :
        w = Watcher("simulation_reseau/requests")
    
    obs = threading.Thread(target=lambda : w.run(listeVariableImportante, c), daemon=True)
    obs.start()
    fenetre.mainloop()


def serveurInterface(f, c, lVI):
     # File to work on and more important variable, using a list to bypass immutable variable limitation
    loadFichier(f, c, lVI)
    commServeur(f)


# first half of server application

def choixFichier(l, f):
    
    fichier = filedialog.askopenfilename(initialdir = "../analyse",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

   
    f[0] = fichier
    nomFichier = fichier.split('/')
    taille = len(nomFichier)
    l.configure(text="Ouvert :"+nomFichier[taille-1])


def inclureBDD(connection, l, oL):

    succesnum = 0

    if connection != None:

        cursor = connection.cursor()

        # Checking if clients name already inside

        cursor.execute("""SELECT nom FROM Clients""")

        check = cursor.fetchall()
        for n in check :
            if n[0] == l[1]:
                # Clients already inside Database
                succesnum += 1
                cursor.execute("""SELECT num FROM Clients WHERE nom=(%s)""", (l[1],))
                selector_client = cursor.fetchall()
                break
        else:
            cursor.execute("""
                INSERT INTO Clients (nom, adresse) VALUES (%s, %s)
                """, (l[1], l[2]))
    
            selector_client = cursor.lastrowid
    
            succesnum += cursor.rowcount

        # Checking if entreprise already inside         
    
        cursor.execute("""SELECT siren FROM Entreprises""")

        check = cursor.fetchall()

        for s in check :
            if s[0] == l[5]:
                # Entreprises already inside

                succesnum += 1
                cursor.execute("""SELECT num FROM Entreprises WHERE siren=(%s)""", (l[5],))
                selector_entreprise = cursor.fetchall()
                break

        else:
            cursor.execute("""
                        INSERT INTO Entreprises (siren) VALUES (%s)""", (l[5],))
    
            selector_entreprise = cursor.lastrowid
    
            succesnum += cursor.rowcount
    
        prix = l[4].replace(",",".")
        cursor.execute("""
                        INSERT INTO Commandes (total) VALUES (%s)
                       """, (int(float(prix)),))
    
        succesnum += cursor.rowcount
    
        selector_commande = cursor.lastrowid
    
    
    for p in l[3]:
        if isinstance(selector_commande, int):
            cursor.execute("""
                    INSERT INTO Produits (numCommande, produit) VALUES (%s, %s)
        """, (selector_commande,p))
    
            succesnum += cursor.rowcount

        else:
            cursor.execute("""
                    INSERT INTO Produits (numCommande, produit) VALUES (%s, %s)
        """, (selector_commande[0],p))
    
            succesnum += cursor.rowcount  
    
        if isinstance(selector_client, int) and isinstance(selector_entreprise, int):
                cursor.execute(""" 
            INSERT INTO Factures (prix, numClient, numEntreprise, numCommande) VALUES (%s, %s, %s, %s)
    """, (int(float(prix)), selector_client, selector_entreprise, selector_commande))
        
        elif isinstance(selector_client, int):
            cursor.execute(""" 
            INSERT INTO Factures (prix, numClient, numEntreprise, numCommande) VALUES (%s, %s, %s, %s)
    """, (int(float(prix)), selector_client, selector_entreprise[0], selector_commande))
        else:
            cursor.execute(""" 
            INSERT INTO Factures (prix, numClient, numEntreprise, numCommande) VALUES (%s, %s, %s, %s)
    """, (int(float(prix)), selector_client[0], selector_entreprise[0], selector_commande))
        succesnum += cursor.rowcount



    if succesnum == (4 + len(l[3])):
        connection.commit()
        oL.configure(text="Inclusion\nOK")
    else :
        oL.configure(text="Inclusion\nNon OK")

    cursor.close()


def loadFichier(f, c, lVI):
   
    # Background of canvas
    canvas = Canvas(f, width=400, height=600)
    canvas.create_rectangle(0, 0, 398, 598, fill='#121212')

    # Placeholder if the user wants to read a file to addup to the dataset
    titleLabel = Label(canvas, text="Chargement Données", width=33, height= 1, font=('Arial', 15), background='#121212', foreground='white')
    titleLabel.place(x=15, y=1)


    # Selecting file widget

    canvas.create_rectangle(50,50, 300, 150, fill='#181818')

    chooseLabel= Label(canvas, text="Choisissez un fichier :",font=('Arial', 10), background="#121212", foreground='white')
    chosenFile = Label(canvas, text="Aucune fichier ouvert...",font=('Arial', 10), width=34)
    chooseButton = Button(canvas, text="choix...", font=('Arial', 10), background='#696969', width=31, command=lambda: choixFichier(chosenFile, lVI))

    chooseLabel.place(x = 52,y = 50)
    chooseButton.place(x = 52, y = 80)
    chosenFile.place(x = 52, y = 130)


    # Imputing file values in the BDD

    canvas.create_rectangle(50, 200, 300, 300, fill='#181818')

    # Label for starting loading file
    loadLabel= Label(canvas, text="Lire les données du fichier:",font=('Arial', 10), background="#121212", foreground='white')
    
    # Button for starting function
    loadButton = Button(canvas,text="Lecture", font=('Arial', 10), background='#696969', width=31, height= 5, command = lambda : fact(lVI, confirmLabel, valueLabel))

    loadLabel.place(x = 52, y=200)
    loadButton.place(x = 50, y = 220)
    


    # Display for confirmation of data included

    confirmLabel = Label(canvas, text="Attente de confirmation...", font=('Arial', 10), background="#181818", foreground='white')
    # Label for printing values
    valueLabel = Label(canvas, text="Aucune valeur pour le moment", font=('Arial', 8), background="#181818", foreground='white')

    confirmLabel.place(x = 52, y = 330)
    valueLabel.place(x = 52, y = 350)

    # Button for including in database

    if c == None :
        infoLabel = Label(canvas, text="Status de connection à la BDD : offline",font=('Arial', 10), background="#181818", foreground='white')
    else :
        infoLabel = Label(canvas, text="Status de connection à la BDD : online",font=('Arial', 10), background="#181818", foreground='white')
    
    if c != None:
        pushButton = Button(canvas, text="Inclure à la BDD", font=('Arial', 10), background='#696969', width=31, height= 2, command =lambda : inclureBDD(c, lVI, okLabel))
        okLabel = Label(canvas,font=('Arial', 10), text="",background="#181818", foreground='white')

    else :
        pushButton = Label(canvas, text="Impossible d'envoyer des données dans la BDD",font=('Arial', 10), background="#181818", foreground='white')

    infoLabel.place(x = 52, y=510)
    pushButton.place(x = 52, y=550)
    okLabel.place(x = 300, y=560)

    # For display if the include went fine


    canvas.place(x=0, y=0)


# Second half of the server application

def commServeur(f):
    canvas = Canvas(f, width=400, height=600)

    canvas.create_rectangle(0, 0, 395, 598, fill='#121212')

    # Placeholder for information about communication
    titleLabel = Label(canvas, text="Communications serveur", width=33, height= 1, font=('Arial', 15), background='#121212', foreground='white')
    titleLabel.place(x=15, y=1)

    canvas.place(x=402, y=0)