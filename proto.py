#f=open("analyse/sfr_facture_fixe.txt",'r')
#f=open("analyse/sfr_facture_mobil.txt",'r')
f=open("analyse/facture_EDF.txt",'r')

tmp="start"
ligne = f.readline()
montant = 0
ttc = 0

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
            if tmp[0]!='0' and tmp[0]!='1' and tmp[0]!='2' and tmp[0]!='3' and tmp[0]!='4' and tmp[0]!='5' and tmp[0]!='6' and tmp[0]!='7' and tmp[0]!='8' and tmp[0]!='9' :
                tmp=tmp[1:]
            
            # ICI MISE EN BDD
            print(tmp)
        tmp=mot
    # passage à la ligne suivante
    ligne = f.readline()
    montant = 0
    ttc = 0

f.close()
