f=open("analyse/sfr_facture_fixe.txt",'r')
#f=open("analyse/sfr_facture_mobil.txt",'r')
#f=open("analyse/facture_EDF.txt",'r')

# variable pour le montant
tmpMontant="start"
ligne = f.readline()
montant = 0
ttc = 0

# variable pour l'email
tmpEmail="ouioui@oui.oui"
email = 0

while(ligne != '') :
    ligne = ligne.split()

    for mot in ligne :
        # test pour récup la Ligne du montant 
        if mot == "Montant" :
            montant = 1
        if mot == "TTC" or mot =="prélever" or mot == "prélevé":
            ttc = 1
        # test de récup du prix
        if mot=='€' and montant and ttc:
            # enlève les caractères collés au prix
            if tmpMontant[0]!='0' and tmpMontant[0]!='1' and tmpMontant[0]!='2' and tmpMontant[0]!='3' and tmpMontant[0]!='4' and tmpMontant[0]!='5' and tmpMontant[0]!='6' and tmpMontant[0]!='7' and tmpMontant[0]!='8' and tmpMontant[0]!='9' :
                tmpMontant=tmpMontant[1:]    
            # ICI MISE EN BDD
            print(tmpMontant)
        tmpMontant=mot

        if mot == "email" :
            email += 1
        if email == 2 :
            tmpEmail = mot
            print(tmpEmail)
            email = 0
        if email == 1 and mot ==':' :
            email += 1
        
        
    # passage à la ligne suivante
    ligne = f.readline()
    montant = 0
    ttc = 0

f.close()
