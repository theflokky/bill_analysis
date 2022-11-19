from tkinter import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
from observer import *

def getMessage1(window, clientNameInput, startingDateInput, endingDateInput, enterpriseNameInput):
    clientName = clientNameInput.get()
    startingDate = startingDateInput.get()
    endingDate = endingDateInput.get()
    enterpriseName = enterpriseNameInput.get()

    if (clientName == ''):
        print("Error : Client Name Empty")
    elif (startingDate == '' and endingDate == '' and enterpriseName == ''):
        print("Error : EmptyFields")
    elif (enterpriseName == '') and (startingDate != '' and endingDate != ''):
        print("Date Case")
        # Launching JSON Generation Process

        awaitingResponse()
        total = readJson()
        results1OnlyDateInterface(window, total, clientName,  startingDate, endingDate)
    elif (enterpriseName != '') and (startingDate != '' and endingDate != ''):
        print("Date and Enterprise Case")
        # Launching JSON Generation Process

        awaitingResponse()
        total =readJson()
        results1AllInterface(window, total, clientName, startingDate, endingDate, enterpriseName)
    elif (enterpriseName != '') and (startingDate == '' and endingDate == ''):
        print("Enterprise case")
        # Launching JSON Generation Process

        awaitingResponse()
        total = readJson()
        results1OnlyEnterpriseInterface(window, total, clientName, enterpriseName)


def getMessage2(window, clientNameInput, productNameInput):
    clientName = clientNameInput.get()
    productName = productNameInput.get()

    if (clientName == '' or productName == ''):
        print("Error : Empty Fields")
    else:
        # Launching the JSON Generation Process

        # Awaiting for the response
        awaitingResponse()
        enterpriseList = readJson()
        results2Interface(window, enterpriseList, clientName, productName)

def display():
    window = Tk()
    window.geometry("1202x602")
    window.title('Facturas')
    homeInterface(window)
    window.mainloop()


# Function that is displaying the non-dynamic component
def homeInterface(window):
    # Interface for the first message
    #startingDate = StringVar()
    #startingDate.set("Entrez la date de début (Optionnel)")
    #startingDateInput = Entry(window, textvariable=startingDate, width=30)
    # startingDateInput.pack()
    message1Interface(window)
    message2Interface(window)
    resultsBaseInterface(window)


def message1Interface(window):
    # Background of the Canvas
    canvas = Canvas(window, width=600, height=400)
    canvas.create_rectangle(0, 0, 600, 600, fill='#121212')

    # Form of the Message1
        #message1 title
    titleLabel = Label(canvas, text='Message 1', width= 15, height=2, font=('Arial', 15), background='#121212', foreground='white')
    titleLabel.place(x=220, y=10)

    #message description
    descriptionLabel = Label(canvas, text='Vous retourne le total de vos factures sur une période et/ou pour une \nentreprise spécifique.', font=('Arial', 10), background='#121212', foreground='white')
    descriptionLabel.place(x=100, y=70)

    #Rectangle wich will contain the form
    canvas.create_rectangle(150, 120, 450, 273, fill='#181818')
    # clientName
    clientNameLabel = Label(canvas, text="Nom du Client :", font=('Arial', 10), background="#121212", foreground='white')
    clientNameInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    clientNameLabel.place(x=165, y=135)
    clientNameInput.place(x=280, y=135)

    # starting date
    startingDateLabel = Label(canvas, text="Date de Début :", font=('Arial', 10), background="#121212", foreground='white')
    startingDateInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    startingDateLabel.place(x=165, y=170)
    startingDateInput.place(x=280, y=170)

    # ending date
    endingDateLabel = Label(canvas, text="Date de Fin :", font=('Arial', 10), background="#121212", foreground='white')
    endingDateInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    endingDateLabel.place(x=165, y=205)
    endingDateInput.place(x=280, y=205)

    # enterprise name
    enterpriseNameLabel = Label(canvas, text="N°SIREN :", font=('Arial', 10), background="#121212", foreground='white')
    enterpriseNameInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    enterpriseNameLabel.place(x=165, y=240)
    enterpriseNameInput.place(x=280, y=240)

    # submit button
    submitButton = Button(canvas, text="Soumettre",
                          command=lambda: getMessage1(window, clientNameInput, startingDateInput, endingDateInput, enterpriseNameInput),
                          width=15,
                          height = 2)
    submitButton.place(x=250, y=300)

    canvas.place(x=0, y=0)


