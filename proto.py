#analyse/sfr_facture_fixe.txt
#analyse/sfr_facture_mobil.txt
#analyse/facture_EDF.txt
#analyse/Facture_topachat.txt
#analyse/Facture_place_concert.txt
#analyse/Fact.02_03_2022.txt

import os.path

mailType = ["hotmail","gmail","orange","sfr","free"]
mailTerm = ["fr", "com"]

montantTest = ["ttc" ,"prélever","prélevé","payer"]
prixTest=['0','1','2','3','4','5','6','7','8','9' ]

while True :
    try :
        # variable pour le montant
        tmpMontant="start"
        montant = 0
        ttc = 0
        nl = 0

        email="OuiOui@gmail.com"

        # Récup nom fichier
        print("\nPour arrêter CTRL-C")
        name = input("Nom facture : ")
        
        with open(name, "r") as f :
            allFile = f.read()
            lignes = allFile.split("\n")

        for l in lignes :
            try :
                if nl == 1 and montant :
                    if not l[len(l)-1] in prixTest :
                        l = l[:-1]
                    numb = float(l)
                    nl=0
                    montant = 0
                    print(l)
            except ValueError : 
                pass
            ligne = l.split()

            for mot in ligne :
                mot = mot.lower()
                # test pour récup la Ligne du montant 
                if mot == "montant" :
                    montant = 1
                    nl = 1
                if mot in montantTest:
                    ttc = 1
                    print(tmpMontant)
                
                # enlève les caractères collés au prix
                taille = len(tmpMontant)-1
                if not tmpMontant[taille] in prixTest :
                    tmpMontant=tmpMontant[:-1]    
                
                if mot=='€' and montant : #and ttc :
                    # ICI MISE EN BDD
                    nl=0
                    montant = 0
                    
                tmpMontant=mot
                # test de récup du prix
                
                # Récup email
                if mot.find("@") != -1 :
                    for typ in mailType :
                        for ter in mailTerm :
                            if mot[mot.find("@")+1:] == typ+"."+ter :
                                email = mot
                                print(email)
                                # ICI RÉCUP DU MAIL (ID)
                
            montant = 0
            ttc = 0
    except KeyboardInterrupt:
        print("\nBye !")
        break

