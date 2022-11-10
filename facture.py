
# analyse/Fact.02_03_2022.txt

import os.path

montantTest = ["ttc" ,"prélever","prélevé","payer"]
prixTest=['0','1','2','3','4','5','6','7','8','9' ]

clientTest = ["client"]
noClient = [":","="]

adresseTestLieu = ["lieu"]
adresseTestRue = ["rue"]

produitTest = ["produit","produits"]

siretTest = ["rcs","siret"]

while True :
    try :
        # variable pour le montant
        tmpMot="start"

        # Récup nom fichier
        print("\nPour arrêter CTRL-C")
        name = input("Nom facture : ")
        
        with open(name, "r") as f :
            allFile = f.read()
            lignes = allFile.split("\n")
        lignes = [i.lower() for i in lignes if len(i.split()) != 0]

        prixOn = False
        prixDeja = False
        prix = ""

        cli = False
        clientDeja = False
        client = ""

        adr = True
        adresse = ""

        prod = False
        produitDeja = False
        produit = []
        produitNextLine = False

        siret = ""
        siretGo = 0
        siretDeja = False

        for l in lignes :
            if l.split()[0] in adresseTestLieu and adr:
                adresse = l
                adr = False

            if l.split()[0] in clientTest and not clientDeja:
                tmp = l.split()[1:]
                for i in tmp :
                    if not i in noClient :
                        client = client + " " + i
                client = client[1:]

            if l.split()[0] in produitTest and not produitDeja :
                prod = True
                produitDeja = True
            if prod and produitNextLine:
                prod = False
                produitNextLine = False
                produit.append(l)

            for mot in l.split() :
                if not prixDeja and tmpMot in montantTest :
                    prixOn = True
                if prixOn :
                    if not mot[len(mot)-1] in prixTest :
                        mot = mot[:-1]    
                    prix = mot
                    prixDeja = True
                    prixOn = False
                if mot in siretTest and not siretDeja:
                    siretGo = 3
                    siretDeja = False

                if siretGo != 0 :
                    if mot[0] in prixTest :
                        siret = siret +" "+ mot
                        siretGo -= 1

                tmpMot = mot
                
            if prod :    
                produitNextLine = True
        print(client)
        print(adresse)
        print(produit)
        print(prix)
        print(siret[1:])
        # faire une fonction et mettre un retun à la place des prints !! 

        

    except KeyboardInterrupt:
        print("\nBye !")
        break
    except FileNotFoundError:
        print("\nLe fichier n'existe pas ! Bye !")
        break