def message2Interface(window):
    canvas = Canvas(window, width=600, height=400)
    canvas.create_rectangle(0, 0, 600, 400, fill='#121212')

    # Form of the Message1
    #message1 title
    titleLabel = Label(canvas, text='Message 2', width= 15, height=2, font=('Arial', 15), background='#121212', foreground='white')
    titleLabel.place(x=220, y=10)

    #message description
    descriptionLabel = Label(canvas, text='Vous retourne la liste des entreprises vous ayant vendu ce produit.', font=('Arial', 10), background='#121212', foreground='white')
    descriptionLabel.place(x=100, y=70)

    #Rectangle wich will contain the form
    canvas.create_rectangle(150, 120, 450, 250, fill='#181818')

    # clientName
    clientNameLabel = Label(canvas, text="Nom du client :", font=('Arial', 10), background="#121212", foreground='white')
    clientNameInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    clientNameLabel.place(x=165, y=150)
    clientNameInput.place(x=280, y=150)

    # product name
    productNameLabel = Label(canvas, text="Produit Visé :", font=('Arial', 10), background="#121212", foreground='white')
    productNameInput = Entry(canvas, bd=0, font=('Arial', 10), background="#404040", foreground='white')

    productNameLabel.place(x=165, y=200)
    productNameInput.place(x=280, y=200)

    # submit button
    submitButton = Button(canvas, text="Soumettre",
                          command=lambda: getMessage2(window, clientNameInput, productNameInput),
                          width=15,
                          height = 2)
    submitButton.place(x=250, y=300)
    canvas.place(x=600, y=0)


def resultsBaseInterface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='#121212')

    canvas.create_rectangle(150, 60, 450, 170, fill='#181818')
    title1Label = Label(canvas, text='Requête', width= 15, height=1, font=('Arial', 15), background='#121212', foreground='white')
    title1Label.place(x=220, y=10)

    canvas.create_rectangle(750, 60, 1050, 170, fill='#181818')
    title2Label = Label(canvas, text='Résultat', width= 15, height=1, font=('Arial', 15), background='#121212', foreground='white')
    title2Label.place(x=820, y=10)
    
    canvas.place(x=0, y=400)
    return canvas

def results1OnlyDateInterface(window, total, clientName, startingDate, endingDate):
    canvas = resultsBaseInterface(window)

    clientLabel = Label(canvas, text="Nom du client :", font=('Arial', 10), background="#121212", foreground='white')
    startingDateLabel = Label(canvas, text="Date de Début :", font=('Arial', 10), background="#121212", foreground='white')
    endingDateLabel = Label(canvas, text="Date de Fin :", font=('Arial', 10), background="#121212", foreground='white')
    clientLabel.place(x = 165, y = 70)
    startingDateLabel.place(x = 165, y = 105)
    endingDateLabel.place(x = 165, y = 140)

    clientNameLabel = Label(canvas, text=clientName, font=('Arial', 10), background="#121212", foreground='white')
    startingDateNameLabel = Label(canvas, text=startingDate, font=('Arial', 10), background="#121212", foreground='white')
    endingDateNameLabel = Label(canvas, text=endingDate, font=('Arial', 10), background="#121212", foreground='white')
    clientNameLabel.place(x = 280, y = 70)
    startingDateNameLabel.place(x = 280, y = 105)
    endingDateNameLabel.place(x = 280, y = 140)

    totalNameLabel = Label(canvas, text='Total :', font=('Arial', 15), background="#121212", foreground='white')
    totalNameLabel.place(x = 780, y = 100)

    totalLabel = Label(canvas, text=str(total[0]), font=('Arial', 15), background="#121212", foreground='white')
    totalLabel.place(x = 900, y = 100)

