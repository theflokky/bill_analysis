import os.path

montantTest = ["ttc" ,"prélever","prélevé","payer"]
prixTest=['0','1','2','3','4','5','6','7','8','9' ]

clientTest = ["client"]
noClient = [":","="]

adresseTestLieu = ["adresse"]

produitTest = ["produit","désignation","description"]

siretTest = ["rcs","siret","siren"]

files = ["analyse/Fact.02_03_2022.txt","analyse/22856.txt","analyse/4055919.txt","analyse/4369173.txt"]

def fact(name):
    
    # variable pour le montant
    tmpMot="start"
        
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

    adr = False
    adresse = ""

    produit = []

    siret = ""
    siretGo = 0
    siretDeja = False

    for l in lignes :
        if l.split()[0] in clientTest and not clientDeja:
            tmp = l.split()[1:]
            for i in tmp :
                if not i in noClient :
                    client = client + " " + i
            client = client[1:]
            clientDeja = True

        if l.split()[0] in produitTest :
            tmp = l.split()[1:]
            temp = ""
            for i in tmp :
                if not i in noClient :
                    temp = temp + " " + i
            temp = temp[1:]
            produit.append(temp)

        for mot in l.split() :
            if mot in adresseTestLieu and not adr:
                tmp = l.split()[1:]
                for i in tmp :
                    if not i in noClient :
                        adresse = adresse + " " + i
                adresse = adresse[1:]
                adr = True
            
            if not prixDeja and tmpMot in montantTest :
                prixOn = True
            if prixOn and not mot in noClient :
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
        
    return(client,adresse,produit,prix,siret[1:])
    #print(client)
    #print(adresse)
    #print(produit)
    #print(prix)
    #print(siret[1:])
    # faire une fonction et mettre un retun à la place des prints !! 


if __name__ == "__main__" :
    for i in files :
        fact(i)
        print()
