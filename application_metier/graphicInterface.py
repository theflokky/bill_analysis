from tkinter import *

# Base function for the graphic interface


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
    results1Interface(window)


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
                          command=lambda: getMessage1(clientNameInput, startingDateInput, endingDateInput, enterpriseNameInput))
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
                          command=lambda: getMessage2(clientNameInput, productNameInput))
    submitButton.place(x=220, y=220)
    canvas.place(x=600, y=0)


def results1Interface(window):
    canvas = Canvas(window, width=1200, height=200)
    canvas.create_rectangle(0, 0, 1200, 200, fill='black')
    canvas.place(x=0, y=600)


def getMessage1(clientNameInput, startingDateInput, endingDateInput, enterpriseNameInput):
    clientName = clientNameInput.get()
    startingDate = startingDateInput.get()
    endingDate = endingDateInput.get()
    enterpriseName = enterpriseNameInput.get()

    print("Error : Empty Fields")


def getMessage2(clientNameInput, productNameInput):
    clientName = clientNameInput.get()
    productName = productNameInput.get()

    if (clientName == '' or productName == ''):
        print("Error : Empty Fields")
    # else:
        # Launching the JSON Generation Process