def results1OnlyEnterpriseInterface(window, total, clientName, enterpriseName):
    canvas = resultsBaseInterface(window)

    clientLabel = Label(canvas, text="Nom du client :", font=('Arial', 10), background="#121212", foreground='white')
    productLabel = Label(canvas, text="Entreprise Visée :", font=('Arial', 10), background="#121212", foreground='white')
    clientLabel.place(x = 165, y = 80)
    productLabel.place(x = 165, y = 120)

    clientNameLabel = Label(canvas, text=clientName, font=('Arial', 10), background="#121212", foreground='white')
    productNameLabel = Label(canvas, text=enterpriseName, font=('Arial', 10), background="#121212", foreground='white')
    clientNameLabel.place(x = 280, y = 80)
    productNameLabel.place(x = 280, y = 120)

    totalNameLabel = Label(canvas, text='Total :', font=('Arial', 15), background="#121212", foreground='white')
    totalNameLabel.place(x = 780, y = 100)

    totalLabel = Label(canvas, text=str(total[0]), font=('Arial', 15), background="#121212", foreground='white')
    totalLabel.place(x = 900, y = 100)

def results1AllInterface(window, total, clientName, startingDate, endingDate, enterpriseName):
    canvas = resultsBaseInterface(window)

    clientLabel = Label(canvas, text="Nom du client :", font=('Arial', 10), background="#121212", foreground='white')
    startingDateLabel = Label(canvas, text="Date de Début :", font=('Arial', 10), background="#121212", foreground='white')
    endingDateLabel = Label(canvas, text="Date de Fin :", font=('Arial', 10), background="#121212", foreground='white')
    enterpriseNameLabel = Label(canvas, text="Entreprise Visée :", font=('Arial', 10), background="#121212", foreground='white')
    clientLabel.place(x = 165, y = 70)
    startingDateLabel.place(x = 165, y = 95)
    endingDateLabel.place(x = 165, y = 120)
    enterpriseNameLabel.place(x = 165, y = 145)


    clientNameLabel = Label(canvas, text=clientName, font=('Arial', 10), background="#121212", foreground='white')
    startingDateNameLabel = Label(canvas, text=startingDate, font=('Arial', 10), background="#121212", foreground='white')
    endingDateNameLabel = Label(canvas, text=endingDate, font=('Arial', 10), background="#121212", foreground='white')
    enterpriseLabel = Label(canvas, text=enterpriseName, font=('Arial', 10), background="#121212", foreground='white')
    clientNameLabel.place(x = 280, y = 70)
    startingDateNameLabel.place(x = 280, y = 95)
    endingDateNameLabel.place(x = 280, y = 120)
    enterpriseLabel.place(x = 280, y = 145)

    totalNameLabel = Label(canvas, text='Total :', font=('Arial', 15), background="#121212", foreground='white')
    totalNameLabel.place(x = 780, y = 100)

    totalLabel = Label(canvas, text=str(total[0]), font=('Arial', 15), background="#121212", foreground='white')
    totalLabel.place(x = 900, y = 100)

#Function wich is displaying the results of the number 2 request
def results2Interface(window, enterpriseList, clientName, productName):
    canvas = resultsBaseInterface(window)

    clientLabel = Label(canvas, text="Nom du client :", font=('Arial', 10), background="#121212", foreground='white')
    productLabel = Label(canvas, text="Produit Visé :", font=('Arial', 10), background="#121212", foreground='white')
    clientLabel.place(x = 165, y = 80)
    productLabel.place(x = 165, y = 120)

    clientNameLabel = Label(canvas, text=clientName, font=('Arial', 10), background="#121212", foreground='white')
    productNameLabel = Label(canvas, text=productName, font=('Arial', 10), background="#121212", foreground='white')
    clientNameLabel.place(x = 280, y = 80)
    productNameLabel.place(x = 280, y = 120)

    enterpriseLabel = Label(canvas, text='Liste :', font=('Arial', 15), background="#121212", foreground='white')
    enterpriseLabel.place(x = 780, y = 100)

    scroll = Scrollbar(canvas, activebackground="#181818")
    scroll.place(x=1010, y=90)

    enterpriseNameLabel = Listbox(canvas, font=('Arial', 10), background="#121212", foreground='white', yscrollcommand=scroll.set, width=15, height=4)
    enterpriseNameLabel.place(x = 900, y = 80)
    for i in range(0, len(enterpriseList)):
        enterpriseNameLabel.insert(i, enterpriseList[i])




