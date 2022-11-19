from tkinter import *
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json

currentFilePath = ""

class Watcher:
    DIRECTORY_TO_WATCH = "simulation_reseau/responses"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = EventHandler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()

        time.sleep(10)
        self.observer.stop()

        self.observer.join()


class EventHandler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        global currentFilePath
        if event.event_type == 'created':
            print("Creation of : ", event.src_path)
            currentFilePath = event.src_path


def awaitingResponse():
    w = Watcher()
    w.run()

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
        enterpriseList = readJson()
        results1OnlyDateInterface(window)
    elif (enterpriseName != '') and (startingDate != '' and endingDate != ''):
        print("Date and Enterprise Case")
        # Launching JSON Generation Process

        awaitingResponse()
        enterpriseList =readJson()
        results1AllInterface(window)
    elif (enterpriseName != '') and (startingDate == '' and endingDate == ''):
        print("Enterprise case")
        # Launching JSON Generation Process

        awaitingResponse()
        enterpriseList = readJson()
        results1OnlyEnterpriseInterface(window)


def getMessage2(window, clientNameInput, productNameInput):
    clientName = clientNameInput.get()
    productName = productNameInput.get()

    if (clientName == '' or productName == ''):
        print("Error : Empty Fields")
    else:
        # Launching the JSON Generation Process

        # Awaiting for the response
        awaitingResponse()
        total = readJson()
        results2Interface(window, total, clientName, productName)

def readJson():
    global currentFilePath
    with open(currentFilePath, 'r') as file:
        data = json.load(file)
        total = []
        # We try the type of the message
        messageType = data['reponse']['type']
        discussionID = data['reponse']['id_discussion']
        clientName = data['reponse']['nom_client']
        if (messageType == 1):
            enterpriseList = data['reponse']['liste_entreprises']
            return enterpriseList
            print(enterpriseList)
        elif (messageType == 2):
            total.append(data['reponse']['total'])
            return total
            print(total)
        else:
            print("Error")
            exit(0)

def display():
    window = Tk()
    window.geometry("1202x802")
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
    results2Interface(window, [65000], "Giroud", "Buts")


def message1Interface(window):
    # Background of the Canvas
    canvas = Canvas(window, width=600, height=600)
    canvas.create_rectangle(0, 0, 600, 600, fill='black')

    # Form of the Message1
    # clientName
    clientNameLabel = Label(canvas, text="Nom Client :")
    clientNameInput = Entry(canvas, bd=0)

    clientNameLabel.place(x=100, y=100)
    clientNameInput.place(x=200, y=100)

    # starting date
    startingDateLabel = Label(canvas, text="Date Début :")
    startingDateInput = Entry(canvas, bd=0)

    startingDateLabel.place(x=100, y=130)
    startingDateInput.place(x=200, y=130)

    # ending date
    endingDateLabel = Label(canvas, text="Date Fin :")
    endingDateInput = Entry(canvas, bd=0)

    endingDateLabel.place(x=100, y=160)
    endingDateInput.place(x=200, y=160)

    # enterprise name
    enterpriseNameLabel = Label(canvas, text="Entreprise :")
    enterpriseNameInput = Entry(canvas, bd=0)

    enterpriseNameLabel.place(x=100, y=190)
    enterpriseNameInput.place(x=200, y=190)

    # submit button
    submitButton = Button(canvas, text="Soumettre",
                          command=lambda: getMessage1(window, clientNameInput, startingDateInput, endingDateInput, enterpriseNameInput))
    submitButton.place(x=220, y=220)

    canvas.place(x=0, y=0)


def message2Interface(window):
    canvas = Canvas(window, width=600, height=600)
    canvas.create_rectangle(0, 0, 600, 600, fill='black')

    # Form of the Message1
    # clientName
    clientNameLabel = Label(canvas, text="Nom Client :")
    clientNameInput = Entry(canvas, bd=0)

    clientNameLabel.place(x=100, y=100)
    clientNameInput.place(x=200, y=100)

    # product name
    productNameLabel = Label(canvas, text="Produit :")
    productNameInput = Entry(canvas, bd=0)

    productNameLabel.place(x=100, y=130)
    productNameInput.place(x=200, y=130)

    # submit button
    submitButton = Button(canvas, text="Soumettre",
                          command=lambda: getMessage2(window, clientNameInput, productNameInput))
    submitButton.place(x=220, y=220)
    canvas.place(x=600, y=0)


def resultsBaseInterface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='black')
    canvas.place(x=0, y=600)

def results1OnlyDateInterface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='red')
    canvas.place(x=0, y=600)

def results1OnlyEnterpriseInterface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='green')
    canvas.place(x=0, y=600)

def results1AllInterface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='orange')
    canvas.place(x=0, y=600)

#Function wich is displaying the results of the number 2 request
def results2Interface(window, total, clientName, productName):
    clientNameLabel = Label(window, text=clientName)
    productNameLabel = Label(window, text=productName)
    totalLabel = Label(window, text=str(total[0]))
    totalLabel.place(x = 50, y = 650)
    clientNameLabel.place(x = 50, y = 700)
    productNameLabel.place(x = 50, y = 750)
